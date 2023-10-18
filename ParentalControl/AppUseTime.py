import time
from datetime import date
import psutil
import win32process
import win32api
import win32gui
import logging as log

from Funtionality.Config import get_config, filter_list
from ParentalControl.Auth import write_app_use_time, read_app_use_time


class Tracking:

    current_date = str(date.today())

    def __init__(self):
        super().__init__()
        self.active_time = 0
        self.app_use_times = read_app_use_time()
        self.specific_date = str(date.today())
        self.usage_time_for_specific_date = {}
        self.values = get_config()
        self.cond_usetime = True

    def update_condition(self):
        self.cond_usetime = False

    def save_app_usetime(self):
        self.app_use_times[self.specific_date] = self.usage_time_for_specific_date
        write_app_use_time(self.app_use_times)

    def run(self):
        log.info("App use time tracking start")
        # Access the app usage data for the specific
        if self.app_use_times is not None:
            if self.specific_date in self.app_use_times:
                self.usage_time_for_specific_date = self.app_use_times[self.specific_date]

        self.cond_usetime = True

        while self.cond_usetime:
            self.values = get_config()  # keep track update
            pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
            try:
                p = psutil.Process(pid)
                ExecutablePath = p.exe()
                langs = win32api.GetFileVersionInfo(ExecutablePath, r'\VarFileInfo\Translation')
                key = r'StringFileInfo\%04x%04x\FileDescription' % (langs[0][0], langs[0][1])
                app_name = (win32api.GetFileVersionInfo(ExecutablePath, key))
                start_time = time.time()
                if app_name not in filter_list and "window" not in app_name.lower():
                    while pid == win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]:
                        time.sleep(1)
                        self.active_time = int(time.time() - start_time)
                    # Add the new use time to the existing use time for the app
                    if app_name in self.usage_time_for_specific_date:
                        self.usage_time_for_specific_date[app_name] += self.active_time
                    else:
                        self.usage_time_for_specific_date[app_name] = self.active_time

                if self.specific_date != str(date.today()):
                    self.save_app_usetime()
                    self.specific_date = str(date.today())

            except Exception:
                pass

        log.info("App use time tracking stop")
        self.save_app_usetime()
