import ast
import configparser
import os
import logging as log
import datetime

from psutil import process_iter
from pygrabber.dshow_graph import FilterGraph

# ACCURACY AND PERFORMANCE
DETECTION_RATE = 0.5  # second


# FILE
PSW_HASH = "hash.txt"
TEMP = 'temps'
LOG_FOLDER = 'logs'

# PATH
ICON_PATH = "Resources/logo.ico"
appdata_path = os.getenv('APPDATA')
app_folder = os.path.join(appdata_path, 'AlignPosition')
main_folder = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(main_folder, LOG_FOLDER)
model_file = os.path.join(main_folder, 'trained_model.joblib')

# LOGGING
X = datetime.datetime.now()
FORMAT = X.strftime("%Y") + '-' + X.strftime("%m") + '-' + X.strftime("%d") + ' ' + X.strftime("%H") + X.strftime(
    "%M") + X.strftime("%S")
# Maximum number of log records allowed
max_log_records = 10

# Create log folders if they don't exist
os.makedirs(log_folder, exist_ok=True)

# Get a list of log files in the folder
log_files = [f for f in os.listdir(log_folder) if f.endswith('.log')]

# Sort the log files by modification time in ascending order
log_files.sort(key=lambda x: os.path.getmtime(os.path.join(log_folder, x)))

# Delete the oldest log file if there are more than 3 log files
if len(log_files) > 3:
    oldest_log_file = os.path.join(log_folder, log_files[0])
    os.remove(oldest_log_file)

log.basicConfig(
    level=log.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        log.FileHandler(os.path.join(log_folder, FORMAT + '.log')),
        log.StreamHandler()
    ]
)

# DEFAULT
CONFIG_PATH = f'{main_folder}/config.ini'
DEFAULT_VAL = {
    'camera': 0,
    'speed': 1,
    'idle': 5,
    'rest': 5,
    'notifications': True,
    'background': True,
    'init': True,
}

# COLORS
APP_BACKGROUND_COLOR = '#1FC3B7'  # LIGHT GREEN

# TEXT STYLE
TITLE_TEXT_SIZE = 26
TEXT_SIZE = 18
SMALL_TEXT = 12
TEXT_COLOR = '#ffffff'  # WHITE
SYNC_TEXT_COLOR = '#0F615B'  # DARK GREEN
BUTTON_COLOR = '#0F615B'
FONT = 'Calibri'


# check alive of program
def check_process():
    if "Align Position" in (p.name() for p in process_iter()):
        return False
    else:
        return True


# get camera list
def get_available_cameras():
    available_cameras = {}
    try:
        devices = FilterGraph().get_input_devices()
        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
    finally:
        return available_cameras


# update value
def write_config(dictionary_str):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(CONFIG_PATH)
    config.optionxform = str
    config['Option'] = ast.literal_eval(str(dictionary_str))
    with open(CONFIG_PATH, "w") as f:
        log.info("Config updated")
        config.write(f)


# create or reset config
def create_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config['Option'] = DEFAULT_VAL
    with open(CONFIG_PATH, "w") as f:
        log.info("Reset/create config")
        config.write(f)


# read value from config
def read_config():
    if os.path.exists(CONFIG_PATH):
        # Read config from a file
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(CONFIG_PATH)
        config_dict = dict(config['Option'])
        return config_dict
    else:
        log.warning("Config not found")
        create_config()


# Check value valid before read value
def get_config():
    try:
        check_condition()
    except Exception as e:
        log.error(e)
        create_config()
    finally:
        var = read_config()
        return var


# check config condition
def check_condition():
    try:
        read_config()  # to make sure the file is initialized
        values = read_config()
        if len(values) != len(DEFAULT_VAL):
            raise Exception("Invalid config option")
        int(values.get('camera'))
        float(values.get('speed'))
        float(values.get('idle'))
        float(values.get('rest'))
        a = values.get('background') == 'True' or values.get('background') == 'False'
        b = values.get('notifications') == 'True' or values.get('notifications') == 'False'
        c = values.get('init') == 'True' or values.get('init') == 'False'
        if not (a and b and c):
            raise Exception("Invalid config option")
    except Exception as e:
        raise Exception("Invalid config values")
