import os
import sys
import time
import logging as log
import zroya
from PySide6 import QtWidgets

from Funtionality.Config import abs_logo_path
from Funtionality.ErrorMessage import WarningMessageBox
from Window.Authorize_2 import PINDialog2, get_condition, change_condition

status = zroya.init(
    app_name="AlignPosition",
    company_name="None",
    product_name="AlignPosition",
    sub_product="None",
    version="v01"
)

log.debug("zroya init: " + str(status))

callback = None
sleep_time = 300
shutdown_time = 30
clear_time = 10000  # millisecond
logo = abs_logo_path
notify = None
elapsed_time = 0

try:
    first_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
    first_notify.setFirstLine("Hi There~")
    first_notify.setSecondLine("Your program now is run in background!")
    first_notify.setExpiration(clear_time)

    break_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
    break_notify.setFirstLine("It's Break Time!!!")
    break_notify.setSecondLine("Take a coffee break in a busy day!")
    break_notify.setExpiration(clear_time)

    sleep_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
    sleep_notify.setFirstLine("Over Today Usetime")
    sleep_notify.setSecondLine("Your computer will be sleep in " + str(sleep_time) + " seconds!")
    # sleep_notify.setImage(logo)
    sleep_notify.addAction("Cancel")

except Exception as e:
    app = QtWidgets.QApplication(sys.argv)
    title = "Error"
    hint = "Missing Icon Resources, reinstall the application"
    error = "File Not Found"
    widget = WarningMessageBox(title, hint, error)
    sys.exit()


def set_elapsed_time(shared_elapsed_time):
    global elapsed_time
    elapsed_time = shared_elapsed_time


def cancel_handler():
    window = PINDialog2()
    window.exec()


def show_control():
    global condition, callback
    start_time = time.time()
    zroya.show(sleep_notify, on_action=cancel_handler)
    while True:
        time.sleep(sleep_time)
        get_condition()
        if condition:
            change_condition()
            log.info("System Sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            break
        if time.time() - start_time >= clear_time or notify:
            break


def show_break():
    zroya.show(break_notify)
