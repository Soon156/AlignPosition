import time
from datetime import date
import psutil
import win32process
import win32api
import win32gui

from Funtionality.EncryptData import read_app_use_time, write_app_use_time

condition = True  # To control thread
current_date = str(date.today())


def update_condition():
    global condition
    condition = False


def tracking():
    active_time = 0
    usage_time_for_specific_date = {}
    app_use_times = read_app_use_time()
    specific_date = str(date.today())

    # Access the app usage data for the specific date
    if specific_date in app_use_times:
        usage_time_for_specific_date = app_use_times[specific_date]

    while condition:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
        try:
            p = psutil.Process(pid)
            ExecutablePath = p.exe()
            langs = win32api.GetFileVersionInfo(ExecutablePath, r'\VarFileInfo\Translation')
            key = r'StringFileInfo\%04x%04x\FileDescription' % (langs[0][0], langs[0][1])
            app_name = (win32api.GetFileVersionInfo(ExecutablePath, key))
            start_time = time.time()
            if app_name != 'Windows Explorer' and app_name != 'Align Position':
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



'''
# Track Use Time
def computer_time(rest_time):
    global rest_timer
    rest = use_time - rest_timer
    if rest >= (rest_time * 60):
        active_notification(1)
        rest_timer = use_time'''
