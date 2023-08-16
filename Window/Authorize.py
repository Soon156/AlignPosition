import sys
import threading
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog
from Funtionality.Config import get_config, clear_log
from Funtionality.UpdateConfig import use_time
from ParentalControl.Auth import login_user
from Window.main import MainWindow
from Window.ui_Authorize import Ui_PINDialog


class PINDialog(QDialog, Ui_PINDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def valid_pin(self):
        if login_user(self.PIN_line.text()):
            self.close()
            # Create the application instance
            app = QtWidgets.QApplication(sys.argv)

            get_config()
            clear_log()

            values = get_config()
            if values['app_tracking'] == "True":
                use_time.start()

            # Create the main window
            window = MainWindow()
            window.setScreen(app.primaryScreen())
            window.notify_state = True
            window.show()

            # Start the event loop
            app.exec()

        else:
            self.PIN_hint_lbl.setText("Incorrect PIN")
            self.PIN_hint_lbl.show()
