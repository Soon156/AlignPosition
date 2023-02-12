import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from plyer import notification as n
from cvzone import putTextRect
import initialize as i
import time as t

# counter
counter_position = 0
counter_face = 0
object_distance = 0

condition = True

use_time = 0
temp_time = 0
total_time = 0
rest_timer = 0


def active_notification(value):
    values = i.get_val()
    if values.get('Notifications'):
        if value == 0:
            n.notify(
                app_name="Align Position",
                title="Detection Start!",
                message="Monitoring your health from now!",
                app_icon='Resources/logo.ico',
                timeout=5,
            )
        elif value == 1:
            n.notify(
                app_name="Align Position",
                title="Take a break!",
                message="You already use computer for a long time",
                app_icon='Resources/logo.ico',
                timeout=10,
            )
        elif value == 2:
            n.notify(
                app_name="Align Position",
                title="Sit Properly!",
                message="Keep your position right",
                app_icon='Resources/logo.ico',
                timeout=10,
            )
        elif value == 3:
            n.notify(
                title="Align Position",
                message="Take a break!",
                app_icon='Resources/logo.ico',
                timeout=5,
            )
        else:
            n.notify(
                title="Something Wrong...",
                message="This shouldn't happened!",
                app_icon='Resources/logo.ico',
                timeout=5,
            )


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


def computer_time(rest_time):
    global rest_timer
    rest = use_time - rest_timer
    if rest >= (rest_time * 60):
        active_notification(1)
        rest_timer = use_time


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

            putTextRect(img, f'Focal Length: {round(f,2)}',
                        (face[10][0] - 100, face[10][1] - 50),
                        scale=1.5)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def distance_measure():
    global object_distance, counter_face, counter_position, use_time, temp_time, total_time
    values = i.get_val()
    W = float(values.get('Width')) / 10
    f = float(values.get('Focal'))
    cap = cv2.VideoCapture(values.get('Camera'), cv2.CAP_DSHOW)
    detector = FaceMeshDetector(maxFaces=1)
    start = 0
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
