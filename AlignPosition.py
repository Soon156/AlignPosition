import sys
import threading
from PySide6 import QtWidgets
from Funtionality.ErrorMessage import WarningMessageBox
from ParentalControl.AppUseTime import tracking
from Window.main import MainWindow
from Funtionality import Config

if __name__ == '__main__':

    if not Config.check_process():
        Config.get_config()
        Config.clear_log()

        # Create the application instance
        app = QtWidgets.QApplication(sys.argv)

        values = Config.get_config()
        if values['app_tracking'] == "True":
            use_time = threading.Thread(target=tracking)
            use_time.start()

        # Create the main window
        window = MainWindow()
        window.setScreen(app.primaryScreen())
        window.show()

        # Start the event loop
        app.exec()
    else:
        app = QtWidgets.QApplication(sys.argv)
        title = "Warning"
        hint = "The 'Align Position' process is already running."
        error = "Application Running"
        widget = WarningMessageBox(title, hint, error)
