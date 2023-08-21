import threading
import time
import logging as log
from datetime import datetime
from PySide6.QtCore import QThread
from Funtionality.Config import get_config
from Funtionality.Notification import show_control, reset_signal
from ParentalControl.Auth import retrieve_table_data


class ParentalTracking(QThread):
    cond_usetime = True

    def __init__(self):
        super().__init__()
        self.current_day = datetime.now().weekday()
        self.current_time = datetime.now().time()
        self.values = get_config()
        self.data = retrieve_table_data()
        self.state = False  # To control the notification not spam
        self.total_time_state = False  # To control the total time notification
        self.start_time = time.time()  # Time to reset notification state
        self.thread = None

    def stop_parental_thread(self):
        self.cond_usetime = False

    def update_table_data(self):
        self.data = retrieve_table_data()
        self.total_time_state = False
        self.state = False

    def run(self):
        log.info("Parental tracking start")
        print(self.cond_usetime)
        while self.cond_usetime:
            time.sleep(1)
            # Check total use time
            limit_time = self.data[0]
            limit_time_in_sec = limit_time * 60 * 60
            use_time = self.parent().latest_usetime

            # CHECKME need avoid crash on 2 notification
            # Check limit use time
            if limit_time != 24 and use_time > limit_time_in_sec and not self.total_time_state:
                self.thread = threading.Thread(target=show_control)
                self.thread.start()
                self.total_time_state = True
            # Check the computer access time
            if (self.current_day, self.current_time.hour) in self.data[2:] and not self.state:
                self.thread = threading.Thread(target=show_control)
                self.thread.start()
                self.state = True

            # Re-enable the notification after an hour
            if time.time() - self.start_time > 3600:
                self.start_time = time.time()
                self.state = False

            # Show PIN dialog to cancel operation
            if cancel_signal:  # FIXME replacement
                self.parent().w2.show()
                reset_signal()

        log.info("Parental tracking stop")
