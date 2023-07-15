from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from UI.ui_quickAccess import Ui_Dialog
from .calibration import WebcamWidget
from Funtionality.Config import get_config, get_available_cameras, write_config, create_config
import logging as log

values = get_config()
available_cameras = get_available_cameras()


def update_camera(index, device_name):
    values['camera'] = index
    write_config(values)
    log.info(f"Camera change to {device_name}")


def notify_change(checked):
    if checked:
        values['notifications'] = True
        log.info(f"Notification Enable")
        write_config(values)
    else:
        values['notifications'] = False
        log.info(f"Notification Disable")
        write_config(values)


def background_change(checked):
    if checked:
        values['background'] = True
        log.info(f"Background Enable")
        write_config(values)
    else:
        values['background'] = False
        log.info(f"Background Disable")
        write_config(values)


def reminder_change(value):
    values['rest'] = value
    write_config(values)
    log.info(f"New break time is {value} minutes")


def idle_change(value):
    values['idle'] = value
    write_config(values)
    log.info(f"New idle time is {value} minutes")


class QuickWindow(QDialog, Ui_Dialog):
    configReset = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = None
        self.setupUi(self)
        self.configReset.connect(self.update_config)
        self.update_config()

        # link handler with object
        self.calibrate_btn.clicked.connect(self.calibrate)
        self.notify_box.stateChanged.connect(notify_change)
        self.background_box.stateChanged.connect(background_change)
        self.reminder_box.textChanged.connect(reminder_change)
        self.idle_box.textChanged.connect(idle_change)
        self.reset_btn.clicked.connect(self.reset_conf)
        self.camera_box.currentTextChanged.connect(lambda text: update_camera(self.camera_box.currentData(), text))

    def update_config(self):
        # Set value from config
        if values.get('notifications') == "True":
            self.notify_box.setChecked(True)
        else:
            self.notify_box.setChecked(False)
        if values.get('background') == "True":
            self.background_box.setChecked(True)
        else:
            self.background_box.setChecked(False)
        for index, device_name in available_cameras.items():
            self.camera_box.addItem(device_name, index)

        self.idle_box.setValue(float(values.get('idle')))
        self.reminder_box.setValue(float(values.get('rest')))

    def reset_conf(self):
        create_config()
        global values
        values = get_config()
        self.update_config()

    def calibrate(self):
        self.setEnabled(False)
        w = WebcamWidget(self)
        w.exec_()
        self.setEnabled(True)
