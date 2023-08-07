import ast
import configparser
import os
import logging as log
import datetime
from psutil import process_iter
from pygrabber.dshow_graph import FilterGraph
import winreg

VERSION = "0.0.1"

# ACCURACY AND PERFORMANCE
DETECTION_RATE = 0.5  # second
counter = 0  # To check the program exist

# Get the current month and year
now = datetime.datetime.now()
current_month, current_year = now.month, now.year

# App_Use_Time Filter List
filter_list = ["Windows Explorer", "Align Position", "null", "Application Frame Host", "Windows Problem Reporting",
               "Desktop Window Manager", ""]

# PATH
logo_path = "Resources\logo.ico"
appdata_path = os.getenv('APPDATA')
app_folder = os.path.join(appdata_path, 'AlignPosition')
log_folder = os.path.join(app_folder, 'logs')
model_file = os.path.join(app_folder, 'trained_model.joblib')
oldTemp_folder = os.path.join(app_folder, 'old_temps')
temp_folder = os.path.join(app_folder, 'temps')
userdata = os.path.join(app_folder, 'usr_data.bin')
app_use_time_file = f"use_time_{current_month:02d}_{current_year}.bin"
app_use_time = os.path.join(app_folder, app_use_time_file)
package_folder = os.path.dirname(os.path.abspath(__file__))
library_in_production = os.path.dirname(package_folder)
home_in_pro = os.path.dirname(library_in_production)
abs_logo_path = os.path.join(library_in_production, logo_path)  # Test
# abs_logo_path = os.path.join(home_in_pro, logo_path)  # Production
key_file_path = os.path.expanduser('~/.AlignPosition/user.key')
salt_file_path = os.path.expanduser('~/.AlignPosition/salt.bin')
fernet_file_path = os.path.expanduser('~/.AlignPosition/fernet.key')
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
app_name = "Align Position"
exe_path = os.path.join(library_in_production, "Align Position.exe")

# Create folders if they don't exist
os.makedirs(app_folder, exist_ok=True)
os.makedirs(log_folder, exist_ok=True)
os.makedirs(temp_folder, exist_ok=True)
os.makedirs(oldTemp_folder, exist_ok=True)
os.makedirs(os.path.dirname(key_file_path), exist_ok=True)  # Create the directory if it doesn't exist

# LOGGING
X = datetime.datetime.now()
FORMAT = X.strftime("%Y") + '-' + X.strftime("%m") + '-' + X.strftime("%d") + ' ' + X.strftime("%H") + X.strftime(
    "%M") + X.strftime("%S")
# Maximum number of log records allowed
max_log_records = 10

log.basicConfig(
    level=log.INFO,
    format='%(asctime)s %(levelname)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        log.FileHandler(os.path.join(log_folder, FORMAT + '.log')),
        log.StreamHandler()
    ]
)

# DEFAULT
CONFIG_PATH = f'{app_folder}/config.ini'
DEFAULT_VAL = {
    'camera': 0,
    'rest': 60,
    'idle': 0.1,
    'notifications': True,
    'background': True,
    'app_tracking': False,
    'overlay': "Right",
    'overlay_enable': True,
    'auto': False,
    'init': True,
    'dev': False
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


# clear log if exist >3
def clear_log():
    log_files = [f for f in os.listdir(log_folder) if f.endswith('.log')]
    log_files.sort(key=lambda x: os.path.getmtime(os.path.join(log_folder, x)))
    if len(log_files) > 3:
        files_to_remove = log_files[:-3]  # Get the files to remove (excluding the newest 3)
        for file_name in files_to_remove:
            file_path = os.path.join(log_folder, file_name)
            os.remove(file_path)
            log.info(f"Log file remove: {file_path}")


# check alive of program
def check_process():
    global counter
    for p in process_iter():
        if p.name() == "AlignPosition.exe":
            counter += 1
        if counter >= 2:
            log.error("Program is already run")
            return True
    return False


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
    print(dictionary_str["auto"])
    if dictionary_str["auto"] == "True":  # TODO check working
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        log.info("Auto-start Enable")
        pass
    else:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.DeleteValue(key, app_name)
        log.info("Auto-start Disable")
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(CONFIG_PATH)
    config.optionxform = str
    config['Option'] = ast.literal_eval(str(dictionary_str))
    with open(CONFIG_PATH, "w") as f:
        config.write(f)
        log.info("Config updated")


# create or reset config
def create_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config['Option'] = DEFAULT_VAL
    with open(CONFIG_PATH, "w") as f:
        config.write(f)
        log.info("Reset/create config")


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
        log.warning(e)
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
            create_config()
            raise Exception("Invalid config option")

        int(values.get('camera'))
        float(values.get('idle'))
        a = values.get('background') == 'True' or values.get('background') == 'False'
        b = values.get('notifications') == 'True' or values.get('notifications') == 'False'
        c = values.get('init') == 'True' or values.get('init') == 'False'
        e = values.get('auto') == 'True' or values.get('auto') == 'False'
        f = values.get('app_tracking') == 'True' or values.get('app_tracking') == 'False'
        g = values.get('overlay') == 'Right' or values.get('overlay') == 'Left'
        h = values.get('overlay_enable') == 'True' or values.get('overlay_enable') == 'False'
        if not (a and b and c and e and f and g and h and float(values.get('rest')) >= 1):
            raise Exception("Invalid config value")
    except Exception as e:
        log.warning(e)
