import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from notifypy import Notify
from cvzone import putTextRect
import initialize as i
import time as t

# counter to decide condition
counter_position = 0
counter_face = 0
object_distance = 0

# condition to break/stop thread
condition = True

# use to update main window usetime tracker
use_time = 0
temp_time = 0
total_time = 0
rest_timer = 0
notification = Notify(default_application_name="AlignPosition.exe",
                      default_notification_icon="Resources/logo.ico")


# Notification list
def active_notification(value):
    values = i.get_val()
    if values.get('Notifications'):
        if value == 0:
            notification.title = "Detection Start!"
            notification.message = "Monitoring your health from now!"
            notification.send(block=False)
        elif value == 1:
            notification.title = "Take a break!"
            notification.message = "You already use computer for a long time"
            notification.send(block=False)
        elif value == 2:
            notification.title = "Sit Properly!"
            notification.message = "Keep your position right"
            notification.send(block=False)
        else:
            notification.title = "Something Wrong..."
            notification.message = "This shouldn't happened!"
            notification.send(block=False)


# Detect Position
def position_detect():
    global object_distance
    global counter_position
    values = i.get_val()
    try:
        ds = float(values.get('Distance'))
        r = float(values.get('Range'))
        if object_distance < (ds - r):
            if counter_position >= values.get('Position'):
                active_notification(2)
                counter_position = 0
            else:
                counter_position += 1
        else:
            counter_position = 0
    except ValueError:
        pass


# Track Use Time
def computer_time(rest_time):
    global rest_timer
    rest = use_time - rest_timer
    if rest >= (rest_time * 60):
        active_notification(1)
        rest_timer = use_time


# Provide tool to calibrate focal length
def calibration():
    values = i.get_val()
    W = (float(values.get('Width'))) / 10
    d = float(values.get('Distance'))
    cap = cv2.VideoCapture(values.get('Camera'), cv2.CAP_DSHOW)
    detector = FaceMeshDetector(maxFaces=1)
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            w, _ = detector.findDistance(pointLeft, pointRight)
            f = (d * w) / W
            print(f)

            putTextRect(img, f'Focal Length: {round(f, 2)}',
                        (face[10][0] - 100, face[10][1] - 50),
                        scale=1.5)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# Detect Face
def distance_measure():
    global object_distance, counter_face, counter_position, use_time, temp_time, total_time
    values = i.get_val()
    W = float(values.get('Width')) / 10
    f = float(values.get('Focal'))
    cap = cv2.VideoCapture(values.get('Camera'), cv2.CAP_DSHOW)
    detector = FaceMeshDetector(maxFaces=1)
    active_notification(0)
    while condition:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)
        t.sleep(float(values['Speed']))
        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            w, _ = detector.findDistance(pointLeft, pointRight)
            d = round((W * f) / w, 2)
            position_detect()
            object_distance = d
            counter_face = 0
            use_time += 1
        else:
            counter_face += 1
            if counter_face > values.get('Idle'):
                counter_position = 0
            else:
                use_time += 1
        computer_time(values.get('Rest'))
        temp_time = total_time + use_time
    else:
        total_time += use_time
