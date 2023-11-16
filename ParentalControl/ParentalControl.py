import threading
import time
import logging as log
from datetime import datetime
from PySide6.QtCore import QThread, Signal
from Funtionality.Config import get_config  # parental_monitoring
from Funtionality.Notification import show_control, reset_signal, get_signal, update_cancel_cond
from ParentalControl.Auth import read_table_data


class ParentalTracking(QThread):
    cond_usetime = True
    cancel = Signal()

    def __init__(self):
        super().__init__()
        self.current_day = datetime.now().weekday()
        self.current_time = datetime.now().time()
        self.values = get_config()
        self.data = read_table_data()
        self.state = False  # To control the notification not spam
        self.total_time_state = False  # To control the total time notification
        self.notify_time = 0  # Time to reset notification state
        self.thread = None
        # parental_monitoring(value=1)

    def stop_parental_thread(self):
        # parental_monitoring(value=0)
        self.cond_usetime = False

    def update_table_data(self):
        self.data = read_table_data()
        self.total_time_state = False
        self.state = False

    def update_time(self):
        if self.current_day != datetime.now().weekday():
            self.total_time_state = False
            self.current_day = datetime.now().weekday()
        self.current_time = datetime.now().time()

    def run(self):
        log.info("Parental tracking start")
        while self.cond_usetime:
            time.sleep(1)
            self.update_time()

            limit_time = self.data[0][self.current_day]
            limit_time_in_sec = limit_time * 60 * 60
            try:
                use_time = self.parent().latest_usetime
            except AttributeError:
                use_time = 0

            # CHECKME need avoid crash on 2 notification
            # Check limit use time
            if limit_time >= 24 and use_time > limit_time_in_sec and not self.total_time_state:
                self.thread = threading.Thread(target=show_control)
                self.thread.start()
                self.total_time_state = True

            # Check the computer access time
            if (self.current_day, self.current_time.hour) in self.data[2] and not self.state:
                self.thread = threading.Thread(target=show_control)
                self.thread.start()
                self.notify_time = time.time()
                self.state = True

            # Re-enable the notification after an hour
            if time.time() - self.notify_time > 3600:
                self.state = False

            cancel_signal = get_signal()
            # Show PIN dialog to cancel operation
            if cancel_signal:
                self.cancel.emit()
                reset_signal()
        update_cancel_cond()
        self.parent().parental_control_thread = False
        log.info("Parental tracking stop")
