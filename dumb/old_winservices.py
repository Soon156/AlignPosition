import subprocess
import logging as log
import winreg
import win32serviceutil
import win32service
import servicemanager
from Funtionality.Config import check_process, exe_path, parental_monitoring
from ParentalControl.Auth import read_table_data


class SimpleService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'AlignPositionService'
    _svc_display_name_ = 'Align Position Service'
    _svc_description_ = 'Parental control module for Align Position'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.is_running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.is_running = False
        log.info("Parental control services stop by request")

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        log.info("Services Start")
        parental_monitoring(value=1)
        self.main()

    def main(self):
        while self.is_running:
            if not check_process():
                data = read_table_data()
                if len(data) > 1 and data[1]:
                    try:
                        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\Align Position") as registry_key:
                            value, _ = winreg.QueryValueEx(registry_key, "Parental State")
                    except Exception:
                        value = 0
                    if value == "1":
                        try:
                            subprocess.Popen(exe_path)
                            log.info("Align Position start by parental services")
                        except Exception:
                            pass
                        # time.sleep(30)
                    else:
                        self.SvcStop()
            else:
                log.debug("Process is running")
                # time.sleep(5)
        log.info("Parental control services stopped")


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(SimpleService)
