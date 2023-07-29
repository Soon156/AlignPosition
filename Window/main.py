import os
import threading
import time
import logging as log

import zroya
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QApplication
from Funtionality.Config import model_file, get_config, write_config, logo_path
from Funtionality.Notification import first_notify, show_break, set_elapsed_time
from ParentalControl.AppUseTime import update_condition
from PostureRecognize.PositionDetect import PostureRecognizer, read_elapsed_time_data
from PostureRecognize.FrameProcess import LandmarkExtractor
from UI.ui_main import Ui_MainMenu
from .calibration import WebcamWidget
from .quickAccess import QuickWindow
from .parentalControl import ParentalWindow
from pystray import Menu, Icon, MenuItem
from PIL.Image import open

# App logo
image = open(logo_path)  # TODO check if exist, and log


class MainWindow(QWidget, Ui_MainMenu):  # TODO disable quick access when monitoring in progress
    def __init__(self):
        super().__init__()
        self.w = None
        self.start_time = 0
        self.monitoring_state = False
        self.setupUi(self)
        self.quick_btn.clicked.connect(self.quick_access)
        self.usetime_lbl.setText(f"Today Use Time (s): {read_elapsed_time_data()}")
        self.msg_label.setText("Good Morning MFK")  # TODO add hint here
        self.posture_recognizer = PostureRecognizer()
        self.system_icon = Icon("AlignPosition", image, menu=Menu(
            MenuItem("Show", lambda: self.show(), default=True),
            MenuItem("Detection", self.start_monitoring),
            MenuItem("Exit", self.exit_app)
        ))
        self.system_icon.run_detached()
        if os.path.exists(model_file):
            self.start_btn.clicked.connect(self.start_monitoring)
        else:
            log.warning("Model file not found")  # TODO check is this repeated
            self.le = LandmarkExtractor()
            self.start_btn.setText("Calibrate")
            self.start_btn.clicked.connect(self.calibrate)

        self.parental_btn.clicked.connect(self.parental_control)
        self.posture_recognizer.elapsed_time_updated.connect(self.update_elapsed_time_label)

    def start_monitoring(self):
        if os.path.exists(model_file):
            if self.monitoring_state:
                self.monitoring_state = False
                self.start_btn.setText("Start Monitoring")
                self.posture_recognizer.stop_capture()
                log.info("Monitoring stop")

            else:
                self.monitoring_state = True
                self.start_btn.setText("Stop Monitoring")
                posture_thread = threading.Thread(target=self.run_posture_recognizer)
                self.start_time = time.time()
                posture_thread.start()
                log.info("Monitoring start")
        else:
            self.show()

    def run_posture_recognizer(self):
        self.posture_recognizer.load_model()  # TODO Error Handler
        self.posture_recognizer.start_capture()  # TODO Error Handler

    def quick_access(self):
        self.setEnabled(False)
        w = QuickWindow(self)
        w.exec_()
        self.setEnabled(True)

    def parental_control(self):
        self.setEnabled(False)
        w = ParentalWindow(self)
        w.exec_()
        self.setEnabled(True)

    def calibrate(self):
        self.setEnabled(False)
        w = WebcamWidget(self)
        w.exec_()
        if os.path.exists(model_file):
            try:
                self.start_btn.clicked.disconnect(self.calibrate)
            except RuntimeError:
                pass
            self.start_btn.clicked.connect(self.start_monitoring)
            self.start_btn.setText("Start Monitoring")
        self.setEnabled(True)

    @Slot(int)
    def update_elapsed_time_label(self, elapsed_time):
        var = get_config()
        self.usetime_lbl.setText(f"Today Use Time (s): {elapsed_time}")
        set_elapsed_time(elapsed_time)
        a = time.time() - self.start_time
        b = float(var.get('rest')) * 60
        if a >= b:
            thread = threading.Thread(target=show_break)
            thread.start()
            self.start_time = time.time()

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

        QApplication.exit()
