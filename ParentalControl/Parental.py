import hashlib
from Settings import *
import win32api
import win32con
import tkinter as tk
from tkinter import ttk
import re
import os


# TODO plan to add firebase/TPM for more secure storing


def getHash(secret):
    sha256 = hashlib.sha256()  # create a new SHA-256 hash object
    sha256.update(secret.encode())  # add some data to the hash object
    digest = sha256.hexdigest()  # get the hex digest of the hash
    return digest


def comparePin(new_secret, *argv):
    try:
        # open the file in read mode
        with open(PSW_HASH, 'r') as file:
            # read the contents of the file
            contents = file.read()
            salt = os.path.getctime(PSW_HASH)
            if re.match('^[a-fA-F0-9]{64}$', contents):
                if getHash(str(salt) + new_secret) == contents:
                    for win in argv:
                        parentalWindow(win)
                    return True
                else:
                    tk.messagebox.showwarning(title="Warning", message="PIN is not same")
            else:
                tk.messagebox.showerror(title="Error",
                                        message="Hash file has been modified! Reinstall the application.")
    except FileNotFoundError:
        tk.messagebox.showerror(title="Error", message="Hash file not found! Reinstall the application.")
    return False


def newPin(secret, *argv):
    if os.path.exists(PSW_HASH):
        os.chmod(PSW_HASH, 0o777)
        os.remove(PSW_HASH)
    with open(PSW_HASH, 'x') as file:
        # write the string to the file
        salt = os.path.getctime(PSW_HASH)
        file.write(getHash(str(salt) + secret))
        win32api.SetFileAttributes(PSW_HASH, win32con.FILE_ATTRIBUTE_HIDDEN)
        os.chmod(PSW_HASH, 0o444)
    tk.messagebox.showinfo(title="Success", message="Your PIN has been save!")
    for win in argv:
        parentalWindow(win)


def changePin(secret, new_secret):
    if comparePin(secret):
        tk.messagebox.showinfo(title="Success", message="Your PIN has been change!")


def parentalWindow(win):
    try:
        win.destroy()
    finally:
        parental_window = ParentalTopLevel()


class NewPinTopLevel(ctk.CTkToplevel):
    def __init__(self):
        # window setup
        super().__init__(fg_color=APP_BACKGROUND_COLOR)
        self.title('Align Position')
        self.after(250, lambda: self.iconbitmap("./Resources/logo.ico"))
        self.geometry('300x300')
        self.resizable(False, False)
        self.grab_set()
        change_title_bar_color(self)
        label = ctk.CTkLabel(master=self, text='Request New Pin')
        label.pack()
        input = tk.Entry(master=self, show='*')
        input.pack()
        button = ctk.CTkButton(master=self, text="OK", command=lambda: newPin(input.get(), self))
        button.pack()


class PinTopLevel(ctk.CTkToplevel):
    def __init__(self):
        # window setup
        super().__init__(fg_color=APP_BACKGROUND_COLOR)
        self.title('Align Position')
        self.after(250, lambda: self.iconbitmap("./Resources/logo.ico"))
        self.geometry('300x300')
        self.resizable(False, False)
        self.grab_set()
        change_title_bar_color(self)
        label = ctk.CTkLabel(master=self, text='Insert Pin')
        label.pack()
        input1 = tk.Entry(master=self, show='*')
        input1.pack()
        button = ctk.CTkButton(master=self, text="OK", command=lambda: comparePin(input1.get(), self))
        button.pack()


class ParentalTopLevel(ctk.CTkToplevel):
    def __init__(self):
        # window setup
        super().__init__(fg_color=APP_BACKGROUND_COLOR)
        self.title('Align Position')
        self.after(250, lambda: self.iconbitmap("./Resources/logo.ico"))
        self.geometry('500x300')
        self.resizable(False, False)
        self.grab_set()
        change_title_bar_color(self)

        # Widgets
        TimeTable(self)

        self.mainloop()


class TimeTable(ctk.CTkFrame):
    def __init__(self, parent):
        # window setup
        super().__init__(master=parent, fg_color='transparent')
        # layout
        self.pack(pady=20)
        # Widgets
        table = ttk.Treeview(master=self, columns=('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'))
        table.heading('mon', text='Monday')
        table.heading('tue', text='Tuesday')
        table.heading('wed', text='Wednesday')
        table.heading('thu', text='Thursday')
        table.heading('fri', text='Friday')
        table.heading('sat', text='Saturday')
        table.heading('sun', text='Sunday')
        table.pack(fill='both', expand=True)
        time = 0
        for i in range(24):
            if i == 0:
                time = 12
            elif i == 1:
                time = 1
            elif i == 13:
                time -= 12
            else:
                time += 1
            time_string = str(time) + "a.m."
            status = "False"
            data = (time, status)
            table.insert(parent='', index=i, values=data)
