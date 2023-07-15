import os
import threading
import time

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QApplication
from Funtionality.Config import model_file, get_config, write_config, logo_path
from Notification import first_time, notice_user
from PostureRecognize.PositionDetect import PostureRecognizer, read_elapsed_time_data
from PostureRecognize.FrameProcess import LandmarkExtractor
from UI.ui_main import Ui_MainMenu
from .calibration import WebcamWidget
from .quickAccess import QuickWindow
from pystray import Menu, Icon, MenuItem
from PIL.Image import open

# App logo
image = open(logo_path)


class MainWindow(QWidget, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.system_icon = None
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
            MenuItem("Calibrate", self.calibrate),
            MenuItem("Exit", self.exit_app)
        ))
        thread = threading.Thread(target=self.show_window)
        thread.start()
        if os.path.exists(model_file):
            self.start_btn.clicked.connect(self.start_monitoring)
        else:
            self.le = LandmarkExtractor()
            self.start_btn.setText("Calibrate")
            self.start_btn.clicked.connect(self.calibrate)
        self.posture_recognizer.elapsed_time_updated.connect(self.update_elapsed_time_label)

    def show_window(self):
        self.system_icon.run()

    def start_monitoring(self):
        if os.path.exists(model_file):
            if self.monitoring_state:
                self.monitoring_state = False
                self.start_btn.setText("Start Monitoring")
                self.posture_recognizer.stop_capture()

            else:
                self.monitoring_state = True
                self.start_btn.setText("Stop Monitoring")
                posture_thread = threading.Thread(target=self.run_posture_recognizer)
                self.start_time = time.time()
                posture_thread.start()
        else:
            self.calibrate()

    def run_posture_recognizer(self):
        self.posture_recognizer.load_model()
        self.posture_recognizer.start_capture()

    def quick_access(self):
        self.setEnabled(False)
        w = QuickWindow(self)
        w.exec_()
        self.setEnabled(True)

    def calibrate(self):
        self.setEnabled(False)
        w = WebcamWidget(self)
        w.exec_()
        if os.path.exists(model_file):
            self.start_btn.clicked.disconnect(self.calibrate)
            self.start_btn.clicked.connect(self.start_monitoring)
            self.start_btn.setText("Start Monitoring")
        self.setEnabled(True)

    @Slot(int)
    def update_elapsed_time_label(self, elapsed_time):
        var = get_config()
        self.usetime_lbl.setText(f"Today Use Time (s): {elapsed_time}")
        if time.time() - self.start_time >= float(var.get('rest')) * 60:
            thread = threading.Thread(target=notice_user)
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
                first_time()
            self.hide()
        else:
            self.exit_app()

    def exit_app(self):
        if self.monitoring_state:
            self.monitoring_state = False
            self.posture_recognizer.stop_capture()
        try:
            self.system_icon.stop()
        except AttributeError:
            pass
        QApplication.quit()
