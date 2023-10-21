import subprocess
import time
import winreg
import win32serviceutil
import win32service
import servicemanager
from Funtionality.Config import check_process, exe_path
from ParentalControl.Auth import read_table_data


class SimpleService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'AlignPositionService'
    _svc_display_name_ = 'Align Position Service'
    _svc_description_ = 'Parental control module for Align Position'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.is_running = True
        self.last_check_time = time.time()
        self.check_interval = 60

    def SvcStop(self):
        self.is_running = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, "Services Start"))

    def main(self):
        while self.is_running:
            try:
                current_time = time.time()
                if current_time - self.last_check_time >= self.check_interval:
                    self.last_check_time = current_time  # Update the last check time
                    if not check_process():
                        data = read_table_data()
                        if data is not None and data[1]:
                            try:
                                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\Align Position") as registry_key:
                                    value, _ = winreg.QueryValueEx(registry_key, "Parental State")
                            except Exception:
                                value = "0"
                            if value == "1":
                                try:
                                    subprocess.Popen(exe_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                                except Exception:
                                    pass
            except Exception as e:
                servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                                      0,
                                      (self._svc_name_, str(e)))


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(SimpleService)
