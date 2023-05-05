import cv2
import mediapipe as mp
import numpy as np

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose(model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
threshold = 0.1
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    # Display the image with the landmark annotations
    annotated_image = img.copy()
    mp.solutions.drawing_utils.draw_landmarks(annotated_image, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    cv2.imshow("Posture Detection", annotated_image)
    key = cv2.waitKey(1)
    # Break the loop if the user presses the "q" key
    if key == ord("q"):
        break

    if key == ord("c"):
        # Detect the posture landmarks using Mediapipe
        results = pose.process(img)

        # If landmarks were detected, compare them to the saved landmarks
        if results.pose_landmarks:
            # Load the saved landmark data from file
            with open("landmarks.npy", "rb") as f:
                saved_landmarks = np.load(f)

            # Extract the landmark data as a numpy array
            new_landmarks = np.array(
                [[lmk.x, lmk.y, lmk.z, lmk.visibility] for lmk in results.pose_landmarks.landmark])

            # Compute the mean absolute error between the new landmarks and the saved landmarks
            mean_error = np.mean(np.abs(new_landmarks - saved_landmarks))

            # Print whether the new posture is the same as the saved posture
            if mean_error < threshold:
                print("The posture is the same as the saved posture")
            else:
                print("The posture is different from the saved posture")

    if key == ord("s"):
        # If landmarks were detected, save them to a file
        if results.pose_landmarks:
            # Extract the landmark data as a numpy array
            landmark_data = np.array(
                [[lmk.x, lmk.y, lmk.z, lmk.visibility] for lmk in results.pose_landmarks.landmark])

            # Save the landmark data to a file
            with open("landmarks.npy", "wb") as f:
                np.save(f, landmark_data)
                print("Saved")
        else:
            print("Failed to save")

cap.release()
cv2.destroyAllWindows()
