# import shutil
import cv2
from Config import get_config, TEMP, app_folder
import time
import logging as log
import os
import mediapipe as mp
import numpy as np
from threading import Thread

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


def extract_landmark(frames, folder):

    files = os.listdir(folder)

    frame_count = len(files) + 1
    failed_count = 0

    for frame in frames:
        # Make exception for black image
        mean_intensity = frame.mean()
        if mean_intensity > 10:
            frame_landmark = get_landmark(frame)
            if frame_landmark is not None:
                frame_path = os.path.join(folder, f"frame_{frame_count}.npy")
                np.save(frame_path, frame_landmark)
                frame_count += 1
            else:
                failed_count += 1
        else:
            failed_count += 1

        if failed_count > 30:
            log.warning("Make sure your face is clearly visible in the preview")  # TODO

    log.info("Frames extraction completed")  # TODO


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
            break

        frames.append(frame)

        # Display the frame with pose landmarks and labels
        cv2.imshow("Pose Landmarks", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    log.info("Frame buffering completed")

    return frames


def extract_landmarks_and_buffer_frames(categories, append):
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

    frames = buffer_frames()

    t1 = Thread(target=extract_landmark, args=(frames, folder))
    t1.start()