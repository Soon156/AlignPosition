import os
import sys
import threading
import time
import logging as log
from datetime import datetime

import zroya
from PySide6 import QtCharts
from PySide6.QtCore import Slot, Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QSizePolicy, QLineEdit, QFileDialog, \
    QTableWidgetItem
from PySide6.QtCharts import QBarSet, QBarSeries, QBarCategoryAxis, QChart, QChartView
from PySide6.QtGui import QPainter, QColor, QDesktopServices, QIcon
from Funtionality.Config import model_file, get_config, get_available_cameras, create_config, \
    key_file_path, desktop_path, Bad_Posture, Good_Posture, Append_Posture, Cancel_Calibrate, Capture_Posture, \
    Model_Training, abs_logo_path
from Funtionality.UpdateConfig import write_config, tracking_instance
from Funtionality.Notification import first_notify, show_break
from ParentalControl.Auth import change_password, login_user, read_use_time, \
    read_app_use_time, user_register, save_table_data, retrieve_table_data
from ParentalControl.Backup_Restore import extract_zip, zip_files
from ParentalControl.ParentalControl import ParentalTracking
from PostureRecognize.ElapsedTime import seconds_to_hms
from PostureRecognize.FrameProcess import temp_backup_restore
from PostureRecognize.Model import TrainModel
from PostureRecognize.PositionDetect import PostureRecognizerThread, read_elapsed_time_data, StartPreview, \
    CalibrateThread
from .Authorize import PINDialog
from .Authorize_2 import PINDialog2
from .OverlayWindow import OverlayWidget
from .ui_MainMenu import Ui_MainWindow
from .minWindow import MinWindow
from pystray import Menu, Icon, MenuItem
from PIL.Image import open
import Window.resource_rc

