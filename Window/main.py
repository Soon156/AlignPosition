import os
import threading
import time
import logging as log
from datetime import datetime

import cv2
import zroya
from PySide6 import QtCharts
from PySide6.QtCore import Slot, Qt, QSize, QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QSizePolicy, QLineEdit, QFileDialog
from PySide6.QtCharts import QBarSet, QBarSeries, QBarCategoryAxis, QChart, QChartView
from PySide6.QtGui import QPainter, QPixmap, QImage
from Funtionality.Config import model_file, get_config, write_config, logo_path, get_available_cameras, create_config, \
    key_file_path, desktop_path
from Funtionality.Notification import first_notify, show_break, set_elapsed_time
from ParentalControl.AppUseTime import update_condition
from ParentalControl.Auth import change_password, login_user, read_use_time, \
    read_app_use_time, user_register
from ParentalControl.Backup_Restore import extract_zip, zip_files
from PostureRecognize.ElapsedTime import seconds_to_hms
from PostureRecognize.FrameProcess import LandmarkExtractor, temp_backup_restore
from PostureRecognize.Model import train_model
from PostureRecognize.PositionDetect import PostureRecognizerThread, read_elapsed_time_data
from .OverlayWindow import OverlayWidget
from .ui_MainMenu import Ui_MainWindow
from .minWindow import MinWindow
from pystray import Menu, Icon, MenuItem
from PIL.Image import open

Good_Posture = "Maintain your good posture 5 seconds, clicked proceed to Start"
Bad_Posture = "Maintain your bad posture 5 seconds, clicked proceed to Start"
Append_Posture = "Append bad posture, clicked proceed to Start"
Cancel_Calibrate = "Calibration Cancel"
Append_Finish = "Append done"
Model_Training = "Training model, please wait patiently...."
Capture_Posture = "Capturing posture, stay still...."
Cancel = "Cancelling..."


class TrainModel(QThread):
    error_msg = Signal(str)

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):
        try:
            train_model()
            self.train_finished()
        except Exception as e:
            self.error_msg.emit(str(e))

    def train_finished(self):
        self.parent().recalibrate_btn.setText("Re-Calibrate")
        self.parent().append_btn.show()
        if self.arg == "calibrate":
            log.info("Calibrate Success")
            self.parent().hint_lbl.setText("Calibrate finish")
        elif self.arg == "append":
            log.info("Append Success")
            self.parent().hint_lbl.setText("Append finish")
        self.parent().monitor_btn.setText("Start")
        self.parent().check_model()
        self.parent().proceed_btn.hide()
        self.parent().proceed_btn.setEnabled(True)
        self.parent().cancel_btn.hide()
        self.parent().is_capturing = False


class StartPreview(QThread):
    error_msg = Signal(str)

    def __init__(self, index):
        super().__init__()
        self.index = index
        self.condition = True

    def run(self):
        try:
            self.parent().camera = cv2.VideoCapture(self.index, cv2.CAP_DSHOW)
            while self.condition:

                ret, frame = self.parent().camera.read()
                if ret:
                    # Flip the frame horizontally
                    frame = cv2.flip(frame, 1)

                    # Resize the frame to fit the label
                    frame = cv2.resize(frame, (640, 360))

                    # Convert the OpenCV frame to QImage
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = frame.shape
                    bytes_per_line = ch * w
                    q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

                    # Convert the QImage to QPixmap for display
                    pixmap = QPixmap.fromImage(q_image)

                    # Set the pixmap on the image label
                    self.parent().calibrate_preview_lbl.setPixmap(pixmap)
                else:
                    raise Exception("Camera read failed")
        except Exception as e:
            log.error(e)
            self.error_msg.emit(str(e))

    def stop_preview(self):
        self.condition = False
        self.parent().camera.release()


