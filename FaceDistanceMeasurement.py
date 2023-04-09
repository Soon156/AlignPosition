import cv2
# from cvzone.FaceMeshModule import FaceMeshDetector
# from cvzone import putTextRect
import Config as i
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
'''
# Provide tool to calibrate focal length
def calibration():
    values = i.get_val()
    W = (float(values.get('width'))) / 10
    d = float(values.get('distance'))
    cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)
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
'''
'''
# Detect Face
def distance_measure():
    global object_distance, counter_face, counter_position, use_time, temp_time, total_time
    values = i.get_val()
    W = float(values.get('width')) / 10
    f = float(values.get('focal'))
    cap = cv2.VideoCapture(int(values.get('camera')), cv2.CAP_DSHOW)
    detector = FaceMeshDetector(maxFaces=1)
    active_notification(0)
    while condition:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)
        t.sleep(float(values['speed']))
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
            if counter_face > float(values.get('idle')):
                counter_position = 0
            else:
                use_time += 1
        computer_time(float(values.get('rest')))
        temp_time = total_time + use_time
    else:
        total_time += use_time
'''