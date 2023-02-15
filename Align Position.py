import time as t
import threading as trd
import tkinter
from os import path

import customtkinter
from PIL.Image import open
from pystray import Menu, Icon, MenuItem
from plyer import notification as n

import AppTopLevel as at
import FaceDistanceMeasurement as fm
import SettingTopLevel as st
import TimerTopLevel as tt
import initialize as i

# Initialize
# counter: use to initialize distance thread
counter = 0
# counter_thread: use to initialize memo(scoreboard) thread
counter_thread = 0
# use to stop memo thread
condition = True
# get available camera
available_camera = i.get_available_cameras()
# condition for on top function
switch = 0
# App logo
image = open("Resources/logo.ico")
# To reset scoreboard
d = 'Distance: 0'
u = 'Use Time(s): 0'
tut = 'Total Use Time(s): 0'


# thread to update scoreboard
def threading(distance_label, use_time_label, total_use_time_label):
    var = i.get_val().get('Speed')
    while condition:
        distance_label.configure(text='Distance: ' + str(fm.object_distance))
        use_time_label.configure(text='Use Time(s): ' + str(fm.use_time))
        total_use_time_label.configure(text='Total Use Time(s): ' + str(fm.temp_time))
        t.sleep(var)


# main program
class App(tkinter.Tk):

    def __init__(self):
        super().__init__()
        # Window appearance
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.geometry(f"{320}x{200}")
        self.title("Align Position")
        self.iconbitmap('Resources/logo.ico')

        # call init function
        self.init()

        # Window GUI
        main = customtkinter.CTkFrame(self, corner_radius=0)
        main.pack(fill="both", expand=True)

        # Window Grid
        frame = customtkinter.CTkFrame(master=main, corner_radius=0)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)
        frame.grid(sticky='nsew', padx=5, pady=5)

        # Detect button
        self.detect = customtkinter.CTkButton(master=frame, command=lambda: self.start_detection(),
                                              text='Start Detection')
        self.detect.grid(column=0, row=0, padx=5, pady=5)

        # Camera List Option Menu
        camera_list = customtkinter.StringVar(value=available_camera[i.get_val().get('Camera')])
        combobox = customtkinter.CTkOptionMenu(master=frame,
                                               values=[*list(available_camera.values())],
                                               command=self.camera_list_callback,
                                               variable=camera_list)
        combobox.grid(column=0, row=1, padx=5, pady=5)

        # Detect setting: Calibrate camera focal length
        detect_setting = customtkinter.CTkButton(master=frame,
                                                 command=lambda: st.create_toplevel(self),
                                                 text='Detection Setting')
        detect_setting.grid(column=0, row=2, padx=5, pady=5)

        # Personalize setting: sensitivity setting
        personalize_setting = customtkinter.CTkButton(master=frame,
                                                      command=lambda: tt.create_toplevel(main),
                                                      text='Customization Setting')
        personalize_setting.grid(column=0, row=3, padx=5, pady=5)

        # App behaviour setting
        app_setting = customtkinter.CTkButton(master=frame,
                                              command=lambda: at.create_toplevel(frame),
                                              text='App Setting')
        app_setting.grid(column=0, row=4, padx=5, pady=5)

        # Scoreboard
        self.distance_label = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                                     text=d)
        self.distance_label.grid(column=1, row=0, padx=5, pady=5)

        self.use_time_label = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                                     text=u)
        self.use_time_label.grid(column=1, row=1, padx=5, pady=5)
        self.tt_use_time_label = customtkinter.CTkLabel(master=frame, justify=tkinter.LEFT,
                                                        text=tut)
        self.tt_use_time_label.grid(column=1, row=2, padx=5, pady=5)
        self.distance = [trd.Thread(target=fm.distance_measure, name='dc')]
        self.memo = [trd.Thread(target=threading, name='memo',
                                args=(self.distance_label, self.use_time_label, self.tt_use_time_label))]

        # Reset scoreboard button
        self.rst_status = customtkinter.CTkButton(master=frame,
                                                  command=self.reset_status,
                                                  text='Reset')

        # Stay on top checkbox
        self.rst_status.grid(column=1, row=3, padx=5, pady=5)
        on_top = customtkinter.CTkCheckBox(master=frame,
                                           command=self.change_focus,
                                           text='Stay On Top')
        on_top.grid(column=1, row=4, padx=5, pady=5)

        # Exit window
        self.protocol('WM_DELETE_WINDOW', self.quit_window)
        self.mainloop()

    # Initialize: check existed of config file
    def init(self):
        # If program already running then close program
        if i.check_process():
            if path.isfile('config.txt'):
                i.get_val()
            else:
                i.create_config()
        else:
            self.destroy()

    # Exit window function
    def quit_window(self):
        global condition, counter_thread
        var = i.get_val()
        # Initialize system tray
        system_icon = Icon("AlignPosition", image, menu=Menu(
            MenuItem("Show", self.show_window, default=True),
            MenuItem("Detection", self.start_detection),
            MenuItem("Exit", self.exit_app)
        ))
        # If background running is allowed
        if var.get('Background'):
            # Then stop scoreboard update (since it will cause the program freeze if not end the thread)
            if self.memo[counter_thread].is_alive():
                condition = False
                # Create new thread for memo
                self.memo.append(trd.Thread(target=threading, name='memo',
                                            args=(self.distance_label, self.use_time_label, self.tt_use_time_label)))
                self.memo[counter_thread].join(timeout=5)
                counter_thread += 1
            # If user is first time use the app
            if var.get('Init'):
                var['Init'] = False
                i.save_value(str(var))
                # Then show notification
                n.notify(
                    app_name="Align Position",
                    title="Working Background",
                    message="I'm Still working in background!",
                    app_icon='Resources/logo.ico',
                    timeout=5,
                )
            self.withdraw()
            system_icon.run()
        else:
            self.exit_app(system_icon)

    # Camera option menu callback
    def camera_list_callback(self, choice):
        values = i.get_val()
        values['Camera'] = (list(available_camera.keys()))[(list(available_camera.values())).index(choice)]
        i.save_value(str(values))
        if self.distance[counter].is_alive() or self.memo[counter_thread].is_alive():
            self.start_detection()

    # Show window if hide
    def show_window(self, icon):
        global condition
        if self.distance[counter].is_alive():
            condition = True
            self.memo[counter_thread].start()
        self.deiconify()
        icon.stop()

    # Exit app function
    def exit_app(self, system_icon):
        global condition
        # BUG
        if self.memo[counter_thread].is_alive():
            condition = False
            self.memo[counter_thread].join()
        if self.distance[counter].is_alive():
            fm.condition = False
            self.distance[counter].join()
        try:
            system_icon.stop()
        finally:
            self.destroy()

    # Detection button callback
    def start_detection(self):
        global counter, counter_thread, condition
        fm.rest_timer = 0
        if self.distance[counter].is_alive() or self.memo[counter_thread].is_alive():
            self.rst_status.configure(state=tkinter.NORMAL)
            fm.condition = False
            condition = False
            self.detect.configure(text='Start Detection')
            self.distance.append(trd.Thread(target=fm.distance_measure, name='dc'))
            self.memo.append(trd.Thread(target=threading, name='memo',
                                        args=(self.distance_label, self.use_time_label, self.tt_use_time_label)))
            self.memo[counter_thread].join()
            self.distance[counter].join()
            self.reset_scoreboard()
            counter += 1
            counter_thread += 1
        else:
            self.rst_status.configure(state=tkinter.DISABLED)
            fm.condition = True
            condition = True
            self.distance[counter].start()
            self.memo[counter_thread].start()
            self.detect.configure(text='Stop Detection')

    # Reset when stop detection
    def reset_scoreboard(self):
        self.distance_label.configure(text=d)
        fm.use_time = 0

    # Reset by user click
    def reset_status(self):
        fm.total_time = 0
        fm.temp_time = 0
        fm.rest_timer = 0
        self.reset_scoreboard()
        self.tt_use_time_label.configure(text=tut)
        self.use_time_label.configure(text=u)

    # On top function
    def change_focus(self):
        global switch
        if switch == 0:
            self.wm_attributes("-topmost", 1)
            switch = 1
        else:
            self.wm_attributes("-topmost", 0)
            switch = 0


App()
