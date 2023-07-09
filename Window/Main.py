from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow
from .variable import TITLE, ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.resize(800, 600)

        self.counter = 0

        # Create the widgets
        self.label = QLabel("Counter: 0")
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.increment_counter)

        # Create a layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def increment_counter(self):
        self.counter += 1
        self.label.setText(f"Counter: {self.counter}")
