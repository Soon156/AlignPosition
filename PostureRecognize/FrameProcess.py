import multiprocessing
import shutil
import threading
import cv2
from PySide6.QtWidgets import QApplication
from Funtionality.Config import oldTemp_folder, temp_folder
import time
import logging as log
import os
import mediapipe as mp
import numpy as np
import concurrent.futures


def temp_backup_restore(condition="False"):  # True: restore, False: backup
    if condition == "True":
        source_folder = oldTemp_folder
        destination_folder = temp_folder
        log_message = "Temp Restore"
    else:
        source_folder = temp_folder
        destination_folder = oldTemp_folder
        log_message = "Temp Backup"
    try:
        # Clear the destination folder
        shutil.rmtree(destination_folder, ignore_errors=True)
        for item in os.listdir(source_folder):
            source_item = os.path.join(source_folder, item)
            destination_item = os.path.join(destination_folder, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)
            else:
                shutil.copy(source_item, destination_item)
    except:
        pass

    log.info(log_message)


def get_landmark(frame):
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            landmarks = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.pose_landmarks.landmark])
            mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            return frame, landmarks
        else:
            return frame, None


def buffer_frames(cap, duration=5):
    frames = []
    start_time = time.time()
    end_time = start_time + duration

    while time.time() <= end_time:
        ret, frame = cap.read()

        if not ret:
            log.error("Invalid video source, cap.read() failed")
            raise Exception("Invalid video source")

        frames.append(frame)

    log.info("Frame buffering completed")

    return frames


# TODO change to QThread, concurrent have issue with PYQT
class LandmarkExtractor:
    def __init__(self):
        self.failed_count = 0

    def extract_landmark(self, frame, folder, lock, counter, threshold=50, ):
        frame_count = 0
        # Make exception for black image
        mean_intensity = frame.mean()
        if (255 - threshold) > mean_intensity > threshold:
            frame, frame_landmark = get_landmark(frame)
            if frame_landmark is not None:
                with lock:
                    frame_count = counter.value
                    counter.value += 1
                frame_path = os.path.join(folder, f"frame_{frame_count}.npy")
                np.save(frame_path, frame_landmark)

        if self.failed_count > 50:  # TODO change to frame_count
            log.warning(f"Make sure your face is clearly visible in the preview. Failed Count: {self.failed_count}")
            self.failed_count = 0
            raise Exception("Face Not Detected")

    def extract_landmarks_and_buffer_frames(self, win, categories):

        if categories == "append":
            counter = 1
            while True:
                folder = os.path.join(temp_folder, f"append_{counter}")
                if not os.path.exists(folder):
                    os.makedirs(folder, exist_ok=True)
                    break
                counter += 1
        else:
            folder = os.path.join(temp_folder, categories)
            # Make sure folder exists
            os.makedirs(folder, exist_ok=True)

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
            frames = buffer_frames(win.camera)
            win.hint_lbl.setText("Relax yourself, processing data....")  # Set the initial text
            QApplication.processEvents()
            # Submit the extract_landmark function for each frame
            futures = [executor.submit(self.extract_landmark, frame, folder, lock, counter) for frame in frames]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)
            log.info("Frames extraction completed")
        except Exception as e:
            log.error(e)
            raise Exception
