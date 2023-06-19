import cv2
from Config import get_config
import logging as log
import joblib
from PostureRecognize.Model import model_file
from PostureRecognize.FrameProcess import get_landmark
import numpy as np

classifier = joblib.load(model_file)


def capture_landmarks():
    # Create a VideoCapture object to capture video from the camera
    values = get_config()
    cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)  # 0 indicates the default camera

    while True:
        # Read the video frames
        ret, frame = cap.read()

        if not ret:
            log.error("Invalid video source, cap.read() failed")
            break

        # Get landmark of frame
        landmark = get_landmark(frame)

        if landmark is not None:

            # Do further processing with the pose landmarks
            labels = detect_posture(landmark)
            # Display the labels on the frame
            label_text = f"Posture: {labels}"
            cv2.putText(frame, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the frame with pose landmarks and labels
        cv2.imshow("Pose Landmarks", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


def detect_posture(landmark):
    # Reshape the landmarks array to have the correct shape
    landmarks = np.array(landmark)
    landmarks = landmarks.reshape(-1, 3)

    # Use the loaded model for predictions or other tasks
    predictions = classifier.predict(landmarks)

    # Count the number of good and bad posture predictions
    num_good = np.count_nonzero(predictions == 0)
    num_bad = np.count_nonzero(predictions == 1)

    # Determine the majority and print the result
    if num_good > num_bad:
        result = "The majority is good posture."
    elif num_bad > num_good:
        result = "The majority is bad posture."
    else:
        result = "Equal number of good and bad postures."

    return result
