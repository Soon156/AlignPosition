import ast
from psutil import process_iter
from pygrabber.dshow_graph import FilterGraph
import configparser
import csv
import cv2
import uuid
import os


# default config
file_name = 'config.ini'
default_value = {'width': 63,
                 'focal': 840,
                 'distance': 53,
                 'camera': 0,
                 'range': 10,
                 'speed': 1,
                 'position': 5,
                 'idle': 5,
                 'rest': 5,
                 'scaling': 1.0,
                 'appearance': 'System',
                 'notifications': True,
                 'background': True,
                 'init': True
                 }


# save value to config
def write_config(dictionary_str):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_name)
    config.optionxform = str
    config['Option'] = ast.literal_eval(str(dictionary_str))
    with open(file_name, "w") as f:
        config.write(f)


# create or reset config
def create_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config['Option'] = default_value
    with open(file_name, "w") as f:
        config.write(f)


# read value from config
def read_config():
    # Read config from a file
    config = configparser.ConfigParser()
    config.read(file_name)
    config_dict = dict(config['Option'])
    return config_dict


# get camera list
def get_available_cameras():
    available_cameras = {}
    try:
        devices = FilterGraph().get_input_devices()
        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
    finally:
        return available_cameras


# Check value type when get value
def get_val():
    try:
        check_condition()
    except Exception as e:
        print(e)
        create_config()
    finally:
        var = read_config()
        return var


# avoid program to run 2 times
def check_process():
    if "AlignPosition.exe" in (p.name() for p in process_iter()):
        return False
    else:
        return True


# check config condition
def check_condition():
    values = read_config()
    for i in default_value:
        if i not in values:
            raise Exception()
    float(values.get('width'))
    float(values.get('focal'))
    float(values.get('distance'))
    float(values.get('range'))
    int(values.get('camera'))
    float(values.get('speed'))
    float(values.get('position'))
    float(values.get('idle'))
    float(values.get('rest'))
    float(values.get('scaling'))
    a = values.get('background') == 'True' or values.get('background') == 'False'
    b = values.get('notifications') == 'True' or values.get('notifications') == 'False'
    c = values.get('init') == 'True' or values.get('init') == 'False'
    d = values.get('appearance') == 'System' or values.get('appearance') == 'Light' or \
        values.get('appearance') == 'Dark'
    e = values.get('scaling') == 1.2 or values.get('scaling') == 1.1 or values.get('scaling') == 1.0 \
        or values.get('scaling') == 0.9 or values.get('scaling') == 0.8
    if not (a or b or c or d or e):
        raise Exception()


directory = "./conf/position"
landmark_filepath = "./conf/position/landmark.csv"
thumbnail_filepath = "./conf/position/.thumbnail/"


def new_landmark(landmark, thumbnail):
    os.makedirs(directory)
    os.makedirs(thumbnail_filepath)
    with open(landmark_filepath, 'w', newline='') as csvfile:
        write_landmark(csvfile, landmark, thumbnail)


def append_landmark(landmark, thumbnail):
    try:
        # Open the CSV file in append mode
        with open(landmark_filepath, 'a', newline='') as csvfile:
            write_landmark(csvfile, landmark, thumbnail)
    except FileNotFoundError:
        new_landmark(landmark, thumbnail)


def write_landmark(csvfile, landmark, thumbnail):
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Generate a unique ID for the data
    landmarks_id = str(uuid.uuid1())

    # Save the frame as a PNG image file
    new_filepath = thumbnail_filepath + landmarks_id + ".jpg"
    cv2.imwrite(new_filepath, thumbnail)

    row = [landmarks_id, new_filepath]
    # Loop through the landmarks and write each row to the CSV file
    for position in landmark:
        # Create a list with the data to be written to the CSV file
        row += [position.x, position.y, position.z]

    # Write the row to the CSV file
    writer.writerow(row)


def read_landmarks_from_csv():
    landmarks_list = []
    with open(landmark_filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Parse the landmarks ID and thumbnail path from the CSV row
            landmarks_id = row[0]
            thumbnail_path = row[1]

            # Parse the landmark positions from the CSV row
            landmark = []
            for i in range(2, len(row), 3):
                x, y, z = float(row[i]), float(row[i + 1]), float(row[i + 2])
                landmark.extend([x, y, z])
            # Append the landmarks ID, positions, and thumbnail path to the list
            landmarks_list.extend([landmarks_id, thumbnail_path, landmark])
    return landmarks_list


def read_thumbnail(thumbnail_path):
    # Load the image file
    img = cv2.imread(thumbnail_path)

    # Display the image
    cv2.imshow('Image', img)
    cv2.waitKey(0)


# print(read_landmarks_from_csv())
# read_thumbnail(read_landmarks_from_csv()[1])
