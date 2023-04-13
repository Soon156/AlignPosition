from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk
from Config import create_config, get_config, write_config

# COLORS
APP_BACKGROUND_COLOR = '#1FC3B7'  # LIGHT GREEN

# TEXT STYLE
TITLE_TEXT_SIZE = 26
TEXT_SIZE = 18
SMALL_TEXT = 12
TEXT_COLOR = '#ffffff'  # WHITE
SYNC_TEXT_COLOR = '#0F615B'  # DARK GREEN
BUTTON_COLOR = '#0F615B'
FONT = 'Calibri'

PSW_HASH = "hash.txt"

def change_title_bar_color(self):
    HWND = windll.user32.GetParent(self.winfo_id())
    DWMWA_ATTRIBUTE = 35
    COLOR = 0x005B610F
    windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))


class SettingsTopLevel(ctk.CTkToplevel):

    def __init__(self):
        # window setup
        super().__init__(fg_color=APP_BACKGROUND_COLOR)
        self.title('Align Position')
        self.iconbitmap("./Resources/logo.ico")
        self.geometry('300x300')
        self.resizable(False, False)
        self.grab_set()
        change_title_bar_color(self)

        # Widget
        SettingsButton(self)

        self.mainloop()


class SettingsButton(ctk.CTkFrame):
    def __init__(self, parent):
        # window setup
        super().__init__(master=parent, fg_color=APP_BACKGROUND_COLOR)

        self.background_btn = ctk.CTkButton(master=self, command=self.background_switch,
                                            text='Background')
        self.update_background()
        self.background_btn.grid(column=0, row=0, sticky='nsew', pady=20)

        self.notification_button = ctk.CTkButton(master=self,
                                                 command=self.notification_switch,
                                                 text='Notification')
        self.update_notification()
        self.notification_button.grid(column=0, row=1, sticky='nsew', pady=20)

        reset_setting = ctk.CTkButton(master=self, command=create_config, text='Reset Config')
        reset_setting.grid(column=0, row=2, sticky='nsew', pady=20)

        self.pack(pady=20)

    # Allow app to run background
    def background_switch(self):
        values = get_config()
        if values['background'] == 'True':
            values['background'] = False
        else:
            values['background'] = True
        write_config(str(values))
        self.update_background()

    # Allow app to notify user
    def notification_switch(self):
        values = get_config()
        if values['notifications'] == 'True':
            values['notifications'] = False
        else:
            values['notifications'] = True
        write_config(str(values))
        self.update_notification()

    # Update GUI
    def update_background(self):
        values = get_config()
        if values['background'] == 'True':
            self.background_btn.configure(text='Deactivate Background')
        else:
            self.background_btn.configure(text='Activate Background')

    # Update GUI
    def update_notification(self):
        values = get_config()
        if values['notifications'] == 'True':
            self.notification_button.configure(text='Close Notification')
        else:
            self.notification_button.configure(text='Open Notification')
