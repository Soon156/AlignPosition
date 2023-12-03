import ctypes
import logging as log
import os
import sys
import time
from datetime import datetime
import zroya
from PySide6.QtCore import Slot, Qt, QSize
from PySide6.QtGui import QColor, QDesktopServices, QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, \
    QTableWidgetItem, QSystemTrayIcon, QMenu
from matplotlib import pyplot as plt
from Chart.BadTime import BadTimeChartWidget
from Chart.ProgramUseTime import ProgramUseTimeChartWidget
from Chart.UseTime import UseTimeChartWidget
from Funtionality.Config import get_config, get_available_cameras, create_config, \
    key_file_path, abs_logo_path, remove_all_data, check_key, reset_parental, GRAY_COLOR  # parental_monitoring
from Funtionality.Notification import first_notify, break_notify
from Funtionality.UpdateConfig import write_config, stop_tracking, waiting, \
    get_app_tracking_state, tracking_app_use_time, save_usetime
from Funtionality.Version import check_for_update
from Funtionality.WindowEvent import CheckEvent
from ParentalControl.Auth import change_password, login_user, user_register, save_table_data, read_table_data, msg
from ParentalControl.ParentalControl import ParentalTracking
from PostureRecognize.ElapsedTime import seconds_to_hms
from PostureRecognize.PositionDetect import PostureRecognizerThread, read_elapsed_time_data  # StartPreview
from UI_Window.ui_MainMenu import Ui_MainWindow
from UI_Window.ui_MainMenuDark import Ui_MainWindow as Ui_MainWindowDark
from .Authorize import PINDialog
from .Authorize_2 import PINDialog2
from .OverlayWindow import OverlayWidget
from .ParentalWindow import ParentalDialog
from .changeStyleSheet import get_theme, top_side_menu, top_side_menu_dark, choice_side_menu, choice_side_menu_dark, \
    btm_side_menu, btm_side_menu_dark
from .minWindow import MinWindow

dark_cell = QColor(113, 94, 117)
light_cell = QColor(155, 190, 200)
transparent_cell = QColor(0, 0, 0, 0)

if get_theme():
    ui_class = Ui_MainWindow
else:
    ui_class = Ui_MainWindowDark


