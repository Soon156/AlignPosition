import ctypes
import win32con
import win32gui
from Funtionality import Config
import logging as log
from PySide6.QtCore import Signal, QThread, QObject

event = None
condition = True

def reset_event():
    global event
    event = None


class SendSignal(QObject):
    # Define a signal with specific parameters (if needed)
    win_event = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        if event is not None:
            self.win_event.emit(event)
            reset_event()


check_signal = SendSignal()


class CheckEvent(QThread):
    def __init__(self):
        super().__init__()
        self.power_handler = PowerBroadcastHandler()

    def run(self):
        self.power_handler.start()

    def stop(self):
        self.power_handler.stop()
        while condition:
            pass
        log.info("Exit window event handler")


def power_broadcast_handler(hwnd, msg, wparam, lparam):
    global event
    event_type = wparam

    if event_type == win32con.PBT_APMSUSPEND:
        log.info("System is suspending (going to sleep)...")
        event = "sleep"
    elif event_type == win32con.PBT_APMRESUMESUSPEND:
        log.info("System has resumed from suspend (woke up from sleep)...")
        event = "return"
    elif event_type == win32con.PBT_APMSTANDBY:
        log.info("System is entering standby (going to hibernate)...")
        event = "sleep"
    elif event_type == win32con.PBT_APMRESUMESTANDBY:
        log.info("System has resumed from standby (woke up from hibernate)...")
        event = "return"
    elif event_type == win32con.PBT_APMBATTERYLOW:
        event = "Battery is low..."
    elif event_type == win32con.PBT_APMPOWERSTATUSCHANGE:
        event = "Power status has changed..."
    elif event_type == win32con.PBT_APMQUERYSUSPEND:
        event = "sleep"

    if event == "sleep":
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000001)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
    check_signal.run()

    return True


# Define the callback function to handle the WM_QUERYENDSESSION message
def query_end_session_handler(hwnd, msg, wparam, lparam):
    global event
    log.info("System is shutting down...")
    event = "shutdown"
    ctypes.windll.advapi32.AbortSystemShutdownW(None)
    print("shutdown Aboard")
    return True


# Register the power broadcast and query end session handlers
class PowerBroadcastHandler:
    def __init__(self):
        self.is_running = True
        self.hwnd = None
        self.message_map = {
            win32con.WM_POWERBROADCAST: power_broadcast_handler,
            win32con.WM_QUERYENDSESSION: query_end_session_handler,
        }

    def start(self):
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self.message_map
        wc.lpszClassName = "PowerBroadcastHandlerClass"
        wc.style = win32con.WS_EX_TOOLWINDOW  # Add this line to set the window style
        hinst = wc.hInstance = win32gui.GetModuleHandle(None)
        self.classAtom = win32gui.RegisterClass(wc)
        self.hwnd = win32gui.CreateWindowEx(
            win32con.WS_EX_TOOLWINDOW,  # Use the WS_EX_TOOLWINDOW style
            self.classAtom, "Window", 0, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
            0, 0, hinst, None
        )
        win32gui.InitCommonControls()
        while self.is_running:
            try:
                win32gui.PumpWaitingMessages()
            except Exception as e:
                log.error(f"Error in PumpWaitingMessages: {e}")

    def stop(self):
        global condition
        self.is_running = False
        try:
            if self.hwnd:
                win32gui.DestroyWindow(self.hwnd)
                win32gui.UnregisterClass(self.classAtom, None)
        except Exception as e:
            log.warning("Window handler: " + str(e))
            pass
        condition = False
