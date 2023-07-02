import multiprocessing
import threading

import cv2
from Config import get_config, TEMP, app_folder
import time
import logging as log
import os
import mediapipe as mp
import numpy as np
import concurrent.futures
DURATION = 5


def calculate_brightness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = int(gray.mean())
    return brightness


def get_landmark(frame):
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            landmarks = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.pose_landmarks.landmark])
            return landmarks
        else:
            return None


def buffer_frames():
    values = get_config()
    cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)

    frames = []
    start_time = time.time()
    end_time = start_time + DURATION

    while time.time() <= end_time:
        ret, frame = cap.read()

        if not ret:
            log.error("Invalid video source, cap.read() failed")
            raise Exception("Invalid video source")

        frames.append(frame)

        # Display the frame with pose landmarks and labels
        cv2.imshow("Pose Landmarks", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass
    # Release the VideoCapture and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    log.info("Frame buffering completed")

    return frames


class LandmarkExtractor:
    def __init__(self):
        self.failed_count = 0

    def extract_landmark(self, frame, folder, lock, counter):

        # Make exception for black image
        mean_intensity = frame.mean()
        if mean_intensity > 10:
            frame_landmark = get_landmark(frame)
            if frame_landmark is not None:
                with lock:
                    frame_count = counter.value
                    counter.value += 1
                frame_path = os.path.join(folder, f"frame_{frame_count}.npy")
                np.save(frame_path, frame_landmark)
            else:
                self.failed_count += 1
        else:
            self.failed_count += 1

        if self.failed_count > 30:
            self.failed_count = 0
            log.warning("Make sure your face is clearly visible in the preview")
            raise Exception("Face Not Detected")

    def extract_landmarks_and_buffer_frames(self, categories, append):
        output_folder = os.path.join(app_folder, TEMP)
        folder = os.path.join(output_folder, categories)

        # Make sure folder exists
        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(folder, exist_ok=True)

        if not append:
            # Iterate over the files in the folder
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                os.remove(file_path)
            log.info("Temp folder cleared")

        # Create a ThreadPoolExecutor with the number of desired threads
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count())
        # Create a lock for file writing synchronization
        lock = threading.Lock()

        # Create a shared counter
        files = os.listdir(folder)
        frame_count = len(files) + 1
        counter = multiprocessing.Value('i', frame_count)

        try:
            frames = buffer_frames()
            # Submit the extract_landmark function for each frame
            futures = [executor.submit(self.extract_landmark, frame, folder, lock, counter) for frame in frames]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)
            log.info("Frames extraction completed")

        except Exception as e:
            log.error(e)