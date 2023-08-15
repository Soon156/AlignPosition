from PySide6.QtWidgets import QDialog
import logging as log
from ParentalControl.Auth import login_user
from Window.ui_Authorize import Ui_PINDialog

condition = True


def change_condition():
    global condition
    condition = False


def get_condition():
    print(condition)
    return condition


class PINDialog2(QDialog, Ui_PINDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def valid_pin(self):
        if login_user(self.PIN_line.text()):
            self.close()
            change_condition()
            log.info("Cancel Sleeping")

        else:
            self.PIN_hint_lbl.setText("Incorrect PIN")
            self.PIN_hint_lbl.show()