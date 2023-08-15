import os
from datetime import date

import cv2
import time
import logging as log
import joblib
import numpy as np
from PySide6.QtCore import Signal, QThread, QRunnable, QObject, QThreadPool
from PySide6.QtGui import QImage, QPixmap
from Funtionality.Config import get_config, Model_Training, Bad_Posture, Capture_Posture, temp_folder
from PostureRecognize.ElapsedTime import read_elapsed_time_data, save_elapsed_time_data
from PostureRecognize.Model import model_file
from PostureRecognize.FrameProcess import get_landmark, buffer_frames


class StartPreview(QThread):
    error_msg = Signal(str)

    def __init__(self, index):
        super().__init__()
        self.index = index
        self.condition = True

    def run(self):
        try:
            self.parent().camera = cv2.VideoCapture(self.index, cv2.CAP_DSHOW)
            while self.condition:

                ret, frame = self.parent().camera.read()
                if ret:
                    # Flip the frame horizontally
                    frame = cv2.flip(frame, 1)

                    # Resize the frame to fit the label
                    frame = cv2.resize(frame, (640, 360))

                    # Convert the OpenCV frame to QImage
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = frame.shape
                    bytes_per_line = ch * w
                    q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

                    # Convert the QImage to QPixmap for display
                    pixmap = QPixmap.fromImage(q_image)

                    # Set the pixmap on the image label
                    self.parent().calibrate_preview_lbl.setPixmap(pixmap)
                else:
                    raise Exception("Camera read failed")
        except Exception as e:
            log.error(e)
            self.error_msg.emit(str(e))

    def stop_preview(self):
        self.condition = False
        self.parent().camera.release()


class PostureRecognizerThread(QThread):
    elapsed_time_updated = Signal(int)
    error_msg = Signal(str)
    update_overlay = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.classifier = None
        self.old_time = read_elapsed_time_data()
        self.elapsed_time = 0
        self.new_time = self.old_time
        self.badCount = 0
        self.goodCount = 0
        self.date_today = date.today()

    def run(self):
        try:
            self.load_model()
            self.start_capture()
        except Exception as e:
            self.error_msg.emit(str(e))

    def load_model(self):
        try:
            self.classifier = joblib.load(model_file)
        except FileNotFoundError as e:
            log.error(e)

    def start_capture(self):
        self.running = True
        try:
            self.capture_landmarks()
        except Exception as e:
            self.error_msg.emit(str(e))

    def stop_capture(self):
        self.running = False

    def capture_landmarks(self):
        # Create a VideoCapture object to capture video from the camera
        values = get_config()
        cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)
        start_time = time.time()
        idle_time = 0
        temp_time = 0
        total_time = 0
        counter = False
        while self.running:
            # Read the video frames
            ret, frame = cap.read()

            frame = cv2.flip(frame, 1)
            if not ret:
                log.error("Invalid video source, cap.read() failed")
                raise Exception("cap.read() failed")

            # Get landmark of frame
            frame, landmark = get_landmark(frame)
            if landmark is not None:
                # Do further processing with the pose landmarks
                labels = self.detect_posture(landmark)

                # Update the elapsed time only if landmark is not None
                self.elapsed_time = int(time.time() - start_time)
                if counter:
                    total_time += temp_time
                self.new_time = self.old_time + self.elapsed_time - total_time
                self.elapsed_time_updated.emit(self.new_time)
                counter = False

                # Display the labels on the frame
                label_text = f"Posture: {labels}"
                cv2.putText(frame, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            else:
                if not counter:
                    idle_time = time.time()
                    counter = True
                else:
                    pass_time = int(time.time() - idle_time)
                    # Check if the counter should be updated
                    if pass_time >= float(values.get('idle')) * 60:
                        temp_time = pass_time

            if values.get('dev') == "True":
                # Display the frame with pose landmarks and labels
                cv2.imshow("Pose Landmarks", frame)

            if date.today() != self.date_today:
                save_elapsed_time_data(self.new_time, self.date_today)
                self.new_time = 0
                self.old_time = self.new_time

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        save_elapsed_time_data(self.new_time, self.date_today)
        self.old_time = self.new_time
        # Release the VideoCapture and close the OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    def detect_posture(self, landmark, threshold=65):
        # Use the loaded model for predictions or other tasks
        predictions = self.classifier.predict(landmark)

        good_posture_count = np.count_nonzero(predictions == 0)
        total_count = len(predictions)
        percentage = (good_posture_count / total_count) * 100

        result = "Detecting..."
        # Determine the majority and print the result
        if percentage >= threshold:
            self.goodCount += 1
            if self.goodCount >= 10:
                result = "good"
                self.update_overlay.emit(result)
                self.badCount = 0
        else:
            self.badCount += 1
            if self.badCount >= 10:
                result = "bad"
                self.update_overlay.emit(result)
                self.goodCount = 0
        return result


class WorkerSignals(QObject):
    counter = Signal()


class CalibrateThread(QThread):  # TODO still need debug memory
    finished = Signal(str)
    error_msg = Signal(str)

    def __init__(self, cat):
        super().__init__()
        self.cat = cat
        self.new_frame_count = 0
        self.thread_pool = QThreadPool()

    def run(self):
        if self.cat == "append":
            counter = 1
            while True:
                folder = os.path.join(temp_folder, f"append_{counter}")
                if not os.path.exists(folder):
                    os.makedirs(folder, exist_ok=True)
                    break
                counter += 1
        else:
            folder = os.path.join(temp_folder, self.cat)
            # Make sure folder exists
            os.makedirs(folder, exist_ok=True)

        try:
            # Iterate over the files in the folder
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                os.remove(file_path)
            log.info("Temp folder cleared")

            # Create a shared counter
            files = os.listdir(folder)
            frame_count = len(files) + 1

            try:
                frames = buffer_frames(self.parent().camera)
                self.parent().hint_lbl.setText("Relax yourself, processing data....")

                log.debug("start pool")
                for frame in frames:
                    worker = ExtractLandmark(frame, folder, frame_count)
                    worker.signals.counter.connect(self.counter_handler)
                    frame_count += 1
                    self.thread_pool.start(worker)
                self.thread_pool.waitForDone()
                log.debug("finish thread pool")
                self.finished.emit(self.cat)
                log.debug(self.new_frame_count)
                if self.new_frame_count < 10:
                    log.warning(f"Available frame count low.\nFrame_count: {self.new_frame_count}")
                    self.error_msg.emit("Make sure your face can be clearly see in the preview window")
                    self.new_frame_count = 0
                log.info("Frames extraction completed")

            except Exception as e:
                self.error_msg.emit(str(e))
                log.critical(e)
                raise Exception

        except PermissionError as e:
            log.warning(e)
            self.error_msg.emit(str(e))

    def counter_handler(self):
        self.new_frame_count += 1


class ExtractLandmark(QRunnable):
    def __init__(self, frame, folder, frame_count):
        super().__init__()
        self.frame = frame
        self.folder = folder
        self.signals = WorkerSignals()
        self.frame_count = frame_count

    def run(self):
        threshold = 50
        # Make exception for black image
        mean_intensity = self.frame.mean()
        if (255 - threshold) > mean_intensity > threshold:
            frame, frame_landmark = get_landmark(self.frame)
            if frame_landmark is not None:
                frame_path = os.path.join(self.folder, f"frame_{self.frame_count}.npy")
                np.save(frame_path, frame_landmark)
                self.signals.counter.emit()
