from Settings import *
from Parental import NewPinTopLevel, PinTopLevel
import os


def SettingsWindow():
    settingwindow = SettingsTopLevel()


def ParentalWindow():
    if os.path.exists(PSW_HASH):
        parentalwindow = PinTopLevel()
    else:
        pinwindow = NewPinTopLevel()


class App(ctk.CTk):
    def __init__(self):
        # window setup
        super().__init__(fg_color=APP_BACKGROUND_COLOR)
        self.title('Align Position')
        self.iconbitmap("./Resources/logo.ico")
        self.geometry('300x300')
        self.resizable(False, False)
        change_title_bar_color(self)

        # Widget
        MainFrame(self)

        self.mainloop()


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        # layout
        self.pack(pady=20)

        button_detection = ctk.CTkButton(master=self, text='Start Detection')
        button_detection.grid(column=0, row=0, sticky='nsew', pady=20)

        button_parental = ctk.CTkButton(master=self, text='Parental Control', command=ParentalWindow)
        button_parental.grid(column=0, row=1, sticky='nsew', pady=20)

        button_settings = ctk.CTkButton(master=self, text='Settings', command=SettingsWindow)
        button_settings.grid(column=0, row=2, sticky='nsew', pady=20)


if __name__ == '__main__':
    App()
