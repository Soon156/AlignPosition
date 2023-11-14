from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QLineEdit
from ParentalControl.Auth import login_user
from Window.changeStyleSheet import get_theme
from Ui_Window.ui_Authorize import Ui_PINDialog
from Ui_Window.ui_AuthorizeDark import Ui_PINDialog as Ui_PINDialogDark

if get_theme():
    ui_class = Ui_PINDialog
else:
    ui_class = Ui_PINDialogDark


class PINDialog2(QDialog, ui_class):
    finished = Signal()
    reset = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PIN_line.returnPressed.connect(self.PIN_btn.click)
        self.PIN_line.setEchoMode(QLineEdit.Password)
        self.PIN_hint_lbl.hide()
        self.PIN_btn.clicked.connect(self.valid_pin)

    def valid_pin(self):
        if login_user(self.PIN_line.text()):
            self.hide()
            self.finished.emit()
        else:
            self.PIN_hint_lbl.setText("Incorrect PIN")
            self.PIN_hint_lbl.show()

    def closeEvent(self, event):
        event.ignore()
        self.reset.emit()
        self.hide()
