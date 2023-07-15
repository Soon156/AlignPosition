import os
import time
from Funtionality.Config import abs_logo_path
import logging as log
import winotify

# instantiate Notifier and Registry class
app_id = "alignposition"
app_path = os.path.abspath(__file__)

r = winotify.Registry(app_id, winotify.PYW_EXE, app_path, force_override=True)
callback = None
condition = False
notifier_thread = None
sleep_time = 30
shutdown_time = 30
clear_time = 5
notify = None

try:
    notifier = winotify.Notifier(r)


    @notifier.register_callback
    def change_condition():
        log.info("Cancel operation shutdown/sleep")
        global condition
        condition = False


    @notifier.register_callback
    def shutdown_callback():
        log.info("Shutdown confirm")
        global callback, condition
        condition = True
        callback = "Shutdown"
        toast = notifier.create_notification("Shutdown",
                                             "Your computer will be shutdown in " + str(shutdown_time) + " seconds",
                                             icon=abs_logo_path, launch=clear)
        toast.add_actions("Cancel", change_condition)
        toast.set_audio(winotify.audio.Mail, loop=True)
        toast.show()


    @notifier.register_callback
    def sleep_callback():
        log.info("Sleep confirm")
        global callback, condition
        condition = True
        callback = "Sleep"
        toast = notifier.create_notification("Sleep", "Your computer will be sleep in " + str(sleep_time) + " seconds!",
                                             icon=abs_logo_path, launch=clear)
        toast.add_actions("Cancel", change_condition)
        toast.set_audio(winotify.audio.Mail, loop=False)
        toast.show()


    @notifier.register_callback
    def clear():
        log.info("Notification Clear")
        notifier.clear()
except Exception as e:
    log.info(f"Message: {e}")
    pass


def break_notification():
    toast = notifier.create_notification("Take a Break", 'Take a coffee break in a busy day!',
                                         icon=abs_logo_path, launch=clear)
    toast.add_actions("Sleep", sleep_callback)
    toast.add_actions("Shutdown", shutdown_callback)
    toast.set_audio(winotify.audio.Default, loop=False)
    toast.show()


def notice_user():
    global notifier_thread
    if notifier_thread is None:
        notifier.start()
        notifier_thread = True

    start_time = time.time()
    break_notification()

    while True:
        notifier.update()
        if callback == "Sleep":
            time.sleep(sleep_time)
            if condition:
                log.info("System Sleep")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break
        if callback == "Shutdown":
            time.sleep(shutdown_time)
            if condition:
                log.info("System Shutdown")
                os.system("shutdown /s /t 0")
                break
            break
        if time.time() - start_time >= clear_time or notify:
            clear()
            break


def first_time():
    toast = notifier.create_notification("Hi There~", 'Your program now is run in background!',
                                         icon=abs_logo_path, launch=clear)
    toast.set_audio(winotify.audio.Default, loop=False)
    toast.show()


def stop_notification():
    global notify
    notify = True


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
