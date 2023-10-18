from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from PostureRecognize.ElapsedTime import read_elapsed_time_data, seconds_to_hms
from .ui_MinWindow import Ui_minDialog
from PySide6.QtCore import Qt


class MinWindow(QDialog, Ui_minDialog):
    signal_bool = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.center()
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        old_time, _ = read_elapsed_time_data()
        self.use_time_lbl.setText(seconds_to_hms(old_time))
        self.start_btn.clicked.connect(self.start_monitor)
        self.stop_btn.clicked.connect(self.stop_monitor)
        if self.parent.monitoring_state:
            self.start_btn.hide()
        else:
            self.stop_btn.hide()
        self.close_btn.clicked.connect(self.close_me)

    def close_me(self):
        self.parent.popout_btn.setEnabled(True)
        self.hide()
        if not self.parent.isVisible():
            self.parent.show()

    def start_monitor(self):
        self.start_btn.hide()
        self.stop_btn.show()
        self.parent.start_monitoring()

    def stop_monitor(self):
        self.start_btn.show()
        self.stop_btn.hide()
        self.parent.start_monitoring()

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
