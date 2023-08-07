import time
from datetime import date
import psutil
import win32process
import win32api
import win32gui
import logging as log

from Funtionality.Config import get_config, filter_list
from ParentalControl.Auth import write_app_use_time, read_app_use_time

condition = True  # To control thread
current_date = str(date.today())


def update_condition():
    global condition
    condition = False


def tracking():
    log.info("App use time tracking start")
    active_time = 0
    usage_time_for_specific_date = {}
    app_use_times = read_app_use_time()
    specific_date = str(date.today())
    values = get_config()
    # Access the app usage data for the specific
    if app_use_times is not None:
        if specific_date in app_use_times:
            usage_time_for_specific_date = app_use_times[specific_date]

    while condition and values['app_tracking'] == "True":
        values = get_config()  # keep track update
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
        try:
            p = psutil.Process(pid)
            ExecutablePath = p.exe()
            langs = win32api.GetFileVersionInfo(ExecutablePath, r'\VarFileInfo\Translation')
            key = r'StringFileInfo\%04x%04x\FileDescription' % (langs[0][0], langs[0][1])
            app_name = (win32api.GetFileVersionInfo(ExecutablePath, key))
            start_time = time.time()
            if app_name not in filter_list:
                while pid == win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]:
                    time.sleep(1)
                    active_time = int(time.time() - start_time)
                # Add the new use time to the existing use time for the app
                if app_name in usage_time_for_specific_date:
                    usage_time_for_specific_date[app_name] += active_time
                else:
                    usage_time_for_specific_date[app_name] = active_time
        except Exception:
            pass
    app_use_times[specific_date] = usage_time_for_specific_date
    write_app_use_time(app_use_times)
