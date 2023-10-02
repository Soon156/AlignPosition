import os
import sys
import time
import logging as log
import zroya
from PySide6 import QtWidgets
from Funtionality.ErrorMessage import WarningMessageBox

status = zroya.init(
    app_name="AlignPosition",
    company_name="None",
    product_name="AlignPosition",
    sub_product="None",
    version="v01"
)

log.debug("zroya init: " + str(status))

sleep_time = 300
clear_time = 10000  # millisecond
cancel_signal = False
cancel_condition = True

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
    sleep_notify.addAction("Cancel")

except Exception as e:
    app = QtWidgets.QApplication(sys.argv)
    title = "Error"
    hint = "Missing Icon Resources, reinstall the application"
    error = "File Not Found"
    widget = WarningMessageBox(title, hint, error)


def cancel_handler(nid, action_id):
    print("cancel handler")
    global cancel_signal, cancel_condition
    cancel_signal = True
    cancel_condition = True


def reset_signal():
    global cancel_signal
    cancel_signal = False


def get_signal():
    return cancel_signal


def update_cancel_cond():
    global cancel_condition
    cancel_condition = False
    log.info("Operation sleep cancel")


def show_control():
    zroya.show(sleep_notify, on_action=cancel_handler)
    start_time = time.time()
    time.sleep(10)
    while True:
        if time.time() - start_time >= sleep_time:
            if cancel_condition:
                log.info("System Sleep")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            break


def show_break():
    zroya.show(break_notify)
