from ast import literal_eval
from psutil import process_iter
from pygrabber.dshow_graph import FilterGraph

# default config
file_name = 'config.txt'
default_value = {'Width': 63,
                 'Focal': 840,
                 'Distance': 53,
                 'Camera': 0,
                 'Range': 10,
                 'Speed': 1,
                 'Position': 5,
                 'Idle': 5,
                 'Rest': 5,
                 'Scaling': 1.0,
                 'Appearance': 'System',
                 'Notifications': True,
                 'Background': True,
                 'Init': True
                 }


# get camera list
def get_available_cameras():
    available_cameras = {}
    try:
        devices = FilterGraph().get_input_devices()
        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
    finally:
        return available_cameras


# save value to config
def save_value(input_value):
    with open(file_name, 'w') as f:
        f.write(input_value)


# read value from config
def load_value(filename):
    with open(filename, 'r') as f:
        read = f.read()
    return read


# Check value type when get value
def get_val():
    try:
        check_condition()
    except ValueError:
        create_config()
    except AttributeError:
        create_config()
    except TypeError:
        create_config()
    except Exception:
        create_config()
    finally:
        var = literal_eval(load_value(file_name))
        return var


# avoid program to run 2 times
def check_process():
    if "Align Position" in (p.name() for p in process_iter()):
        return False
    else:
        return True


# W, eyes distance (Width)
# f, focal length (Focal)
# w, pixel distance (set by ml)
# d, distance between camera and object (Distance)

# create or rest config
def create_config():
    save_value(str(default_value))


# check config condition
def check_condition():
    values = literal_eval(load_value(file_name))
    for i in default_value:
        if i not in values:
            raise Exception()
    float(values.get('Width'))
    float(values.get('Focal'))
    float(values.get('Distance'))
    float(values.get('Range'))
    int(values.get('Camera'))
    float(values.get('Speed'))
    float(values.get('Position'))
    float(values.get('Idle'))
    float(values.get('Rest'))
    float(values.get('Scaling'))
    a = values.get('Background') == True or values.get('Background') == False
    b = values.get('Notifications') == True or values.get('Notifications') == False
    c = values.get('Init') == True or values.get('Init') == False
    d = values.get('Appearance') == 'System' or values.get('Appearance') == 'Light' or \
        values.get('Appearance') == 'Dark'
    e = values.get('Scaling') == 1.2 or values.get('Scaling') == 1.1 or values.get('Scaling') == 1.0 \
        or values.get('Scaling') == 0.9 or values.get('Scaling') == 0.8
    if not (a or b or c or d or e):
        raise Exception()
