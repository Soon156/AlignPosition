from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from Window.Main import MainWindow
from Funtionality import Config
from Window.variable import ICON_PATH

# TODO Error Handler
Config.check_process()
Config.check_condition()

# Create the application instance
app = QApplication([])
app.setWindowIcon(QIcon(ICON_PATH))


# Create the main window
window = MainWindow()
window.show()

# Start the event loop
app.exec()
