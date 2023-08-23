import ast
import configparser
import logging as log
import threading
import winreg

from Funtionality.Config import key_path, app_name, exe_path, CONFIG_PATH, check_key
from ParentalControl.AppUseTime import Tracking

tracking_instance = Tracking()
use_time = threading.Thread(target=tracking_instance.run)


def tracking_app_use_time():
    try:
        use_time.start()
    except RuntimeError:
        log.warning("App time tracking ald start")


def stop_tracking():
    try:
        tracking_instance.update_condition()
        use_time.join()
    except RuntimeError:
        log.warning("App time tracking ald stop")


def write_config(dictionary_str):  # TODO change to services
    if dictionary_str["auto"] == "True":
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        log.info("Auto-start Enable")
        pass
    else:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
                winreg.DeleteValue(key, app_name)
        except FileNotFoundError:
            pass
        log.info("Auto-start Disable")
    if dictionary_str['app_tracking'] == "True":
        tracking_app_use_time()
    else:
        stop_tracking()
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(CONFIG_PATH)
    config.optionxform = str
    config['Option'] = ast.literal_eval(str(dictionary_str))
    with open(CONFIG_PATH, "w") as f:
        config.write(f)
        log.info("Config updated")
