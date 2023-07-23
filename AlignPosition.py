import sys
import logging as log
from PySide6 import QtWidgets

from Funtionality.ErrorMessage import WarningMessageBox
from Window.main import MainWindow
from Funtionality import Config

if __name__ == '__main__':

    if not Config.check_process():
        try:
            Config.check_condition()
        except Exception as e:
            log.warning(e)
        Config.clear_log()

        # Create the application instance
        app = QtWidgets.QApplication(sys.argv)

        # Create the main window
        window = MainWindow()
        window.show()

        # Start the event loop
        app.exec()
    else:
        app = QtWidgets.QApplication(sys.argv)
        title = "Warning"
        hint = "The 'Align Position' process is already running."
        error = "Application Running"
        widget = WarningMessageBox(title, hint, error)
