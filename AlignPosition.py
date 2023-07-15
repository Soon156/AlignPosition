import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox

from Window.main import MainWindow
from Funtionality import Config
import logging as log

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
        # Create the application instance
        app = QtWidgets.QApplication(sys.argv)

        # Create a dummy main window as the parent for the message box
        dummy_main_window = QtWidgets.QMainWindow()
        dummy_main_window.setWindowFlags(dummy_main_window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # Show a warning message box
        message_box = QMessageBox(dummy_main_window)
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Warning")
        message_box.setText("The 'Align Position' process is already running.")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()