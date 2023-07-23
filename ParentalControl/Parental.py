import hashlib
import win32api
import win32con
import tkinter as tk
import re
import os

from Funtionality.Config import psw_key_path


# TODO plan to add firebase/TPM for more secure storing


def getHash(secret):
    sha256 = hashlib.sha256()  # create a new SHA-256 hash object
    sha256.update(secret.encode())  # add some data to the hash object
    digest = sha256.hexdigest()  # get the hex digest of the hash
    return digest


def comparePin(new_secret, *argv):
    try:
        # open the file in read mode
        with open(psw_key_path, 'r') as file:
            # read the contents of the file
            contents = file.read()
            salt = os.path.getctime(psw_key_path)
            if re.match('^[a-fA-F0-9]{64}$', contents):
                if getHash(str(salt) + new_secret) == contents:
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
    if os.path.exists(psw_key_path):
        os.chmod(psw_key_path, 0o777)
        os.remove(psw_key_path)
    with open(psw_key_path, 'x') as file:
        # write the string to the file
        salt = os.path.getctime(psw_key_path)
        file.write(getHash(str(salt) + secret))
        win32api.SetFileAttributes(psw_key_path, win32con.FILE_ATTRIBUTE_HIDDEN)
        os.chmod(psw_key_path, 0o444)
    tk.messagebox.showinfo(title="Success", message="Your PIN has been save!")


def changePin(secret, new_secret):
    if comparePin(secret):
        tk.messagebox.showinfo(title="Success", message="Your PIN has been change!")