class MainWindow(QMainWindow, ui_class):

    def __init__(self, background=False):
        super().__init__()
        # Window Attribute
        self.theme = get_theme()
        if self.theme:
            plt.rcParams['text.color'] = GRAY_COLOR
            plt.rcParams['axes.labelcolor'] = GRAY_COLOR
        else:
            plt.rcParams['text.color'] = 'white'
            plt.rcParams['axes.labelcolor'] = 'white'
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.center()  # Window draggable

        # SET DEFAULT STATE
        # Connect window object
        self.min_btn.clicked.connect(self.min_window_visible)
        self.close_btn.clicked.connect(self.close)
        self.dashboard_btn_2.clicked.connect(self.dashboard_page)
        self.parental_btn_2.clicked.connect(self.parental_page)
        self.settings_btn_2.clicked.connect(self.settings_page)
        self.parental_box.clicked.connect(self.update_parental_box)
        self.warning_msg = None
        self.UsernameFrame.hide()

        # Dashboard page
        self.popout_btn.clicked.connect(self.min_window)
        self.use_time_btn.clicked.connect(self.show_chart)
        self.use_time_btn.setText("Program Use Time")
        self.refresh_chart_btn.clicked.connect(lambda: self.show_chart(True))
        self.monitor_btn.clicked.connect(self.start_monitoring)

        # for monitoring button
        self.icon_start = QIcon()
        self.icon_start.addFile(u":/icon/icons8-startup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_stop = QIcon()
        self.icon_stop.addFile(u":/icon/icons8-shutdown-48.png", QSize(), QIcon.Normal, QIcon.Off)

        # Settings page
        self.init_setting_page()
        self.reset_btn.clicked.connect(self.reset_config)
        self.apply_btn.clicked.connect(self.update_setting)
        self.usetime_table.itemClicked.connect(self.toggle_cell)
        self.theme_box.toggled.connect(self.update_theme_box)
        self.web_btn.clicked.connect(lambda: QDesktopServices.openUrl("https://github.com/Soon156/AlignPosition/wiki"))
        self.remove_data_btn.clicked.connect(self.remove_data)

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
        self.usetime_btn.clicked.connect(self.handle_submit)
        self.parental_setting_btn.clicked.connect(self.call_parental_dialog)

        for day in range(7):  # Init table cell
            for hour in range(24):
                item = QTableWidgetItem(day, hour)
                item.setFlags(Qt.ItemIsEnabled)
                self.usetime_table.setItem(day, hour, item)

        self.dragPos = None  # Window Draggable
        self.start_time = 0  # Monitoring start time for break calculation
        self.monitoring_state = False  # is camera in use
        self.usetime_table.viewport().setMouseTracking(True)
        self.usetime_table.viewport().installEventFilter(self)

        # monitoring thread object
        self.posture_recognizer = PostureRecognizerThread()
        self.posture_recognizer.error_msg.connect(self.error_handler)
        self.posture_recognizer.elapsed_time_updated.connect(self.update_elapsed_time_label)
        self.posture_recognizer.update_overlay.connect(self.update_overlay)
        self.posture_recognizer.finished.connect(self.change_monitoring_state)

        self.login_state = False  # Hold login state

        self.dashboard_page()  # Set the default page
        self.init_chart('tut')  # Show default chart

        # Parental control related function init
        self.current_day = datetime.now().weekday()
        self.current_time = datetime.now().time()
        self.values = get_config()  # Stored config file
        self.parental_thread = None
        self.parental_control_thread = False
        self.latest_usetime = read_elapsed_time_data()  # Get track on total use time

        try:
            self.data = read_table_data()  # Retrieve computer access time data
        except Exception as e:
            self.error_handler(e)

        if self.data and self.data[1]:  # Check is the tracking data exist and is it enabled
            self.start_parental_control_thread()
            # Check condition state
            if self.values['auto'] != "True":
                self.values['auto'] = "True"
                write_config(self.values)
                log.info("Auto start enabled by parental control")

        # System tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(abs_logo_path))
        self.tray_icon.activated.connect(self.tray_action)

        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show)

        detection_action = QAction("Detection", self)
        detection_action.triggered.connect(self.start_monitoring)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.show_authorize_win)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(detection_action)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Init window
        self.w = MinWindow(self)  # Small Window
        self.w1 = OverlayWidget()  # PopOut Window
        self.w1.setScreen(self.screen())
        self.w2 = PINDialog()  # authorize window call by notification
        self.w3 = PINDialog2()  # authorize window call normal operation
        self.w3.finished.connect(self.exit_main)
        self.w3.reset.connect(self.reset_w3_control_state)
        self.w3_authorize_lock = False
        self.w4 = ParentalDialog(self)  # Parental Setting
        self.request = None

        try:
            data = read_table_data()
            values = get_config()
            if ((data and data[1]) or values.get('monitoring') == "True") and check_key():
                self.start_monitoring()
        except Exception as e:
            self.error_handler(e)

        # Check Update
        if not background:
            version = check_for_update()
            if version is not None:
                if self.values['check_update'] == "Yes":
                    self.update_msg(version)
                elif version > self.values['check_update']:
                    self.update_msg(version)

        # Event Handler
        self.event_checker = CheckEvent()
        self.event_checker.update_event.connect(self.event_handler)
        self.event_checker.start()
        self.control_thread = None

    def update_msg(self, version):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle('Align Position')
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setText(f"An update is available! Latest version: {version}")
        msgbox.addButton('Update', QMessageBox.YesRole)
        msgbox.addButton('Skip This Version', QMessageBox.ApplyRole)
        msgbox.addButton('Do Not Check Update', QMessageBox.NoRole)
        result = msgbox.exec()
        if result == 0:
            QDesktopServices.openUrl("https://github.com/Soon156/AlignPosition/releases/latest")
            self.values['check_update'] = "Yes"
        elif result == 1:
            self.values['check_update'] = version
        else:
            self.values['check_update'] = "No"
        write_config(self.values)

    def tray_action(self, react):
        if react == QSystemTrayIcon.DoubleClick or react == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def reset_w3_control_state(self):
        self.w3_authorize_lock = False
        self.request = None

    def start_parental_control_thread(self):
        # parental_monitoring(value=1)
        self.parental_thread = ParentalTracking()
        self.parental_thread.setParent(self)
        self.parental_thread.cancel.connect(self.call_window2)
        self.parental_thread.start()
        self.parental_control_thread = True

    def call_window2(self):
        self.w2.PIN_line.setText("")
        self.w2.PIN_hint_lbl.hide()
        self.w3.PIN_line.setFocus()
        self.w2.show()

    def min_window_visible(self):  # Small window button handler
        try:
            if self.w.isVisible():
                self.hide()
            else:
                self.showMinimized()
        except:
            self.showMinimized()

    def if_visible(self):  # Check main window visibility (tray icon)
        if self.isVisible():
            self.hide()
        else:
            self.show()

    # Page handler
    def dashboard_page(self):
        self.reset_stylesheet()
        if self.theme:
            self.a_2.setStyleSheet(top_side_menu)
        else:
            self.a_2.setStyleSheet(top_side_menu_dark)
        if os.path.exists(key_file_path):
            self.cont_stackedwidget.setCurrentIndex(0)
            elapsed_time, _ = read_elapsed_time_data()
            self.use_time_lbl.setText(seconds_to_hms(elapsed_time))
            self.init_chart('tut')
            self.use_time_btn.setText("Program Use Time")
        else:
            self.parental_page()

    def parental_page(self):
        self.reset_stylesheet()
        if self.theme:
            self.d_2.setStyleSheet(choice_side_menu)
        else:
            self.d_2.setStyleSheet(choice_side_menu_dark)
        self.cont_stackedwidget.setCurrentIndex(3)  # Authentic page
        if self.login_state:
            self.valid_pin(True)
        else:
            if os.path.exists(key_file_path):
                self.PIN_stackedwidget.setCurrentIndex(1)  # Parental page
                self.change_PIN_btn.clicked.connect(self.change_pin)
            else:
                self.OldPINFrame.hide()
                self.PIN_stackedwidget.setCurrentIndex(0)  # Go back to dashboard (new user & change psw)
                self.change_PIN_btn.clicked.connect(lambda: self.change_pin(True))
        self.change_PIN_hint_lbl.hide()
        self.PIN_hint_lbl.hide()
        self.PIN_line.clear()

    def settings_page(self):
        self.reset_stylesheet()
        if self.theme:
            self.c_2.setStyleSheet(btm_side_menu)
        else:
            self.c_2.setStyleSheet(btm_side_menu_dark)
        self.cont_stackedwidget.setCurrentIndex(2)  # Setting page
        self.init_setting_page()

    def min_window(self):  # Small Window
        self.w.init()
        self.popout_btn.setEnabled(False)
        self.hide()

    # Monitoring
    def change_monitoring_state(self, state):
        if not state:
            self.monitor_btn.setIcon(self.icon_start)
            self.w1.hide()
            try:
                self.w.update_btn_state()
            except:
                pass
            log.info("Monitoring stop")
        else:
            self.monitor_btn.setIcon(self.icon_stop)
            if self.values['overlay_enable'] == "True":
                self.w1.show()
            try:
                self.w.update_btn_state(True)
            except:
                pass
            self.posture_recognizer.start()
            log.info("Monitoring start")
        self.monitoring_state = state

    def start_monitoring(self):
        data = None

        try:
            data = read_table_data()
        except Exception as e:
            self.error_handler(e)

        if not self.monitoring_state:
            self.start_time = time.time()
            self.change_monitoring_state(True)
        else:
            if data and data[1]:
                if self.login_state:
                    self.posture_recognizer.stop_capture()
                else:
                    self.w3_authorize_lock = True
                    self.request = "stop_monitor"
                    self.show_authorize_win()
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
            zroya.show(break_notify)
            self.start_time = time.time()

    def update_overlay(self, posture):  # Change overlay window state
        self.w1.change_state(posture)

    # Parental Control
    def valid_pin(self, cond=False):
        if not cond:
            if login_user(self.PIN_line.text()):
                cond = True
                if self.PIN_checkbox.isChecked():
                    log.info("Login state set to True")
                    self.login_state = True
            else:
                self.PIN_hint_lbl.setText("Incorrect PIN")
                self.PIN_hint_lbl.show()

        if cond:
            log.info("Login Successful")
            self.reinit_parental_table()
            self.update_parental_box()
            self.cont_stackedwidget.setCurrentIndex(1)  # Parental page

    def update_parental_box(self):
        if self.parental_box.isChecked():
            self.parental_box.setText("Parental Control Activated")
        else:
            self.parental_box.setText("Parental Control Deactivated")

    def reinit_parental_table(self):
        box_list = [self.mon_box, self.tue_box, self.wed_box, self.thu_box, self.fri_box, self.sat_box, self.sun_box]
        hour_list = [0, 1, 2, 3, 4, 5, 6, 7, 23]
        self.parental_box.setChecked(False)
        try:
            data = read_table_data()
        except:
            data = None
        if data:
            if data[1]:
                self.parental_box.setChecked(True)

            for day, box_name in enumerate(box_list):
                box_name.setValue(data[0][day])

            for cell in data[2]:
                day = cell[0]
                hour = cell[1]
                table_item = self.usetime_table.item(day, hour)
                self.init_cell(table_item)

        else:
            for day in range(7):  # Re-init table cell
                for hour in range(24):
                    table_item = self.usetime_table.item(day, hour)
                    if hour in hour_list:
                        self.init_cell(table_item)
                    else:
                        table_item.setBackground(transparent_cell)
            for day, box_name in enumerate(box_list):
                box_name.setValue(8)

    def toggle_cell(self, item):
        if item.background() == transparent_cell:
            self.init_cell(item)
        else:
            item.setBackground(transparent_cell)

    def init_cell(self, item):
        if self.theme:
            item.setBackground(light_cell)
        else:
            item.setBackground(dark_cell)

    def change_pin(self, new_user=False):  # True: create new PIN for first time user
        old = self.old_PIN_line.text()
        new1 = self.new_PIN_line.text()
        new2 = self.confirm_PIN_line.text()
        if new1 != "" and new2 != "":
            if new1 == new2:
                if len(new1) >= 6 and new1.isdigit():
                    if new_user:
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

    def call_parental_dialog(self):
        self.w4.init_btn()
        self.w4.show()

    def reset_stylesheet(self):
        self.a_2.setStyleSheet('')
        self.c_2.setStyleSheet('')
        self.d_2.setStyleSheet('')

    def error_handler(self, e):
        if e is msg:  # ParentalControl.Auth.msg
            QMessageBox.critical(self, "Error", f"{e}, reset your parental control setting or restore "
                                                f"from a backup")
        if e is not None:
            QMessageBox.warning(self, "Warning", f"Something wrong: {e}")

    # Settings
    def init_setting_page(self):
        values = get_config()
        try:
            data = read_table_data()
        except Exception as e:
            data = None
            self.error_handler(e)

        # Set value from config
        if values.get('background') == "True":
            self.background_box.setChecked(True)
        else:
            self.background_box.setChecked(False)

        if values.get('auto') == "True":
            self.start_box.setChecked(True)
        else:
            if data is not None:
                if data[1]:
                    self.start_box.setChecked(True)
                    QMessageBox.information(self, "Parental Control", "Autostart enable by parental control")
            self.start_box.setChecked(False)

        if values.get('app_tracking') == "True":
            self.app_time_track_box.setChecked(True)
        else:
            self.app_time_track_box.setChecked(False)

        if get_theme():
            self.theme_box.setChecked(True)
            self.theme_box.setText("Light Theme")
        else:
            self.theme_box.setChecked(False)
            self.theme_box.setText("Dark Theme")

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

    def update_theme_box(self, state):
        if state:
            self.theme_box.setText("Light Theme")
        else:
            self.theme_box.setText("Dark Theme")

    def update_setting(self):
        message = None
        break_time = self.reminder_box.value()
        if break_time <= 1:
            message = ["warning", "Action not allowed", "Break time cannot smaller than 1 minute"]
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
                if self.data is not None:
                    if self.data[1]:
                        self.start_box.setChecked(True)
                        message = ["warning", "Action not allowed", "Auto start enabled by parental control"]
                    else:
                        self.values['auto'] = "False"
                        log.info(f"Startup Disable")
                else:
                    self.values['auto'] = "False"
                    log.info(f"Startup Disable")

            if self.app_time_track_box.isChecked() and check_key():
                self.values['app_tracking'] = "True"
                log.info(f"App Tracking Enable")
            else:
                if not check_key():
                    message = ["warning", "Action not allowed", "You must set your PIN first"]
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

            if self.theme_box.isChecked():
                if self.values['theme'] != "1":
                    message = "Theme"
                    self.values['theme'] = 1
            else:
                if self.values['theme'] == "1":
                    message = "Theme"
                    self.values['theme'] = 0
            write_config(self.values)
            self.init_setting_page()
            self.values = get_config()
            try:
                self.w1.win_geometry()
            except:
                pass

        if message is not None:
            if message != "Theme":
                QMessageBox.warning(self, message[1], message[2])
            else:
                QMessageBox.information(self, "Settings", "Setting is update, theme need to be restart to applied!")
        else:
            QMessageBox.information(self, "Settings", "Setting is applied!")

    def remove_data(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle('Warning')
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText(
            'This action will reset the whole program and all your data will be lost!\nBackup your data first before '
            'proceeding.\n\nDo you wish to continue?')
        msgbox.addButton('Yes', QMessageBox.YesRole)
        msgbox.addButton('No', QMessageBox.NoRole)
        result = msgbox.exec()

        if result == 0:
            self.w3_authorize_lock = True
            self.request = "remove_data"
            self.show_authorize_win()

    def reset_config(self):
        stop_tracking()
        create_config()
        self.init_setting_page()
        QMessageBox.information(self, "Settings", "Config has been reset")

    # Chart list
    def init_chart(self, chart):
        while self.chart_cont.count() > 0:
            item = self.chart_cont.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        if chart == 'tut':
            self.chart_cont.addWidget(UseTimeChartWidget(self.theme))
        elif chart == 'but':
            self.chart_cont.addWidget(BadTimeChartWidget(self.theme))
        else:
            self.chart_cont.addWidget(ProgramUseTimeChartWidget(self.theme))

    def show_chart(self, refresh=False):

        if self.monitoring_state:
            self.posture_recognizer.save_usetime()
        try:
            if get_app_tracking_state():
                save_usetime()
        except Exception as e:
            log.warning(str(e))
            pass

        # Update UI
        if self.use_time_btn.text() == "Program Use Time":
            if not refresh:
                self.use_time_btn.setText("Total Bad Posture")
                self.init_chart('put')
            else:
                self.init_chart('tut')
        elif self.use_time_btn.text() == "Total Use Time":
            if not refresh:
                self.use_time_btn.setText("Program Use Time")
                self.init_chart('tut')
            else:
                self.init_chart('but')
        else:
            if not refresh:
                self.use_time_btn.setText("Total Use Time")
                self.init_chart('but')
            else:
                self.init_chart('put')

    # Table view
    def handle_submit(self):
        box_list = [self.mon_box, self.tue_box, self.wed_box, self.thu_box, self.fri_box, self.sat_box, self.sun_box]
        time_limit_list = []
        state = True
        for day, box_name in enumerate(box_list):
            time_limit = box_name.value()
            if time_limit > 24 or time_limit < 1:
                QMessageBox.warning(self, "Not allowed", "Usetime cannot be larger than 24 or smaller than 1")
                state = False
                break
            else:
                time_limit_list.append(box_name.value())

        if state:
            selected_cells = []
            for days in range(7):
                for hour in range(24):
                    item = self.usetime_table.item(days, hour)
                    if item.background() == light_cell or item.background() == dark_cell:
                        selected_cells.append((days, hour))
            parental_data = [time_limit_list, self.parental_box.isChecked(), selected_cells]
            save_table_data(parental_data)
            self.data = read_table_data()
            if self.parental_box.isChecked():
                self.values['auto'] = "True"
                self.values['monitoring'] = "True"
                write_config(self.values)
                self.values = get_config()

                if not self.parental_control_thread:
                    self.start_parental_control_thread()
                else:
                    self.parental_thread.update_table_data()
            else:
                if self.parental_thread is not None:
                    self.parental_thread.stop_parental_thread()
                    while self.parental_control_thread:
                        pass
            QMessageBox.information(self, "Parental Control", "Setting is applied")

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Draggable handler
    def mousePressEvent(self, event):
        if event is not None:
            if event.button() == Qt.LeftButton:
                self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event is not None:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
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
            self.show_authorize_win()

    def show_authorize_win(self):
        if self.data and self.data[1]:
            self.w3.PIN_line.setText("")
            self.w3.PIN_hint_lbl.hide()
            self.w3.PIN_line.setFocus()
            self.w3.show()
        else:
            self.exit_main()

    def exit_main(self):
        if self.w3_authorize_lock:
            self.w3_authorize_lock = False
            if self.request == "remove_data":
                self.stop_waiting_all()
                try:
                    remove_all_data()
                    QMessageBox.information(self, "App Reset", "All data has been removed successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Failed to remove data", str(e))
                self.exit_main()
            elif self.request == "reset_parental_settings":
                try:
                    self.parental_thread.stop_parental_thread()
                except:
                    pass
                try:
                    reset_parental()
                    QMessageBox.information(self, "Parental reset", "All data has been reset successfully")
                    self.reinit_parental_table()
                    self.login_state = False
                except Exception as e:
                    QMessageBox.critical(self, "Failed to remove data", str(e))
            elif self.request == "stop_monitor":
                self.posture_recognizer.stop_capture()
        else:
            self.hide()
            self.stop_waiting_all()
            ctypes.windll.advapi32.InitiateSystemShutdownW(None, None, 0, True, True)
            self.event_checker.stop()

            # Close all dialog window
            windows = [self.w, self.w1, self.w2, self.w3, self.w4]
            for window in windows:
                try:
                    window.destroy()
                except Exception:
                    pass
            log.info("Application Exit...")
            self.destroy()  # End Main Window
            QApplication.exit()
            sys.exit()

    def event_handler(self, event):
        if event == "sleep":
            self.sleeping_state()
        elif event == "shutdown":
            self.sleeping_state(True)
        elif event == "return":
            self.return_from_sleep()
        else:
            log.info("Unhandled event: ", event)

    def sleeping_state(self, shutdown=False):
        if shutdown:
            ctypes.windll.advapi32.AbortSystemShutdownW(None)
            self.w3_authorize_lock = False
            self.exit_main()
        else:
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
            self.control_thread = [self.parental_control_thread, self.monitoring_state, get_app_tracking_state()]
            if self.monitoring_state:
                self.start_monitoring()
            self.stop_waiting_all()
            ctypes.windll.kernel32.SetThreadExecutionState(0x00000002)  # ES_CONTINUOUS

    def return_from_sleep(self):
        if self.control_thread[0]:
            self.start_parental_control_thread()
        if self.control_thread[1]:
            self.start_monitoring()
        if self.control_thread[2]:
            tracking_app_use_time()

    def stop_waiting_all(self):
        log.info("Stopping all active thread....")
        try:
            self.posture_recognizer.stop_capture()  # Stop posture detection
        except:
            pass
        try:
            self.parental_thread.stop_parental_thread()  # Stop parental time tracking
        except:
            pass
        try:
            stop_tracking()  # Stop app use time tracking
        except:
            pass

        try:
            while self.parental_thread.isRunning():
                pass
        except Exception:
            pass
        try:
            while self.posture_recognizer.isRunning():
                pass
        except Exception:
            pass
        try:
            waiting()
        except Exception:
            pass
        log.info("All thread stopped.")
