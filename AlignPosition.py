import sys
import argparse

from PySide6.QtWidgets import QApplication
from Window.loadingWindow import GifAnimationDialog
import resource_rc


def main(background):
    # Create the application instance
    app = QApplication(sys.argv)
    w = GifAnimationDialog()

    if not background:
        w.show()

    check_condition()

    from Window.main import MainWindow
    window = MainWindow()
    window.setScreen(app.primaryScreen())

    if background:
        window.hide()
    else:
        window.show()

    w.finish(window)
    sys.exit(app.exec())


def check_condition():
    from Funtionality.Config import get_config, check_model, check_process, check_logo, retrieve_filter, clear_log, \
        check_key
    from Funtionality.ErrorMessage import WarningMessageBox
    from Funtionality.UpdateConfig import tracking_app_use_time
    values = get_config()
    if check_logo() and check_model():
        if not check_process():
            try:
                get_config()
                retrieve_filter()
                clear_log()
            except Exception as e:  # warning when file in use
                title = "Warning"
                hint = str(e)
                error = "Something Wrong"
                WarningMessageBox(title, hint, error)

            if values['app_tracking'] == "True" and check_key():
                tracking_app_use_time()

        else:
            title = "Warning"
            hint = "The 'Align Position' process is already running."
            error = "Application Running"
            WarningMessageBox(title, hint, error)
    else:
        title = "Error"
        hint = "Missing Critical Resources, please reinstall the application"
        error = "File Not Found"
        WarningMessageBox(title, hint, error)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enhanced Parental Control and Posture Monitoring Application")
    parser.add_argument("--background", action="store_true", help="Run the application in the background")

    args = parser.parse_args()
    main(args.background)
