import sys
from PySide6 import QtWidgets
from Funtionality.ErrorMessage import WarningMessageBox
from Funtionality.UpdateConfig import tracking_app_use_time
from Window.main import MainWindow
from Funtionality import Config

if __name__ == '__main__':
    values = Config.get_config()
    if not Config.check_process():
        # Create the application instance
        app = QtWidgets.QApplication(sys.argv)

        Config.get_config()
        Config.clear_log()

        if values['app_tracking'] == "True":
            tracking_app_use_time()

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
