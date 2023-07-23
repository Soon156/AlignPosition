import cv2
import time
import logging as log
import joblib
import numpy as np
from PySide6.QtCore import Signal, QObject
from Funtionality.Config import get_config, DETECTION_RATE
from PostureRecognize.ElapsedTime import read_elapsed_time_data, save_elapsed_time_data
from PostureRecognize.Model import model_file
from PostureRecognize.FrameProcess import get_landmark


class PostureRecognizer(QObject):
    elapsed_time_updated = Signal(int)

    def __init__(self):
        super().__init__()
        self.running = False
        self.classifier = None
        self.old_time = read_elapsed_time_data()
        self.elapsed_time = 0
        self.new_time = 0
        self.badCount = 0
        self.goodCount = 0

    def load_model(self):
        try:
            self.classifier = joblib.load(model_file)
        except FileNotFoundError as e:
            log.error(e)

    def start_capture(self):
        self.running = True
        self.capture_landmarks()

    def stop_capture(self):
        self.running = False

    def capture_landmarks(self):
        # Create a VideoCapture object to capture video from the camera
        values = get_config()
        cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)  # 0 indicates the default camera
        start_time = time.time()
        idle_time = 0
        temp_time = 0
        total_time = 0
        counter = False
        while self.running:
            # Read the video frames
            ret, frame = cap.read()

            if not ret:
                log.error("Invalid video source, cap.read() failed")
                raise Exception("cap.read() failed")

            # Get landmark of frame
            landmark = get_landmark(frame)

            if landmark is not None:
                # Do further processing with the pose landmarks
                labels = self.detect_posture(landmark)

                # Display the labels on the frame
                label_text = f"Posture: {labels}"
                cv2.putText(frame, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Update the elapsed time only if landmark is not None
                self.elapsed_time = int(time.time() - start_time)
                if counter:
                    total_time += temp_time
                self.new_time = self.old_time + self.elapsed_time - total_time
                self.elapsed_time_updated.emit(self.new_time)
                counter = False

            else:
                if not counter:
                    idle_time = time.time()
                    counter = True
                else:
                    pass_time = int(time.time() - idle_time)
                    # Check if the counter should be updated
                    if pass_time >= float(values.get('idle')) * 60:
                        temp_time = pass_time

            # Display the frame with pose landmarks and labels
            cv2.imshow("Pose Landmarks", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        save_elapsed_time_data(self.new_time)
        self.old_time = self.new_time
        # Release the VideoCapture and close the OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    def detect_posture(self, landmark):
        # Reshape the landmarks array to have the correct shape
        landmarks = np.array(landmark)
        landmarks = landmarks.reshape(-1, 3)

        # Use the loaded model for predictions or other tasks
        predictions = self.classifier.predict(landmarks)

        # Count the number of good and bad posture predictions
        num_good = np.count_nonzero(predictions == 0)
        num_bad = np.count_nonzero(predictions == 1)
        # print(f" {num_good}   :   {num_bad}")
        result = "Detecting..."
        # Determine the majority and print the result
        if num_good >= num_bad:
            self.goodCount += 1
            if self.goodCount >= 5:
                result = "The majority is good posture."
                self.badCount = 0
        elif num_bad > num_good:
            self.badCount += 1
            if self.badCount >= 5:
                result = "The majority is bad posture."
                self.goodCount = 0
        return result
