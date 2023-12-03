import ast
import configparser
import logging as log
import winreg

from Funtionality.Config import key_path, app_name, exe_path, CONFIG_PATH, b_config
from ParentalControl.AppUseTime import Tracking

tracking_instance = None
tracking_state = False
use_time = None


def tracking_app_use_time():
    global use_time, tracking_instance
    try:
        tracking_instance = Tracking()
        tracking_instance.start()
    except RuntimeError as e:
        log.warning("App time tracking ald start")


def waiting():
    try:
        while tracking_instance.isRunning():
            pass
    except:
        pass


def get_app_tracking_state():
    try:
        return tracking_instance.check_condition()
    except Exception as e:
        return False


def save_usetime():
    tracking_instance.save_app_usetime()


def stop_tracking():
    try:
        tracking_instance.stop_tracking()
        waiting()
    except RuntimeError:
        log.warning("App time tracking ald stop")


def write_config(dictionary_str):
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
        if not get_app_tracking_state():
            tracking_app_use_time()
    else:
        stop_tracking()
    config = configparser.ConfigParser(allow_no_value=True)
    config2 = configparser.ConfigParser(allow_no_value=True)
    config.read(CONFIG_PATH)
    config2.read(b_config)

    try:
        config_dict = dict(config2['Option'])
        if config_dict != dictionary_str:
            config.optionxform = str
            config['Option'] = ast.literal_eval(str(dictionary_str))
            with open(b_config, "w") as f:
                config.write(f)
            with open(CONFIG_PATH, "w") as f:
                config.write(f)
            log.info("Config updated")
        else:
            log.info("No changed in config")
    except:
        config.optionxform = str
        config['Option'] = ast.literal_eval(str(dictionary_str))
        with open(b_config, "w") as f:
            config.write(f)
        with open(CONFIG_PATH, "w") as f:
            config.write(f)
        log.info("Config Saved")
        pass
