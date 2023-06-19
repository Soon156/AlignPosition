import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


class WebcamWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.camera = None
        self.is_previewing = False

        # Create the GUI elements
        self.image_label = QLabel(self)
        self.start_button = QPushButton("Start", self)
        self.end_button = QPushButton("End", self)

        # Connect the button signals to the corresponding slots
        self.start_button.clicked.connect(self.start_preview)
        self.end_button.clicked.connect(self.end_preview)

        # Create a layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.end_button)

        # Create a layout for the image label and buttons
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(button_layout)

        # Set the main layout for the widget
        self.setLayout(main_layout)

        # Create a timer to update the preview frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_preview)

    def start_preview(self):
        if not self.is_previewing:
            self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.is_previewing = True
            self.timer.start(30)  # Update every 30 milliseconds

    def end_preview(self):
        if self.is_previewing:
            self.is_previewing = False
            self.timer.stop()
            self.camera.release()

    def update_preview(self):
        ret, frame = self.camera.read()
        if ret:
            # Flip the frame horizontally
            frame = cv2.flip(frame, 1)

            # Convert the OpenCV frame to QImage
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

            # Convert the QImage to QPixmap for display
            pixmap = QPixmap.fromImage(q_image)

            # Set the pixmap on the image label
            self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.end_preview()
        super().closeEvent(event)


# Create the application instance
app = QApplication([])

# Create the main window
window = WebcamWidget()
window.setWindowTitle("Webcam Preview")
window.resize(800, 600)
window.show()

# Start the event loop
app.exec()
