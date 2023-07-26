import os
import time
import logging as log
import zroya
from Funtionality.Config import abs_logo_path
from PostureRecognize.ElapsedTime import save_elapsed_time_data


status = zroya.init(
    app_name="AlignPosition",
    company_name="None",
    product_name="AlignPosition",
    sub_product="None",
    version="v01"
)

log.debug("zroya init: " + str(status))

callback = None
condition = False
sleep_time = 30
shutdown_time = 30
clear_time = 10000  # millisecond
logo = abs_logo_path
notify = None
elapsed_time = 0

first_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
first_notify.setFirstLine("Hi There~")
first_notify.setSecondLine("Your program now is run in background!")
first_notify.setImage(logo)
first_notify.setExpiration(clear_time)

break_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
break_notify.setFirstLine("It's Break Time!!!")
break_notify.setSecondLine("Take a coffee break in a busy day!")
break_notify.setImage(logo)
break_notify.addAction("Sleep")
break_notify.addAction("Shutdown")
break_notify.setExpiration(clear_time)

sleep_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
sleep_notify.setFirstLine("Sleep")
sleep_notify.setSecondLine("Your computer will be sleep in " + str(sleep_time) + " seconds!")
sleep_notify.setImage(logo)
sleep_notify.addAction("Cancel")
break_notify.setExpiration(clear_time)

shutdown_notify = zroya.Template(zroya.TemplateType.ImageAndText2)
shutdown_notify.setFirstLine("Shutdown")
shutdown_notify.setSecondLine("Your computer will be shutdown in " + str(shutdown_time) + " seconds")
shutdown_notify.setImage(logo)
shutdown_notify.addAction("Cancel")
shutdown_notify.setExpiration(clear_time)


def set_elapsed_time(shared_elapsed_time):
    global elapsed_time
    elapsed_time = shared_elapsed_time


def cancel_handler():
    log.info("Cancel operation shutdown/sleep")
    global condition
    condition = False


def callback_handler(nid, action_id):
    global callback, condition
    if action_id == 0:
        log.info("Sleep confirm")
        condition = True
        callback = "Sleep"
        zroya.show(sleep_notify, on_action=cancel_handler)
    else:
        log.info("Shutdown confirm")
        condition = True
        callback = "Shutdown"
        zroya.show(shutdown_notify, on_action=cancel_handler)


def show_break():
    global condition, callback
    start_time = time.time()
    zroya.show(break_notify, on_action=callback_handler)
    while True:
        if callback == "Sleep":
            callback = None
            time.sleep(sleep_time)
            if condition:
                condition = False
                log.info("System Sleep")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break
        if callback == "Shutdown":
            callback = None
            time.sleep(shutdown_time)
            if condition:
                condition = False
                log.info("System Shutdown")
                save_elapsed_time_data(elapsed_time)
                os.system("shutdown /s /t 0")
                break
            break
        if time.time() - start_time >= clear_time or notify:
            break


'''
# Notification list
def active_notification(value):
    values = i.get_val()
    if values.get('notifications') == 'True':
        if value == 0:
            notification.title = "Detection Start!"
            notification.message = "Monitoring your health from now!"
            notification.send(block=False)
        elif value == 1:
            notification.title = "Take a break!"
            notification.message = "You already use computer for a long time"
            notification.send(block=False)
        elif value == 2:
            notification.title = "Sit Properly!"
            notification.message = "Keep your position right"
            notification.send(block=False)
        else:
            notification.title = "Something Wrong..."
            notification.message = "This shouldn't happened!"
            notification.send(block=False)
            '''


