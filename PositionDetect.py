import cv2
import mediapipe as mp
from Config import append_landmark
saved_pose = []

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose(model_complexity=1)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        saved_pose = results.pose_landmarks.landmark
        '''
        # get the landmarks of the left and right eyes
        left_eye_landmarks = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_EYE] if results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_EYE] else None
        right_eye_landmarks = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_EYE] if results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_EYE] else None
        '''

        '''
        if left_eye_landmarks:
            # print the coordinates of the left eye landmarks
            print("Left eye landmarks:")
            print(f"x={left_eye_landmarks.x}, y={left_eye_landmarks.y}, z={left_eye_landmarks.z}")
        else:
            print("Left eye not detected")

        if right_eye_landmarks:
            # print the coordinates of the right eye landmarks
            print("Right eye landmarks:")
            print(f"x={right_eye_landmarks.x}, y={right_eye_landmarks.y}, z={right_eye_landmarks.z}")
        else:
            print("Right eye not detected")
        '''

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        ret, frame = cap.read()
        append_landmark(saved_pose, frame)

        break

cv2.destroyAllWindows()

'''
# Detect Position
def position_detect():
    global object_distance
    global counter_position
    values = i.get_val()
    try:
        ds = float(values.get('distance'))
        r = float(values.get('range'))
        if object_distance < (ds - r):
            if counter_position >= float(values.get('position')):
                # active_notification(2)
                counter_position = 0
            else:
                counter_position += 1
        else:
            counter_position = 0
    except ValueError:
        pass
        '''