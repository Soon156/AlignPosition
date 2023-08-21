from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QLineEdit
from ParentalControl.Auth import login_user
from Window.ui_Authorize import Ui_PINDialog


class PINDialog2(QDialog, Ui_PINDialog):
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.PIN_line.returnPressed.connect(self.PIN_btn.click)
        self.PIN_line.setEchoMode(QLineEdit.Password)
        self.PIN_hint_lbl.hide()
        self.PIN_btn.clicked.connect(self.valid_pin)

    def valid_pin(self):
        if login_user(self.PIN_line.text()):
            self.close()
            self.finished.emit()
        else:
            self.PIN_hint_lbl.setText("Incorrect PIN")
            self.PIN_hint_lbl.show()