class CalibrateThread(QThread):
    finish = Signal(str)
    error_msg = Signal(str)

    def __init__(self, cat):
        super().__init__()
        self.cat = cat

    def run(self):
        self.parent().hint_lbl.setText(Capture_Posture)
        le = LandmarkExtractor()
        try:
            le.extract_landmarks_and_buffer_frames(self.parent(), self.cat)
        except Exception as e:
            self.error_msg.emit(str(e))

        # Check if the stop signal is emitted
        if self.isInterruptionRequested():
            return

        if self.cat == "good":
            self.calibrate_finished("good")
        elif self.cat == "append":
            self.calibrate_finished("append")
        else:
            self.calibrate_finished("calibrate")

    def calibrate_finished(self, mode):
        if mode == "good":
            self.parent().hint_lbl.setText(Bad_Posture)
            self.parent().proceed_btn.setEnabled(True)
        else:
            self.parent().hint_lbl.setText(Model_Training)
            self.finish.emit(mode)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # Window Attribute
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.center()  # Window draggable

        # SET DEFAULT STATE
        # Connect object
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.max_btn.clicked.connect(self.keyPressEvent)
        self.dashboard_btn.clicked.connect(self.dashboard_page)
        self.parental_btn.clicked.connect(self.parental_page)
        self.calibrate_btn.clicked.connect(self.calibration_page)
        self.settings_btn.clicked.connect(self.settings_page)

        # Dashboard page
        self.popout_btn.clicked.connect(self.min_window)
        self.use_time_btn.clicked.connect(self.show_chart)
        self.use_time_btn.setText("Program Use Time")

        # Calibrate page
        self.recalibrate_btn.clicked.connect(lambda: self.calibrate(True))
        self.append_btn.clicked.connect(lambda: self.calibrate(False))
        self.proceed_btn.clicked.connect(self.capture)
        self.cancel_btn.clicked.connect(self.cancel_ops)
        for index, device_name in get_available_cameras().items():
            self.calibrate_camera_box.addItem(device_name, index)
        self.calibrate_camera_box.currentIndexChanged.connect(self.calibrate_camera_box_handler)

        # Settings page
        self.init_setting_page()
        self.reset_btn.clicked.connect(create_config)
        self.apply_btn.clicked.connect(self.update_setting)
        self.values = get_config()

        # Authenticate page
        self.PIN_line.setEchoMode(QLineEdit.Password)
        self.old_PIN_line.setEchoMode(QLineEdit.Password)
        self.new_PIN_line.setEchoMode(QLineEdit.Password)
        self.confirm_PIN_line.setEchoMode(QLineEdit.Password)
        self.PIN_btn.clicked.connect(self.valid_pin)

        # Parental page
        self.changePIN_btn.clicked.connect(self.change_pin_page)
        self.exct_data_btn.clicked.connect(self.extract_data)
        self.restore_btn.clicked.connect(self.restore_data)
        self.restore_btn.setEnabled(True)

        # Init variable
        self.w = None
        self.w1 = None
        self.dragPos = None
        self.start_time = 0
        self.monitoring_state = False
        self.dashboard_page()  # Set the page
        self.posture_recognizer = PostureRecognizerThread()
        self.posture_recognizer.error_msg.connect(self.error_handler)
        self.posture_recognizer.elapsed_time_updated.connect(self.update_elapsed_time_label)
        self.posture_recognizer.update_overlay.connect(self.update_overlay)
        self.calibrate_thread = None
        self.preview_thread = None
        self.camera = None
        self.is_capturing = False  # Flag to indicate if capturing is in progress
        self.tut_chart()  # Show chart
        self.login_state = False
        self.temp = None
        self.training_thread = None

        # System tray icon
        self.image = open(logo_path)
        self.system_icon = Icon("AlignPosition", self.image, menu=Menu(
            MenuItem("Show", self.if_visible, default=True),
            MenuItem("Detection", None),
            MenuItem("Exit", self.exit_app)
        ))
        self.system_icon.run_detached()

    def if_visible(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

    # Page handler
    def dashboard_page(self):
        self.stop_preview()
        self.page_title_lbl.setText("Dashboard")
        self.cont_stackedwidget.setCurrentIndex(0)
        self.use_time_lbl.setText(seconds_to_hms(read_elapsed_time_data()))
        self.tut_chart()
        self.check_model()

    def parental_page(self):
        self.stop_preview()
        self.page_title_lbl.setText("Parental Control")
        self.cont_stackedwidget.setCurrentIndex(4)
        if self.login_state:
            self.cont_stackedwidget.setCurrentIndex(1)
        else:
            if os.path.exists(key_file_path):
                self.PIN_stackedwidget.setCurrentIndex(1)
                self.change_PIN_btn.clicked.connect(self.change_pin)
            else:
                self.OldPINFrame.hide()
                self.PIN_stackedwidget.setCurrentIndex(0)
                self.change_PIN_btn.clicked.connect(lambda: self.change_pin(True))
        self.change_PIN_hint_lbl.hide()
        self.PIN_hint_lbl.hide()

    def calibration_page(self):
        self.hint_lbl.hide()
        self.page_title_lbl.setText("Calibration")
        self.cont_stackedwidget.setCurrentIndex(2)
        self.check_model()
        self.proceed_btn.hide()
        self.cancel_btn.hide()
        self.calibrate_camera_box_handler(int(get_config().get('camera')))

    def settings_page(self):
        self.stop_preview()
        self.page_title_lbl.setText("Settings")
        self.cont_stackedwidget.setCurrentIndex(3)
        self.init_setting_page()

    def min_window(self):
        self.w = MinWindow(self)
        self.w.show()

    def overlay_win(self):
        self.w1 = OverlayWidget()
        self.w1.setScreen(self.screen())
        self.w1.hide()

    def check_model(self):  # If model file exist
        if os.path.exists(model_file):
            try:
                self.monitor_btn.clicked.disconnect(self.calibration_page)
                self.monitor_btn.clicked.disconnect(self.start_monitoring)
            except:
                pass
            self.monitor_btn.clicked.connect(self.start_monitoring)
            if self.monitoring_state:
                self.monitor_btn.setText("Stop")
            else:
                self.monitor_btn.setText("Start")
            self.recalibrate_btn.setText("Recalibrate")
            self.append_btn.show()
        else:
            log.warning("Model file not found")
            self.monitor_btn.setText("Calibrate")
            self.recalibrate_btn.setText("Calibrate")
            self.append_btn.hide()
            self.monitor_btn.clicked.connect(self.calibration_page)

    # Monitoring
    def start_monitoring(self):
        if self.monitoring_state:
            self.monitoring_state = False
            self.monitor_btn.setText("Start")
            self.posture_recognizer.stop_capture()
            self.w1.hide()
            log.info("Monitoring stop")
        else:
            self.monitoring_state = True
            self.monitor_btn.setText("Stop")
            self.start_time = time.time()
            if self.values['overlay_enable'] == "True":
                self.overlay_win()
                self.w1.show()
            try:
                self.posture_recognizer.start()
            except Exception as e:
                log.error(e)
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
                self.exit_app()
            log.info("Monitoring start")

    @Slot(int)
    def update_elapsed_time_label(self, elapsed_time):
        var = get_config()
        self.use_time_lbl.setText(seconds_to_hms(elapsed_time))
        try:
            self.w.use_time_lbl.setText(seconds_to_hms(elapsed_time))
        except:
            pass
        set_elapsed_time(elapsed_time)
        a = time.time() - self.start_time
        b = float(var.get('rest')) * 60
        if a >= b:
            thread = threading.Thread(target=show_break)
            thread.start()
            self.start_time = time.time()

    def update_overlay(self, posture):
        self.w1.change_state(posture)

    # Parental Control
    def valid_pin(self):
        if login_user(self.PIN_line.text()):
            if self.PIN_checkbox.isChecked():
                self.login_state = True
            self.cont_stackedwidget.setCurrentIndex(1)
        else:
            self.PIN_hint_lbl.setText("Incorrect PIN")
            self.PIN_hint_lbl.show()

    def change_pin(self, cond=False):  # True: create new PIN for first time user
        old = self.old_PIN_line.text()
        new1 = self.new_PIN_line.text()
        new2 = self.confirm_PIN_line.text()
        if new1 != "" and new2 != "":
            if new1 == new2:
                if len(new1) >= 6 and new1.isdigit():
                    if cond:
                        user_register(self.new_PIN_line.text())
                        self.cont_stackedwidget.setCurrentIndex(1)
                    else:
                        if change_password(old, new1):
                            QMessageBox.information(self, "PIN changed", "Password changed successfully")
                            self.cont_stackedwidget.setCurrentIndex(1)
                            self.OldPINFrame.show()
                        else:
                            self.change_PIN_hint_lbl.setText("Incorrect PIN")
                            self.change_PIN_hint_lbl.show()
                else:
                    self.change_PIN_hint_lbl.setText("6-digits PIN required")
                    self.change_PIN_hint_lbl.show()
            else:
                self.change_PIN_hint_lbl.setText("PIN does not matched")
                self.change_PIN_hint_lbl.show()
        else:
            self.change_PIN_hint_lbl.setText("Fill in the blank")
            self.change_PIN_hint_lbl.show()

    def change_pin_page(self):
        self.cont_stackedwidget.setCurrentIndex(4)
        self.PIN_stackedwidget.setCurrentIndex(0)

    def extract_data(self):
        path = os.path.join(desktop_path, "Use_Time_Extract.zip")
        zip_files(path)
        QMessageBox.information(self, "Success", f"Use time extract to {path}")

    def restore_data(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle('Warning')
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText('This action will overwrite the exist data\nDo you wish to continue?')
        msgbox.addButton('Yes', QMessageBox.YesRole)
        msgbox.addButton('No', QMessageBox.NoRole)
        result = msgbox.exec()
        if result == 0:
            file_path, type = QFileDialog.getOpenFileName(self, "Open File", "", "(*.zip)")
            if file_path != "":
                try:
                    extract_zip(file_path)
                except Exception as e:
                    QMessageBox.warning(self, "Failed", f"{e}")

    # Calibration
    def calibrate_camera_box_handler(self, index):
        self.stop_preview()
        if not self.monitoring_state:
            self.calibrate_camera_box.setEnabled(True)
            self.recalibrate_btn.setEnabled(True)
            self.append_btn.setEnabled(True)

            if index != -1:
                try:
                    self.preview_thread.wait()
                except:
                    pass
                self.preview_thread = StartPreview(index)
                self.preview_thread.setParent(self)
                self.preview_thread.error_msg.connect(self.error_handler)
                self.preview_thread.start()

        else:
            self.calibrate_camera_box.setEnabled(False)
            self.recalibrate_btn.setEnabled(False)
            self.append_btn.setEnabled(False)
            self.calibrate_preview_lbl.setText("Stop the monitoring to start calibrate")

    def stop_preview(self):
        try:
            self.preview_thread.stop_preview()
        except:
            pass

    def capture(self):
        if not self.is_capturing or self.hint_lbl.text() == Bad_Posture:
            self.is_capturing = True
            self.proceed_btn.setEnabled(False)
            try:
                if self.hint_lbl.text() == Good_Posture:
                    self.calibrate_thread = CalibrateThread("good")
                elif self.hint_lbl.text() == Bad_Posture:
                    self.calibrate_thread = CalibrateThread("bad")
                elif self.hint_lbl.text() == Append_Posture:
                    self.calibrate_thread = CalibrateThread("append")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.calibrate_thread.finish.connect(self.start_train)
            self.calibrate_thread.error_msg.connect(self.error_handler)
            self.calibrate_thread.setParent(self)
            self.calibrate_thread.start()

    def error_handler(self, msg):
        QMessageBox.warning(self, "Warning", f"An error occurred: {msg}")
        if msg.startswith("Model accuracy too low:"):
            self.cancel_ops(cond=True)

    def start_train(self, mode):
        self.training_thread = TrainModel(mode)
        self.training_thread.setParent(self)
        self.training_thread.error_msg.connect(self.error_handler)
        self.training_thread.start()
        self.calibrate_thread = None

    def calibrate(self, cond):  # False: append, True: calibrate/recalibrate
        log.info("Calibration start")
        try:
            self.temp.join()
        except:
            pass
        self.temp = threading.Thread(target=temp_backup_restore)
        self.temp.start()
        self.proceed_btn.show()
        self.cancel_btn.show()
        self.append_btn.hide()
        self.recalibrate_btn.hide()
        self.hint_lbl.show()
        if cond:
            self.hint_lbl.setText(Good_Posture)
        else:
            self.hint_lbl.setText(Append_Posture)

    def cancel_ops(self, cond=None):
        try:
            self.temp.join()
        except:
            pass
        self.training_thread = None
        self.calibrate_thread = None

        self.check_model()

        self.temp = threading.Thread(target=temp_backup_restore, args=("True",))
        self.temp.start()
        self.proceed_btn.hide()
        self.proceed_btn.setEnabled(True)
        self.cancel_btn.hide()
        self.recalibrate_btn.show()
        self.is_capturing = False
        if cond is None:
            self.hint_lbl.setText(Cancel_Calibrate)
            log.info(Cancel_Calibrate)
        else:
            self.hint_lbl.setText("Please try again with different posture")

    # Settings
    def init_setting_page(self):
        values = get_config()
        # Set value from config
        if values.get('background') == "True":
            self.background_box.setChecked(True)
        else:
            self.background_box.setChecked(False)

        if values.get('auto') == "True":
            self.start_box.setChecked(True)
        else:
            self.start_box.setChecked(False)

        if values.get('app_tracking') == "True":
            self.app_time_track_box.setChecked(True)
        else:
            self.app_time_track_box.setChecked(False)

        if values.get('notifications') == "True":
            self.notify_box.setChecked(True)
        else:
            self.notify_box.setChecked(False)

        self.camera_box.clear()
        for index, device_name in get_available_cameras().items():
            self.camera_box.addItem(device_name, index)

        self.reminder_box.setValue(float(values.get('rest')))

        index = self.alert_box.findText(values.get('overlay'))
        self.alert_box.setCurrentIndex(index)

    def update_setting(self):
        break_time = self.reminder_box.value()
        if break_time <= 1:
            QMessageBox.warning(self, "Action not allowed", "Break time cannot smaller than 1 minute")
        else:
            if self.background_box.isChecked():
                self.values['background'] = "True"
                log.info(f"Background Enable")
            else:
                self.values['background'] = "False"
                log.info(f"Background Disable")

            if self.start_box.isChecked():
                self.values['auto'] = "True"
                log.info(f"Startup Enable")
            else:
                self.values['auto'] = "False"
                log.info(f"Startup Disable")

            if self.app_time_track_box.isChecked():
                self.values['app_tracking'] = "True"
                log.info(f"App Tracking Enable")
            else:
                self.values['app_tracking'] = "False"
                log.info(f"App Tracking Disable")

            if self.notify_box.isChecked():
                self.values['notifications'] = "True"
                log.info(f"Break Notification Enable")
            else:
                self.values['notifications'] = "False"
                log.info(f"Break Notification Disable")

            break_time = self.reminder_box.value()
            if not str(break_time) == self.values['rest']:
                self.values['rest'] = break_time
                log.info(f"New break time: {break_time}")

            index = self.camera_box.currentIndex()
            if not str(index) == self.values['camera']:
                self.values['camera'] = index
                log.info(f"Camera change to {index}")

            pos = self.alert_box.currentText()
            if not str(pos) == self.values['overlay']:
                self.values['overlay'] = pos
                log.info(f"Overlay change to {pos} side")

            write_config(self.values)
            self.values = get_config()

    # Chart list
    def tut_chart(self):
        rows = read_use_time()
        rows.reverse()
        # Create a single QBarSet to hold the data values
        bar_set = QBarSet("Data Values")
        categories = []
        temp = []
        # Add data values to the bar_set
        for item in rows[:7]:
            temp.append(item)
        temp.reverse()
        for item in temp:
            bar_set.append(int(item[1]) / 60)
            categories.append(datetime.strptime(item[0], "%Y-%m-%d").strftime("%b %d"))

        # Create a QBarSeries and add the bar_set to it
        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Total Use Time")

        # Set up the X-axis with the date categories
        axis = QBarCategoryAxis()
        axis.append(categories)

        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        y_axis = chart.axisY()
        y_axis.setTitleText("Use Time (min)")

        chart.legend().setVisible(False)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.chart().setTheme(QChart.ChartThemeDark)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(chart_view.sizePolicy().hasHeightForWidth())
        chart_view.setSizePolicy(size_policy)
        self.update_chart(chart_view)

    def put_chart(self):
        data = read_app_use_time()
        # Calculate the total time for each app
        app_total_time = {}
        date_list = []
        for date in data:
            if date not in date_list:
                date_list.append(datetime.strptime(date, "%Y-%m-%d").strftime("%b %d"))
            for app in data[date]:
                app_total_time[app] = app_total_time.get(app, 0) + data[date][app]

        # Sort the apps based on total time in descending order
        sorted_apps = sorted(app_total_time.items(), key=lambda x: x[1], reverse=True)
        top_7_apps = [app for app, _ in sorted_apps[:7]]

        series = QtCharts.QStackedBarSeries()

        for app in top_7_apps:
            temp = []
            bar_set = QBarSet(app)
            for date in data:
                if app in data[date]:
                    use_timedate = round(data[date][app] / 60, 2)
                    temp.append(use_timedate)
            bar_set.append(temp)
            series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Program Use Time")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis = QBarCategoryAxis()
        axis.append(date_list)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # Set chart legend
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignRight)

        # set chart renderer and theme
        chart_view = QChartView(chart)
        chart_view.chart().setTheme(QChart.ChartThemeDark)
        chart_view.setRenderHint(QPainter.Antialiasing)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        chart_view.setSizePolicy(size_policy)
        self.update_chart(chart_view)

    def show_chart(self):
        # Update UI
        if self.use_time_btn.text() == "Program Use Time":
            self.use_time_btn.setText("Total Use Time")
            self.put_chart()
        else:
            self.use_time_btn.setText("Program Use Time")
            self.tut_chart()

    def update_chart(self, chart_view=None):
        chart_view.setMinimumSize(QSize(900, 300))
        while self.chart_cont.count() > 0:
            item = self.chart_cont.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.chart_cont.addWidget(chart_view)

    # Draggable handler
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    # Maximize handler
    def keyPressEvent(self, e):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # Close Event handler
    def closeEvent(self, event):
        event.ignore()
        var = get_config()
        # If background running is allowed
        if var.get('background') == "True":
            # If user is first time use the app
            if var.get('init') == "True":
                var['init'] = False
                write_config(var)
                log.info("First Time Launch")
                zroya.show(first_notify)
            self.hide()
        else:
            self.exit_app()

    def exit_app(self):
        update_condition()
        self.system_icon.stop()
        if self.monitoring_state:
            self.monitoring_state = False
            self.posture_recognizer.stop_capture()
        try:
            self.w.close()
        except:
            pass
        QApplication.exit()
