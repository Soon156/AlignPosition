from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from UI.ui_Settings import Ui_quick_access_dialog
from .calibration import WebcamWidget
from Funtionality.Config import get_config, get_available_cameras, write_config, create_config
import logging as log

values = get_config()
available_cameras = get_available_cameras()


class QuickWindow(QDialog, Ui_quick_access_dialog):
    configReset = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = None
        self.setupUi(self)
        self.configReset.connect(self.get_conf)
        self.get_conf()

        # link button with handler
        self.calibrate_btn.clicked.connect(self.calibrate)
        self.reset_btn.clicked.connect(self.reset_conf)
        self.apply_btn.clicked.connect(self.set_conf)

    def set_conf(self):
        if self.background_box.isChecked():
            values['background'] = "True"
            log.info(f"Background Enable")
        else:
            values['background'] = "False"
            log.info(f"Background Disable")

        if self.notify_box.isChecked():
            values['notifications'] = "True"
            log.info(f"Notification Enable")
        else:
            values['notifications'] = "False"
            log.info(f"Notification Disable")

        if self.start_box.isChecked():
            values['auto'] = "True"
            log.info(f"Startup Enable")
        else:
            values['auto'] = "False"
            log.info(f"Startup Disable")

        value = self.reminder_box.value()
        if not value == values['rest']:
            values['rest'] = value
            log.info(f"New break time is {value} minutes")

        index = self.camera_box.currentIndex()
        if not index == values['camera']:
            values['camera'] = index
            log.info(f"Camera change to {self.camera_box.currentText()}")

        write_config(values)

    def get_conf(self):
        # Set value from config
        if values.get('notifications') == "True":
            self.notify_box.setChecked(True)
        else:
            self.notify_box.setChecked(False)

        if values.get('background') == "True":
            self.background_box.setChecked(True)
        else:
            self.background_box.setChecked(False)

        if values.get('auto') == "True":
            self.start_box.setChecked(True)
        else:
            self.start_box.setChecked(False)

        for index, device_name in available_cameras.items():
            self.camera_box.addItem(device_name, index)

        self.reminder_box.setValue(float(values.get('rest')))

    def reset_conf(self):
        create_config()
        global values
        values = get_config()
        self.get_conf()

    def calibrate(self):
        self.setEnabled(False)
        w = WebcamWidget(self)
        w.exec_()
        self.setEnabled(True)
