from configparser import ConfigParser
from json import dump, load
import os
import logging as log
from datetime import datetime
import winreg

import matplotlib as plt
from psutil import process_iter
from pygrabber.dshow_graph import FilterGraph

from shutil import rmtree

# Get the current month and year
now = datetime.now()
current_month, current_year = now.month, now.year

# App_Use_Time Filter List
filter_list = {"Align Position", "null", "Application Frame Host", "", "Pick an app", "LockApp.exe",
               "Modern Setup Host"}

# Chart Font
font = {'family': 'arial',
        'weight': 'normal',
        'size': 9,
        }

STRING_LIMIT = 13
GRAY_COLOR = '#5A5A5A'
plt.rc('font', **font)
plt.set_loglevel('WARNING')

# Color of chart
bright_colors_light_blue_theme = [
    "#ADD8E6",  # Light Blue
    "#87CEEB",  # Sky Blue
    "#89CFF0",  # Baby Blue
    "#40E0D0",  # Turquoise
    "#00FFFF",  # Cyan / Aqua
    "#AFEEEE",  # Pale Turquoise
    "#B0C4DE",  # Light Steel Blue
    "#B0E0E6",  # Powder Blue
    "#00BFFF"  # Deep Sky Blue
]

dark_colors_purple_theme = [
    "#9370DB",  # Medium Purple
    "#8A2BE2",  # Blue Violet
    "#800080",  # Purple
    "#9932CC",  # Dark Orchid
    "#9400D3",  # Dark Violet
    "#8B008B",  # Dark Magenta
    "#4B0082",  # Indigo
    "#6A5ACD",  # Slate Blue
    "#483D8B"  # Dark Slate Blue
]


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
landmark_model_full = 'pose_landmarker_full.task'
landmark_model_lite = 'pose_landmarker_lite.task'
temp_folder = os.path.join(app_folder, 'temps')
b_config = os.path.join(temp_folder, 'config_old.ini')
userdata = os.path.join(app_folder, 'usetime_data.bin')
app_use_time_file = f"program_usetime.bin"
app_use_time = os.path.join(app_folder, app_use_time_file)
allow_use_time = os.path.join(app_folder, "table_time.bin")
app_filter_list = os.path.join(app_folder, "filter.json")
package_folder = os.path.dirname(os.path.abspath(__file__))

install_path = get_registry_value()

abs_logo_path = os.path.join(install_path, logo_path)
abs_overlay_pic_path = os.path.join(install_path, overlay_logo_path)
abs_model_file_path = os.path.join(install_path, model_file)
abs_detection_file_path = os.path.join(install_path, landmark_model_full)
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
X = datetime.now()
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
    'rest': 30,
    'idle': 0.1,
    'bad_posture': 3,
    'input_idle': 30,
    'notifications': True,
    'background': True,
    'app_tracking': False,
    'overlay': "Right",
    'overlay_enable': True,
    'auto': True,
    'monitoring': True,
    'theme': 1,
    'init': True,
    'model': 'Full',
    'check_update': 'Yes',
    'dev': False
}


# clear log if exist >3
def clear_log():
    log_files = [f for f in os.listdir(log_folder) if f.endswith('.log')]
    log_files.sort(key=lambda x: os.path.getmtime(os.path.join(log_folder, x)))
    if len(log_files) > 5:
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
        if counter > 1:
            return True
    return False


def check_logo():
    if os.path.exists(abs_logo_path) and os.path.exists(abs_overlay_pic_path):
        return True
    else:
        return False


def check_model():
    global abs_detection_file_path
    values = get_config()
    if values['model'] != 'Lite':
        abs_detection_file_path = os.path.join(install_path, landmark_model_full)
    log.info(f'Landmarker model: {abs_detection_file_path}')
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
                    rmtree(item_path)
            else:
                os.remove(item_path)
        rmtree(hidden_file_path)
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
    config = ConfigParser(allow_no_value=True)
    config['Option'] = DEFAULT_VAL
    with open(CONFIG_PATH, "w") as f:
        config.write(f)
        log.info("Reset/create config")


# read value from config
def read_config():
    if os.path.exists(CONFIG_PATH):
        # Read config from a file
        config = ConfigParser(allow_no_value=True)
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
        config = ConfigParser(allow_no_value=True)
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
        int(values.get('theme'))
        int(values.get('input_idle'))
        float(values.get('idle'))
        float(values.get('bad_posture'))
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


# check init
def check_key():
    path = [key_file_path, salt_file_path]
    for item in path:
        if not os.path.exists(item):
            return False
    return True


# Filter list
def init_filter():
    with open(app_filter_list, 'w') as json_file:
        filter_set = list(filter_list)
        dump(filter_set, json_file, indent=4)
        log.info("Filter list created")


def read_filter():
    with open(app_filter_list, 'r') as json_file:
        loaded_list = load(json_file)
        log.info("Filter list read")
    return loaded_list


def retrieve_filter():
    var = []
    try:
        if os.path.exists(app_filter_list):
            var = read_filter()
        else:
            log.warning("Filter list not found")
            init_filter()
            var = read_filter()

    except Exception as e:
        log.warning("Filter list: " + str(e))
        init_filter()
        var = read_filter()
    return var
