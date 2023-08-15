import random
import shutil
import cv2
from Funtionality.Config import oldTemp_folder, temp_folder
import time
import logging as log
import os
import mediapipe as mp
import numpy as np


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


def buffer_frames(cap, duration=5, random_num=30):
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
    random_frames = random.sample(frames, random_num)

    return random_frames
