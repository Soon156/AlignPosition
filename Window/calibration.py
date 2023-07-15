import os
import threading
import cv2
import logging as log
from PySide6.QtCore import QTimer, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QDialog
from PostureRecognize.FrameProcess import LandmarkExtractor, temp_backup_restore
from UI.ui_calibrate import Ui_calibrate_win
from PostureRecognize.Model import train_model
from Funtionality.Config import get_config, model_file

values = get_config()
Good_Posture = "Maintain your good posture 5 seconds\n clicked proceed to Start"
Bad_Posture = "Maintain your bad posture 5 seconds\n clicked proceed to Start"
Append_Posture = "Append bad posture\n clicked proceed to Start"
Cancel_Calibrate = "Calibration Cancel"
Model_Training = "Training model, please wait patiently...."
Capture_Posture = "Capturing posture, stay still...."
Cancel = "Cancelling..."


class CalibrateThread(QThread):
    finished = Signal(str)  # Signal emitted when the task is finished

    def __init__(self, parent, cat, cond):
        super().__init__()
        self.cat = cat
        self.cond = cond
        self.parent = parent

    def run(self):
        self.parent.hint_lbl.setText(Capture_Posture)
        le = LandmarkExtractor()
        le.extract_landmarks_and_buffer_frames(self.parent, self.cat, self.cond)

        if self.cat == "good":
            self.finished.emit("good")
        elif self.cond:
            self.finished.emit("append")
        else:
            self.finished.emit("calibrate")


class WebcamWidget(QDialog, Ui_calibrate_win):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.calibrate_thread = None
        self.training_thread = None
        self.setupUi(self)
        self.le = LandmarkExtractor()

        # Connect the button signals to the corresponding slots
        self.calibrate_btn.clicked.connect(self.start_calibrate)
        self.calibrate_btn_2.clicked.connect(self.start_calibrate)
        self.append_btn.clicked.connect(self.append_posture)
        self.proceed_btn.clicked.connect(self.capture)
        self.cancel_btn.clicked.connect(self.cancel)

        self.proceed_btn.setVisible(False)
        self.cancel_btn.setVisible(False)

        if not os.path.exists(model_file):
            self.append_btn.setVisible(False)
        else:
            self.calibrate_btn_2.setVisible(False)
        # Create a timer to update the preview frames
        self.camera = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)  # TODO error handler
        if not self.camera.isOpened():
            log.error("Failed to open camera")
            raise Exception("Failed to read camera source")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_preview)
        self.timer.start(30)

        self.is_capturing = False  # Flag to indicate if capturing is in progress

    def start_calibrate(self):
        self.calibrate(True)

    def append_posture(self):
        self.calibrate(False)

    def capture(self):
        if not self.is_capturing or self.hint_lbl.text() == Bad_Posture:
            self.is_capturing = True
            self.proceed_btn.setEnabled(False)
            if self.hint_lbl.text() == Good_Posture:
                self.calibrate_thread = CalibrateThread(self, "good", False)
            elif self.hint_lbl.text() == Bad_Posture:
                self.calibrate_thread = CalibrateThread(self, "bad", False)
            elif self.hint_lbl.text() == Append_Posture:
                self.calibrate_thread = CalibrateThread(self, "bad", True)
            self.calibrate_thread.finished.connect(self.calibrate_finished)
            self.calibrate_thread.start()

    def calibrate(self, cond):
        log.info("Calibration start")
        temp_backup_restore(False)
        self.proceed_btn.setVisible(True)
        self.cancel_btn.setVisible(True)
        self.calibrate_btn.setVisible(False)
        self.calibrate_btn_2.setVisible(False)
        self.append_btn.setVisible(False)
        if cond:
            self.hint_lbl.setText(Good_Posture)
        else:
            self.hint_lbl.setText(Append_Posture)

    def cancel(self):
        log.info(Cancel_Calibrate)
        if self.calibrate_thread is not None and self.calibrate_thread.isRunning():
            self.calibrate_thread.finished.disconnect(self.calibrate_finished)
            self.calibrate_thread.stop()  # Terminate the running thread
            self.calibrate_thread.wait()  # Wait for the thread to finish
        if self.training_thread is not None and self.training_thread.isRunning():
            self.training_thread.stop()  # Terminate the running thread
            self.training_thread.join()  # Wait for the thread to finish
        temp_backup_restore(True)
        self.proceed_btn.setVisible(False)
        self.cancel_btn.setVisible(False)
        self.calibrate_btn.setVisible(True)
        if os.path.exists(model_file):
            self.append_btn.setVisible(True)
        else:
            self.calibrate_btn_2.setVisible(True)
        self.hint_lbl.setText(Cancel_Calibrate)
        self.is_capturing = False

    def calibrate_finished(self, mode):
        if mode == "good":
            self.hint_lbl.setText(Bad_Posture)
            self.proceed_btn.setEnabled(True)
        else:
            self.hint_lbl.setText(Model_Training)
            self.training_thread = threading.Thread(target=self.train_model_and_update_label, args=(mode,))
            self.training_thread.start()

    def train_model_and_update_label(self, arg1):
        train_model()
        self.proceed_btn.setVisible(False)
        self.cancel_btn.setVisible(False)
        self.calibrate_btn_2.setVisible(False)
        self.calibrate_btn.setVisible(True)
        self.append_btn.setVisible(True)
        if arg1 == "calibrate":
            log.info("Calibrate Success")
            self.hint_lbl.setText("Calibrate finish")
        elif arg1 == "append":
            log.info("Append Success")
            self.hint_lbl.setText("Append finish")
        self.is_capturing = False

    def update_preview(self):
        ret, frame = self.camera.read()
        if ret:
            # Flip the frame horizontally
            frame = cv2.flip(frame, 1)

            # Resize the frame to fit the label
            label_size = self.preview_lbl.size()
            frame = cv2.resize(frame, (label_size.width(), label_size.height()))

            # Convert the OpenCV frame to QImage
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

            # Convert the QImage to QPixmap for display
            pixmap = QPixmap.fromImage(q_image)

            # Set the pixmap on the image label
            self.preview_lbl.setPixmap(pixmap)

    def closeEvent(self, event):
        self.timer.stop()
        self.camera.release()
        super().closeEvent(event)
