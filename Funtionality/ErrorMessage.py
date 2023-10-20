import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox, QApplication


class WarningMessageBox(QtWidgets.QMainWindow):
    def __init__(self, title, hint, error, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(hint)
        if error == "Application Running":
            message_box.setIcon(QMessageBox.Warning)
            message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()
        self.destroy()
        QApplication.exit()
        sys.exit()
