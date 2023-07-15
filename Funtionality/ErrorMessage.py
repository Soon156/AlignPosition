from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox

"""
Stadard button
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Yes
QMessageBox.No
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore

Icon
QMessageBox::NoIcon
QMessageBox::Question
QMessageBox::Information
QMessageBox::Warning
QMessageBox::Critical
"""


def button_clicked(button):
    if button.text() == "OK":
        print("OK button clicked")


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
            message_box.buttonClicked.connect(button_clicked)
        message_box.exec()
