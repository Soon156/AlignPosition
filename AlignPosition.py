import sys
import threading
from datetime import datetime

from PySide6 import QtWidgets
from Funtionality.ErrorMessage import WarningMessageBox
from ParentalControl.AppUseTime import tracking
from ParentalControl.Auth import retrieve_table_data
from PostureRecognize.ElapsedTime import read_elapsed_time_data
from Window.Authorize import PINDialog
from Window.main import MainWindow
from Funtionality import Config

if __name__ == '__main__':

    if not Config.check_process():
        state = False
        cond = False
        data = retrieve_table_data()
        use_time = read_elapsed_time_data()
        limit_time = data[0]
        limit_time_in_sec = limit_time * 60 * 60
        current_date = datetime.now()
        current_hour = current_date.hour
        day_of_week_int = current_date.weekday()
        print(data[1])
        if data and not data[1]:
            for day, hour in data[2:]:
                if day == day_of_week_int:
                    if hour == current_hour:
                        cond = True
            if limit_time != 24 and use_time > limit_time_in_sec:
                cond = True
            else:
                state = True
        else:
            state = True

        if cond:
            app = QtWidgets.QApplication(sys.argv)
            window = PINDialog()
            window.show()
            app.exec()

        if state:
            # Create the application instance
            app = QtWidgets.QApplication(sys.argv)

            Config.get_config()
            Config.clear_log()

            values = Config.get_config()
            if values['app_tracking'] == "True":
                use_time = threading.Thread(target=tracking)
                use_time.start()

            # Create the main window
            window = MainWindow()
            window.setScreen(app.primaryScreen())
            window.show()

            # Start the event loop
            app.exec()
    else:
        app = QtWidgets.QApplication(sys.argv)
        title = "Warning"
        hint = "The 'Align Position' process is already running."
        error = "Application Running"
        widget = WarningMessageBox(title, hint, error)
