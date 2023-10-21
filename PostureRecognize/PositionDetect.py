import os.path
from datetime import date, datetime
import tensorflow as tf
import cv2
import time
import numpy as np
import zroya
from PySide6.QtCore import Signal, QThread
from Funtionality.Config import get_config, abs_model_file_path, temp_folder
from Funtionality.Notification import posture_notify, brightness_notify
from ParentalControl.Auth import read_table_data
from PostureRecognize.ElapsedTime import read_elapsed_time_data, save_elapsed_time_data
from PostureRecognize.ExtractLandmark import extract_landmark
from PostureRecognize.Prediction import LandmarkResult
import logging as log


class PostureRecognizerThread(QThread):
    elapsed_time_updated = Signal(int)
    error_msg = Signal(str)
    update_overlay = Signal(str)
    finished = Signal(bool)

    def __init__(self):
        super().__init__()
        self.old_time = 0
        self.average = 0
        self.bad_time = 0
        self.new_time = 0
        self.model = None
        self.date_today = None
        self.values = None
        self.last_movement_time = None
        self.running = False
        self.last_posture = "good"

    def run(self):
        try:
            self.running = True
            self.old_time, self.bad_time = read_elapsed_time_data()
            self.new_time = self.old_time
            self.model = tf.keras.models.load_model(abs_model_file_path)
            self.date_today = date.today()
            self.average = 0
            self.values = get_config()

            detector = LandmarkResult()
            # Create a VideoCapture object to capture video from the camera
            cap = cv2.VideoCapture(int(self.values.get('camera')), cv2.CAP_DSHOW)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            start_time = time.time()

            # Control speed and calculate result
            frame_count = 0
            label = "detecting..."
            bad_control = False
            results = []

            # Control idle time
            idle_time = 0
            temp_time = 0
            counter = False

            # Threshold & controller for posture monitoring
            switch = False
            threshold = 30  # black image
            blank_counter = 0
            bad_threshold = float(self.values.get('bad_posture')) * 60
            last_frame = None
            major_change = 10000000
            diff_sum_record = []
            diff_count = 0
            brightness = False
            notify_time = 0
            bad_temp_time = 0
            bad_posture_time = 0

            data = False

            try:
                data = read_table_data()
            except:
                pass

            while self.running and not switch:

                if not cap.isOpened():
                    switch = True
                    log.warning("Camera not available")

                ret, frame = cap.read()

                if not ret and not switch:
                    switch = True
                    log.error("Error reading frame")

                if not switch:
                    frame_count += 1
                    if frame_count >= 25 and not counter:
                        frame_count = 0
                        if not len(results) == 0:
                            self.average = sum(results) / len(results)
                            predicted_labels = [0 if self.average < 0.6 else 1]
                            if predicted_labels[0] == 0:
                                label = "good"
                            else:
                                label = "bad"

                        results = []

                    elif frame_count % 5 == 0:
                        # Get landmark of frame
                        detector.detect_async(frame)
                        result = detector.result
                        try:
                            landmark = extract_landmark(result)
                            if landmark is not None:

                                mean_value = np.mean(frame)
                                if mean_value < threshold:
                                    if blank_counter >= 250 and not brightness:  # about 30 sec base on cpu power
                                        zroya.show(brightness_notify)
                                        notify_time = time.time()
                                        brightness = True
                                    elif time.time() - notify_time > 1800:
                                        brightness = False
                                    else:
                                        blank_counter += 1
                                else:
                                    blank_counter = 0

                                reshape_landmark = np.array(landmark).reshape(-1, 33 * 5)
                                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                                if last_frame is not None:
                                    frame_diff = cv2.absdiff(last_frame, gray)
                                    diff_sum = np.sum(frame_diff)
                                    if len(diff_sum_record) > 3:
                                        diff_sum_record.pop(0)
                                    diff_sum_record.append(diff_sum)

                                last_frame = gray
                                for value in diff_sum_record:
                                    if value > major_change:
                                        diff_count += 1

                                if diff_count < 3:
                                    predictions = self.model.predict(
                                        reshape_landmark, verbose=None)  # Make predictions using the trained model
                                    results.append(predictions[0, 0])
                                else:
                                    results = []
                                    label = "moving"
                                    self.average = 0

                                diff_count = 0

                                # Update the elapsed time
                                if counter:  # If there is idle
                                    start_time += temp_time
                                counter = False  # Reset idle flag

                                self.new_time = int(time.time() - start_time) + self.old_time
                                self.elapsed_time_updated.emit(self.new_time)

                            else:
                                label = "idle"
                                if not counter:  # If not idle before
                                    idle_time = time.time()
                                    counter = True

                                else:  # If idle
                                    pass_time = int(time.time() - idle_time)

                                    # Check if the counter should be updated
                                    if pass_time >= float(self.values.get('idle')) * 60:  # If idle time > threshold
                                        temp_time = pass_time  # set temp time
                                    else:
                                        temp_time = 0  # reset temp time to avoid minus if smaller then threshold
                        except Exception as e:
                            if str(e) not in ["cannot reshape array of size 1 into shape (165)",
                                              "type object 'PoseLandmarkerResult' has no attribute 'pose_landmarks'"]:
                                raise Exception(e)

                    if data is not None:
                        if not data[1]:
                            self.show_dev(frame, label)
                    else:
                        self.show_dev(frame, label)

                    if label == "bad":
                        if bad_control:
                            if bad_posture_time > 3:
                                self.bad_time += bad_posture_time
                            bad_temp_time = time.time()
                            bad_posture_time = 0
                            bad_control = False
                        else:
                            bad_posture_time = time.time() - bad_temp_time

                            if bad_posture_time > bad_threshold:
                                zroya.show(posture_notify)
                                bad_temp_time = time.time()
                    else:
                        bad_control = True

                    # Display the labels on the dev frame
                    self.update_overlay.emit(label)

                else:  # TODO active input thread
                    self.running = False
                    self.error_msg.emit("Camera reading failed, please make sure you are in bright environment, "
                                        "activity monitor trough keyboard/mouse WIP")
                    log.info("Switching to input detection, this will be implement in future....")

                if date.today() != self.date_today:  # Reset the time if pass 12am
                    self.save_usetime()
                    self.new_time = 0
                    self.bad_time = 0
                    self.old_time = self.new_time
                    self.date_today = date.today()
                    start_time = time.time()

                if time.time() - start_time > 600:  # CHECKME possible solution for crash after long time use
                    start_time = time.time()
                    self.save_usetime()
                    self.old_time = self.new_time
                    self.new_time = 0

            self.save_usetime()
            # Release the VideoCapture and close the OpenCV windows
            cap.release()
            detector.close()
            cv2.destroyAllWindows()
            self.finished.emit(self.running)
        except Exception as e:
            log.warning(e)
            self.error_msg.emit(str(e))
            self.stop_capture()
            self.finished.emit(self.running)

    def stop_capture(self):
        self.running = False

    def save_usetime(self):
        save_elapsed_time_data(self.new_time, self.date_today, self.bad_time)

    def show_dev(self, frame, label):
        if self.values.get('dev') == "True":
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (640, 360))
            label_text = f"Posture: {label}, {self.average}"
            cv2.putText(frame, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # Display the frame with pose landmarks and labels
            cv2.imshow("Pose Landmarks", frame)
            temp = cv2.waitKey(1) & 0xFF
            temp1 = 255

            if temp != 255:
                temp1 = temp

            if temp1 == ord('g'):
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                frame_filename = f'good_{timestamp}.jpg'
                file_path = os.path.join(temp_folder, frame_filename)
                cv2.imwrite(file_path, frame)
                log.info(f"{frame_filename} is write to {file_path}")

            if temp1 & 0xFF == ord('b'):
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                frame_filename = f'bad_{timestamp}.jpg'
                file_path = os.path.join(temp_folder, frame_filename)
                cv2.imwrite(file_path, frame)
                log.info(f"{frame_filename} is write to {file_path}")

            if temp1 == ord('q'):
                self.running = False
