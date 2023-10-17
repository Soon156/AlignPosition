from datetime import date, datetime
import tensorflow as tf
import cv2
import time
import numpy as np
from PySide6.QtCore import Signal, QThread
from Funtionality.Config import get_config, abs_model_file_path
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
        self.running = False
        self.model = tf.keras.models.load_model(abs_model_file_path)
        self.old_time, self.badCount = read_elapsed_time_data()
        self.new_time = self.old_time
        self.date_today = date.today()

    def run(self):
        try:
            self.running = True
            average = 0
            detector = LandmarkResult()
            # Create a VideoCapture object to capture video from the camera
            values = get_config()
            cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)
            start_time = time.time()

            # Control speed and calculate result
            frame_count = 0
            label = ""
            bad_control = False
            results = []

            # Control idle time
            idle_time = 0
            temp_time = 0
            counter = False

            # Threshold & controller
            switch = False
            threshold = 70
            blank_counter = 0

            while self.running and not switch:

                if not cap.isOpened():
                    switch = True
                    log.warning("Camera not available")

                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)

                if not ret and not switch:
                    switch = True
                    log.error("Error reading frame")
                else:
                    mean_value = np.mean(frame)
                    if mean_value < threshold:
                        blank_counter += 1
                        print(blank_counter)
                        if blank_counter >= 250:  # about 30 sec base on cpu power
                            switch = True
                    else:
                        blank_counter = 0
                        switch = False

                if not switch:
                    frame_count += 1
                    if frame_count >= 25 and not counter:
                        frame_count = 0
                        if not len(results) == 0:
                            average = sum(results) / len(results)
                        else:
                            average = 0
                        predicted_labels = [0 if average < 0.6 else 1]
                        results = []

                        if predicted_labels[0] == 0:
                            label = "good"
                        else:
                            label = "bad"

                    elif frame_count % 5 == 0:
                        # Get landmark of frame
                        detector.detect_async(frame)
                        result = detector.result
                        try:
                            landmark = extract_landmark(result)
                            if landmark is not None:

                                reshape_landmark = np.array(landmark).reshape(-1, 33 * 5)
                                predictions = self.model.predict(
                                    reshape_landmark, verbose=None)  # Make predictions using the trained model
                                results.append(predictions[0, 0])

                                # Update the elapsed time
                                if counter:  # If there is idle
                                    start_time += temp_time
                                self.new_time = int(time.time() - start_time) + self.old_time
                                self.elapsed_time_updated.emit(self.new_time)

                                counter = False  # Reset idle flag
                            else:
                                label = "idle"
                                if not counter:  # If not idle before
                                    idle_time = time.time()
                                    counter = True

                                else:  # If idle
                                    pass_time = int(time.time() - idle_time)

                                    # Check if the counter should be updated
                                    if pass_time >= float(values.get('idle')) * 60:  # If idle time > threshold
                                        temp_time = pass_time  # set temp time
                                    else:
                                        temp_time = 0  # reset temp time to avoid minus if smaller then threshold
                        except Exception as e:
                            if str(e) not in ["cannot reshape array of size 1 into shape (165)",
                                              "type object 'PoseLandmarkerResult' has no attribute 'pose_landmarks'"]:
                                raise Exception(e)

                    # Display the labels on the dev frame
                    self.update_overlay.emit(label)

                    if label == "bad":
                        if bad_control:
                            self.badCount += 1
                            bad_control = False
                    else:
                        bad_control = True
                else:  # TODO active input thread
                    self.running = False
                    self.error_msg.emit("Camera reading failed, please make sure you are in bright environment, "
                                        "activity monitor trough keyboard/mouse WIP")
                    log.info("Switching to input detection, this will be implement in future....")

                if date.today() != self.date_today:  # Reset the time if pass 12am
                    save_elapsed_time_data(self.new_time, self.date_today, self.badCount)
                    self.new_time = 0
                    self.old_time = self.new_time
                    self.badCount = 0

                if values.get('dev') == "True":
                    label_text = f"Posture: {label}, {average}"
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
                        cv2.imwrite(frame_filename, frame)
                        log.info(f"{frame_filename} is write")

                    if temp1 & 0xFF == ord('b'):
                        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        frame_filename = f'bad_{timestamp}.jpg'
                        cv2.imwrite(frame_filename, frame)
                        log.info(f"{frame_filename} is write")

                    if temp1 == ord('q'):
                        self.running = False

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
        save_elapsed_time_data(self.new_time, self.date_today, self.badCount)
        self.old_time = self.new_time
