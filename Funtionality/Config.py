import configparser
import os
import logging as log
import datetime
import winreg

from psutil import process_iter
from pygrabber.dshow_graph import FilterGraph

import shutil

Good_Posture = "Maintain your good posture 5 seconds, clicked proceed to start"
Bad_Posture = "Maintain your bad posture 5 seconds, clicked proceed to start"
Append_Posture = "Append bad posture, clicked proceed to start"
Cancel_Calibrate = "Calibration Cancel"
Append_Finish = "Append done"
Model_Training = "Training model, please wait patiently...."
Cancel = "Cancelling..."
Capture_Posture = "Capturing posture, stay still...."

# ACCURACY AND PERFORMANCE
DETECTION_RATE = 0.5  # second

# Get the current month and year
now = datetime.datetime.now()
current_month, current_year = now.month, now.year

# App_Use_Time Filter List
filter_list = ["Align Position", "null", "Application Frame Host", "", "Pick an app"]


def get_registry_value(key=winreg.HKEY_CURRENT_USER, subkey="SOFTWARE\Align Position", value_name="Resource Folder"):
    try:
        with winreg.OpenKey(key, subkey) as registry_key:
            value, _ = winreg.QueryValueEx(registry_key, value_name)
            return value
    except:
        library_in_production = os.path.dirname(package_folder)
        return library_in_production


# PATH
logo_path = "Resources\logo.ico"
overlay_logo_path = "Resources\overlay-pic.png"
appdata_path = os.getenv('APPDATA')
app_folder = os.path.join(appdata_path, 'AlignPosition')
log_folder = os.path.join(app_folder, 'logs')
model_file = 'posture_detection_model.keras'
detection_file = 'pose_landmarker_full.task'
temp_folder = os.path.join(app_folder, 'temps')
b_config = os.path.join(temp_folder, 'config_old.ini')
userdata = os.path.join(app_folder, 'usr_data.bin')
app_use_time_file = f"use_time_{current_month:02d}_{current_year}.bin"
app_use_time = os.path.join(app_folder, app_use_time_file)
allow_use_time = os.path.join(app_folder, "table_time.bin")
package_folder = os.path.dirname(os.path.abspath(__file__))

install_path = get_registry_value()

abs_logo_path = os.path.join(install_path, logo_path)
abs_overlay_pic_path = os.path.join(install_path, overlay_logo_path)
abs_model_file_path = os.path.join(install_path, model_file)
abs_detection_file_path = os.path.join(install_path, detection_file)
hidden_file_path = os.path.expanduser('~/.AlignPosition')
key_file_path = os.path.expanduser('~/.AlignPosition/user.key')
salt_file_path = os.path.expanduser('~/.AlignPosition/salt.bin')
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
app_name = "Align Position"
exe_path = os.path.join(install_path, "AlignPosition.exe --background")  # Production

# Create folders if they don't exist
os.makedirs(app_folder, exist_ok=True)
os.makedirs(log_folder, exist_ok=True)
os.makedirs(temp_folder, exist_ok=True)
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
    'auto': True,
    'monitoring': True,
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
    counter = 0
    for p in process_iter():
        if p.name() == "AlignPosition.exe":
            counter += 1
        if counter > 2:
            return True
    return False


def check_logo():
    if os.path.exists(abs_logo_path) and os.path.exists(abs_overlay_pic_path):
        return True
    else:
        return False


def check_model():
    if os.path.exists(abs_model_file_path) and os.path.exists(abs_detection_file_path):
        return True
    else:
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


# remove data
def remove_all_data():
    # remove
    try:
        contents = os.listdir(app_folder)
        for item in contents:
            item_path = os.path.join(app_folder, item)
            if os.path.isdir(item_path):  # Check if it's a directory
                if item != 'logs':  # Exclude the 'log' folder
                    # Remove the directory and its contents
                    shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        shutil.rmtree(hidden_file_path)
        # parental_monitoring()
        log.info("All data has been remove, app will close soon")
    except Exception as e:
        log.warning(e)


def reset_parental():
    try:
        # parental_monitoring()
        os.remove(allow_use_time)
    except FileNotFoundError:
        log.warning("File is not exist or already remove")


"""
   def parental_monitoring(value_name="Parental State", sub_key="SOFTWARE\Align Position"
                        , path=winreg.HKEY_CURRENT_USER, value=0):
    value = str(value)
    try:
        with winreg.OpenKey(path, sub_key, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value)
    except FileNotFoundError:
        with winreg.CreateKey(path, sub_key) as key:
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value)"""


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
        try:
            restore_config()
            check_condition()
        except:
            log.warning("Config restore failed")
            create_config()
    finally:
        var = read_config()
        return var


def restore_config():  # CHECKME
    if os.path.exists(b_config):
        log.warning("Backup config found")
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(b_config)
        config_dict = dict(config['Option'])

        config['Option'] = config_dict
        with open(CONFIG_PATH, "w") as f:
            config.write(f)
        log.warning("Config Restore")

    else:
        log.warning("No backup config found")
        create_config()


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
        i = values.get('monitoring') == 'True' or values.get('monitoring') == 'False'
        if not (a and b and c and e and f and g and h and i and float(values.get('rest')) >= 1):
            raise Exception("Invalid config value")
    except Exception as e:
        raise Exception(e)


def check_key():
    path = [key_file_path, salt_file_path]
    for item in path:
        if not os.path.exists(item):
            return False
    return True