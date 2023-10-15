import sys
import argparse
from PySide6 import QtWidgets
from Funtionality.Config import check_key, check_logo, check_model, get_config, check_process, clear_log
from Funtionality.ErrorMessage import WarningMessageBox
from Funtionality.UpdateConfig import tracking_app_use_time
from Window.main import MainWindow


def main(background):
    values = get_config()

    # Create the application instance
    app = QtWidgets.QApplication(sys.argv)

    if check_logo() and check_model():
        if not check_process():
            get_config()
            clear_log()

            if values['app_tracking'] == "True" and check_key():
                tracking_app_use_time()

            window = MainWindow(background)
            window.setScreen(app.primaryScreen())

            # Start the event loop
            app.exec()
        else:
            title = "Warning"
            hint = "The 'Align Position' process is already running."
            error = "Application Running"
            widget = WarningMessageBox(title, hint, error)
    else:
        title = "Error"
        hint = "Missing Critical Resources, please reinstall the application"
        error = "File Not Found"
        widget = WarningMessageBox(title, hint, error)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enhanced Parental Control and Posture Monitoring Application")
    parser.add_argument("--background", action="store_true", help="Run the application in the background")

    args = parser.parse_args()
    main(args.background)
