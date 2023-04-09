import os.path
import time
from winotify import audio, Registry, PYW_EXE, Notifier

# instantiate Notifier and Registry class
app_id = "align position"
app_path = os.path.abspath(__file__)

r = Registry(app_id, PYW_EXE, app_path, force_override=True)
notifier = Notifier(r)

logo_path = os.getcwd() + "\Resources\logo.ico"

condition1 = False
condition2 = False
condition_sleep = True
condition_shutdown = True

sleep_time = 30
shutdown_time = 30


@notifier.register_callback
def clear():
    notifier.clear()
    print('clear')


@notifier.register_callback
def change_condition():
    global condition_sleep, condition_shutdown
    condition_sleep = False
    condition_shutdown = False


@notifier.register_callback
def sleep_callback():
    global condition1
    toast = notifier.create_notification("Sleep", "Your computer will be sleep in " + str(sleep_time) + " seconds!",
                                         icon=logo_path, launch=clear)
    toast.add_actions("Cancel", change_condition)
    toast.set_audio(audio.Mail, loop=False)
    toast.show()
    condition1 = True


@notifier.register_callback
def shutdown_callback():
    global condition2
    toast = notifier.create_notification("Shutdown",
                                         "Your computer will be shutdown in " + str(shutdown_time) + " seconds",
                                         icon=logo_path, launch=clear)
    toast.add_actions("Cancel", change_condition)
    toast.set_audio(audio.Mail, loop=True)
    toast.show()
    condition2 = True


def break_notification():
    toast = notifier.create_notification("Take a Break", 'Take a coffee break in a busy day!',
                                         icon=logo_path, launch=clear)
    toast.add_actions("Sleep", sleep_callback)
    toast.add_actions("Shutdown", shutdown_callback)
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def notice_user():
    notifier.start()
    start_time = time.time()
    break_notification()

    while True:
        notifier.update()
        time.sleep(1)
        if condition1:
            time.sleep(sleep_time)
            if condition_sleep:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break
        if condition2:
            time.sleep(shutdown_time)
            if condition_shutdown:
                os.system("shutdown /s /t 0")
                break
            break
        if time.time() - start_time >= 10:
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