top_side_menu = "background: #7346ad;border-top-left-radius: 25px;border-top-right-radius: 25px;"
btm_side_menu = "background: #7346ad;border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;"
choice_side_menu = "background: #7346ad;"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # Window Attribute
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.center()  # Window draggable

        # SET DEFAULT STATE
        # Connect window object
        self.min_btn.clicked.connect(self.min_window_visible)
        self.close_btn.clicked.connect(self.close)
        self.dashboard_btn_2.clicked.connect(self.dashboard_page)
        self.parental_btn_2.clicked.connect(self.parental_page)
        self.calibrate_btn_2.clicked.connect(self.calibration_page)
        self.settings_btn_2.clicked.connect(self.settings_page)
        self.parental_box.clicked.connect(self.update_parental_box)

        # Dashboard page
        self.popout_btn.clicked.connect(self.min_window)
        self.use_time_btn.clicked.connect(self.show_chart)
        self.use_time_btn.setText("Program Use Time")
        self.refresh_chart_btn.clicked.connect(lambda: self.show_chart(True))

        # for monitoring button
        self.icon_start = QIcon()
        self.icon_start.addFile(u":/icon/icons8-startup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_stop = QIcon()
        self.icon_stop.addFile(u":/icon/icons8-shutdown-48.png", QSize(), QIcon.Normal, QIcon.Off)

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
        self.usetime_table.cellClicked.connect(self.toggle_cell)
        self.web_btn.clicked.connect(lambda: QDesktopServices.openUrl("https://github.com/Soon156/AlignPosition/"))

        # Authenticate page
        self.PIN_line.setEchoMode(QLineEdit.Password)
        self.old_PIN_line.setEchoMode(QLineEdit.Password)
        self.new_PIN_line.setEchoMode(QLineEdit.Password)
        self.confirm_PIN_line.setEchoMode(QLineEdit.Password)
        self.PIN_btn.clicked.connect(self.valid_pin)
        self.confirm_PIN_line.returnPressed.connect(self.change_PIN_btn.click)
        self.new_PIN_line.returnPressed.connect(self.change_PIN_btn.click)
        self.old_PIN_line.returnPressed.connect(self.change_PIN_btn.click)
        self.PIN_line.returnPressed.connect(self.PIN_btn.click)

        # Parental page
        self.changePIN_btn.clicked.connect(self.change_pin_page)
        self.exct_data_btn.clicked.connect(self.extract_data)
        self.restore_btn.clicked.connect(self.restore_data)
        self.usetime_btn.clicked.connect(self.handle_submit)
        for day in range(7):  # Init table cell
            for hour in range(24):
                item = QTableWidgetItem(day, hour)
                item.setFlags(Qt.ItemIsEnabled)
                self.usetime_table.setItem(day, hour, item)

        self.dragPos = None  # Window Draggable
        self.start_time = 0  # Monitoring start time for break calculation
        self.monitoring_state = False  # is camera in use

        # monitoring thread object
        self.posture_recognizer = PostureRecognizerThread()
        self.posture_recognizer.error_msg.connect(self.error_handler)
        self.posture_recognizer.elapsed_time_updated.connect(self.update_elapsed_time_label)
        self.posture_recognizer.update_overlay.connect(self.update_overlay)
        self.posture_recognizer.finished.connect(self.change_monitoring_state)

        self.preview_thread = None  # Preview state
        self.calibrate_thread = None  # Hold calibrate thread
        self.is_capturing = False  # Indicate if calibrate is in progress
        self.temp = None  # Indicate temp restore/backup progress
        self.training_thread = None  # Hold different training thread
        self.login_state = False  # Hold login state

        self.dashboard_page()  # Set the default page
        self.tut_chart()  # Show default chart

        # Parental control related function init
        self.current_day = datetime.now().weekday()
        self.current_time = datetime.now().time()
        self.values = get_config()  # Stored config file
        self.parental_thread = None
        self.parental_control_thread = False
        self.latest_usetime = read_elapsed_time_data()  # Get track on total use time

        self.data = retrieve_table_data()  # Retrieve computer access time data
        if self.data and self.data[1]:  # Check is the tracking data exist and is it enabled
            self.parental_status = True
            self.start_parental_control_thread()
            # Check condition state
            if self.values['auto'] != "True":
                self.values['auto'] = "True"
                write_config(self.values)
                log.info("Auto start enabled by parental control")
        else:
            self.parental_status = False

        # System tray icon
        self.image = open(abs_logo_path)
        self.system_icon = Icon("AlignPosition", self.image, menu=Menu(
            MenuItem("Show", self.if_visible, default=True),
            MenuItem("Detection", self.start_monitoring),
            MenuItem("Exit", self.exit_app)
        ))
        self.system_icon.run_detached()

        # Init window
        self.w = None  # Small Window
        self.w1 = OverlayWidget()  # PopOut Window
        self.w1.setScreen(self.screen())
        self.w2 = PINDialog()

    def start_parental_control_thread(self):  # TODO
        self.parental_thread = ParentalTracking()
        self.parental_thread.cancel.connect(self.call_window2)
        self.parental_thread.setParent(self)
        self.parental_thread.start()
        self.parental_control_thread = True

    def call_window2(self):
        self.w2.show()

    def min_window_visible(self):  # Small window button handler
        try:
            if self.w.isVisible():
                self.hide()
        except AttributeError:
            self.showMinimized()

    def if_visible(self):  # Check main window visibility (tray icon)
        if self.isVisible():
            self.stop_preview()
            self.hide()
        else:
            self.show()

    # Page handler
    def dashboard_page(self):
        self.stop_preview()
        self.reset_stylesheet()
        self.a_2.setStyleSheet(top_side_menu)
        if os.path.exists(key_file_path):
            self.cont_stackedwidget.setCurrentIndex(0)
            self.use_time_lbl.setText(seconds_to_hms(read_elapsed_time_data()))
            self.tut_chart()
            self.use_time_btn.setText("Program Use Time")
            self.check_model()
        else:
            self.parental_page()

    def parental_page(self):
        self.stop_preview()
        self.reset_stylesheet()
        self.d_2.setStyleSheet(choice_side_menu)
        self.cont_stackedwidget.setCurrentIndex(4)
        if self.login_state:
            self.valid_pin(True)
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
        self.PIN_line.clear()

    def calibration_page(self):
        self.check_model()
        self.reset_stylesheet()
        self.b_2.setStyleSheet(choice_side_menu)
        self.hint_lbl.hide()
        self.cont_stackedwidget.setCurrentIndex(2)
        self.proceed_btn.hide()
        self.cancel_btn.hide()
        self.calibrate_camera_box_handler(int(get_config().get('camera')))

    def settings_page(self):
        self.stop_preview()
        self.reset_stylesheet()
        self.c_2.setStyleSheet(btm_side_menu)
        self.cont_stackedwidget.setCurrentIndex(3)
        self.init_setting_page()

    def min_window(self):
        self.w = MinWindow(self)  # Small Window
        self.w.show()
        self.popout_btn.setEnabled(False)

    def check_model(self):  # If model file exist
        try:
            self.monitor_btn.clicked.disconnect(self.calibration_page)
            self.monitor_btn.clicked.disconnect(self.start_monitoring)
        except:
            pass
        if os.path.exists(model_file):
            self.monitor_btn.setStyleSheet("")
            self.monitor_btn.clicked.connect(self.start_monitoring)
            if self.monitoring_state:
                self.monitor_btn.setIcon(self.icon_stop)
            else:
                self.monitor_btn.setIcon(self.icon_start)

            self.monitor_btn.setText("")
            self.popout_btn.setEnabled(True)
            self.recalibrate_btn.setText("Recalibrate")
            self.recalibrate_btn.show()
            self.append_btn.show()
        else:
            log.warning("Model file not found")
            icon = QIcon()
            icon.addFile(u":/", QSize(), QIcon.Normal, QIcon.Off)
            self.monitor_btn.setIcon(icon)
            self.monitor_btn.setStyleSheet("background-color: rgb(101, 224, 206);")
            self.monitor_btn.setText("Calibrate")
            self.recalibrate_btn.setText("Calibrate")
            self.popout_btn.setEnabled(False)
            self.append_btn.hide()
            self.recalibrate_btn.show()
            self.monitor_btn.clicked.connect(self.calibration_page)

    # Monitoring
    def change_monitoring_state(self, state):
        self.monitoring_state = state
        self.monitor_btn.setIcon(self.icon_start)
        self.w1.hide()
        try:
            self.w.start_btn.show()
            self.w.stop_btn.hide()
        except:
            pass
        log.info("Monitoring stop")

    def start_monitoring(self):
        self.stop_preview()
        if not self.monitoring_state:
            self.monitoring_state = True
            try:
                self.w.start_btn.hide()
                self.w.stop_btn.show()
            except:
                pass
            self.monitor_btn.setIcon(self.icon_stop)
            self.start_time = time.time()
            if self.values['overlay_enable'] == "True":
                self.w1.show()
            try:
                self.posture_recognizer.start()
            except Exception as e:
                log.error(e)
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
                self.exit_app()
            log.info("Monitoring start")
        else:
            self.posture_recognizer.stop_capture()

    @Slot(int)
    def update_elapsed_time_label(self, elapsed_time):
        self.use_time_lbl.setText(seconds_to_hms(elapsed_time))
        try:
            self.w.use_time_lbl.setText(seconds_to_hms(elapsed_time))
        except:
            pass

        self.latest_usetime = elapsed_time  # Update elapsed time in global

        # Show notify if hit break time
        a = time.time() - self.start_time
        b = float(self.values.get('rest')) * 60
        if a >= b:
            show_break()
            self.start_time = time.time()

    def update_overlay(self, posture):  # Change overlay window state
        self.w1.change_state(posture)

    # Parental Control

    def valid_pin(self, cond=False):
        if not cond:
            if login_user(self.PIN_line.text()):
                cond = True
                if self.PIN_checkbox.isChecked():
                    self.login_state = True
            else:
                self.PIN_hint_lbl.setText("Incorrect PIN")
                self.PIN_hint_lbl.show()
        else:
            cond = True
        if cond:
            use_time = 8
            data = retrieve_table_data()
            self.parental_box.setChecked(False)
            if data:
                if data[1]:
                    self.parental_box.setChecked(True)
                use_time = data[0]
                for day, hour in data[2:]:
                    table_item = self.usetime_table.item(day, hour)
                    table_item.setBackground(QColor(220, 20, 60))
            self.update_parental_box()
            self.usetime_box.setValue(use_time)
            self.cont_stackedwidget.setCurrentIndex(1)

    def update_parental_box(self):
        if self.parental_box.isChecked():
            self.parental_box.setText("Parental Control Activated")
        else:
            self.parental_box.setText("Parental Control Deactivated")

    def change_pin(self, cond=False):  # True: create new PIN for first time user
        old = self.old_PIN_line.text()
        new1 = self.new_PIN_line.text()
        new2 = self.confirm_PIN_line.text()
        if new1 != "" and new2 != "":
            if new1 == new2:
                if len(new1) >= 6 and new1.isdigit():
                    if cond:
                        user_register(self.new_PIN_line.text())
                        self.dashboard_page()
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

    def reset_stylesheet(self):
        self.a_2.setStyleSheet('')
        self.b_2.setStyleSheet('')
        self.c_2.setStyleSheet('')
        self.d_2.setStyleSheet('')

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
            self.hint_lbl.setText(Capture_Posture)
            self.calibrate_thread.setParent(self)
            self.calibrate_thread.finished.connect(self.calibrate_finished)
            self.calibrate_thread.error_msg.connect(self.error_handler)
            self.calibrate_thread.start()

    def calibrate_finished(self, mode):
        if mode != "good" and mode != "append":
            mode = "calibrate"

        if mode == "good":
            self.hint_lbl.setText(Bad_Posture)
            self.proceed_btn.setEnabled(True)
        else:
            self.hint_lbl.setText(Model_Training)
            self.start_train(mode)

    def error_handler(self, msg):
        if msg.startswith("Model accuracy too low:"):
            self.cancel_ops(cond=True)
        if "cap.read()" in msg:
            self.change_monitoring_state(False)
            msg = "Camera in use or not available, try change camera in settings"
        QMessageBox.warning(self, "Warning", f"An error occurred: {msg}")

    def start_train(self, mode):
        self.training_thread = TrainModel(mode)
        self.training_thread.error_msg.connect(self.error_handler)
        self.training_thread.finished.connect(self.train_finished)
        self.training_thread.start()
        self.calibrate_thread = None

    def train_finished(self, arg):
        self.recalibrate_btn.setText("Re-Calibrate")
        self.append_btn.show()
        if arg == "calibrate":
            log.info("Calibrate Success")
            self.hint_lbl.setText("Calibrate finish")
        elif arg == "append":
            log.info("Append Success")
            self.hint_lbl.setText("Append finish")
        self.check_model()
        self.proceed_btn.hide()
        self.proceed_btn.setEnabled(True)
        self.cancel_btn.hide()
        self.recalibrate_btn.show()
        self.is_capturing = False
        log.debug("GUI after train updated")

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

            if self.start_box.isChecked() and not self.data[1]:
                self.values['auto'] = "True"
                log.info(f"Startup Enable")
            elif not self.start_box.isChecked() and self.data[1]:
                self.start_box.setChecked(True)
                QMessageBox.warning(self, "Not allowed", "Auto start enabled by parental control")
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
            try:
                self.w1.win_geometry()
            except:
                pass

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
            name = None
            total_time = 0
            for date in data:
                use_timedate = 0
                if app in data[date]:
                    use_timedate = data[date][app] / 60
                    total_time += use_timedate
                temp.append(use_timedate)
                name = f"{app}: {round(total_time,2)} m"
            bar_set = QBarSet(name)
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

    def show_chart(self, state=False):
        try:
            self.posture_recognizer.save_usetime()
            tracking_instance.save_app_usetime()
        except Exception as e:
            log.warning(e)

        # Update UI
        if self.use_time_btn.text() == "Program Use Time":
            if not state:
                self.use_time_btn.setText("Total Use Time")
                self.put_chart()
            else:
                self.tut_chart()
        else:
            if not state:
                self.use_time_btn.setText("Program Use Time")
                self.tut_chart()
            else:
                self.put_chart()

    def update_chart(self, chart_view=None):
        chart_view.setMinimumSize(QSize(900, 300))
        while self.chart_cont.count() > 0:
            item = self.chart_cont.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.chart_cont.addWidget(chart_view)

    # Table view
    def handle_submit(self):
        value = self.usetime_box.value()
        if value > 24 or value < 1:
            QMessageBox.warning(self, "Not allowed", "Usetime cannot be larger than 24 or smaller than 1")
        else:
            selected_cells = [self.usetime_box.value(), self.parental_box.isChecked()]
            for day in range(7):
                for hour in range(24):
                    item = self.usetime_table.item(day, hour)
                    if item.background() == QColor(220, 20, 60):
                        selected_cells.append((day, hour))
            save_table_data(selected_cells)
            self.data = selected_cells
            if self.parental_box.isChecked():
                self.values['auto'] = "True"
                write_config(self.values)
                self.values = get_config()
                if self.parental_control_thread:
                    self.start_parental_control_thread()
                else:
                    self.parental_thread.update_table_data()
            else:
                self.parental_thread.stop_parental_thread()
                self.parental_control_thread = False

    def toggle_cell(self, row, column):
        item = self.usetime_table.item(row, column)
        if item.background() == QColor(220, 20, 60):
            item.setBackground(QColor(0, 0, 0, 0))
        else:
            item.setBackground(QColor(220, 20, 60))

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
        if self.data and self.data[1]:
            window = PINDialog2()
            window.finished.connect(self.exit_main)
            window.exec()
        else:
            self.exit_main()

    def exit_main(self):
        self.destroy()  # End Main Window
        try:
            self.parental_thread.stop_parental_thread()  # Stop parental time tracking
        except:
            pass
        tracking_instance.update_condition()  # Stop app use time tracking
        if self.monitoring_state:  # Stop monitoring
            self.monitoring_state = False
            self.posture_recognizer.stop_capture()
        self.system_icon.stop()  # Stop system tray
        # Close all dialog window
        windows = [self.w, self.w1, self.w2]
        for window in windows:
            try:
                window.close()
            except Exception as e:
                log.info(str(e))
        QApplication.exit()
        sys.exit()
