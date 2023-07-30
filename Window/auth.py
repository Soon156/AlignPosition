import hashlib
import os

from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
import re
from Funtionality.Config import psw_key_path
from UI.ui_Authorize import Ui_Auth_Dialog
import logging as log
from Window.parentalControl import ParentalWindow

# TODO plan to add firebase/TPM for more secure storing


def get_hash(secret):
    sha256 = hashlib.sha256()  # create a new SHA-256 hash object
    sha256.update(secret.encode())  # add some data to the hash object
    digest = sha256.hexdigest()  # get the hex digest of the hash
    return digest


class Authentication(QDialog, Ui_Auth_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = None
        self.setupUi(self)
        self.label_2.hide()
        self.lineEdit.setEchoMode(QLineEdit.Password)
        if os.path.exists(psw_key_path):
            self.check_validation()
            self.pushButton.clicked.connect(self.compare_pin)
        else:
            self.pushButton.clicked.connect(self.new_pin)
            self.label_2.show()
            self.label_2.setText("Create a new PIN")

    def check_validation(self, msg="Hash file has been modified! Reinstall the application."):
        try:
            # open the file in read mode
            with open(psw_key_path, 'r') as file:
                # read the contents of the file
                contents = file.read()
                if re.match('^[a-fA-F0-9]{64}$', contents):
                    return contents
                else:
                    QMessageBox.critical(self, "Error", msg)
                    raise Exception(msg)
        except FileNotFoundError:
            return None

    def compare_pin(self):
        secret = self.lineEdit.text()
        try:
            content = self.check_validation()
            salt = os.path.getctime(psw_key_path)
            if get_hash(str(salt) + secret) == content:
                self.close()
                w = ParentalWindow(self)
                w.exec_()
            else:
                self.label_2.show()
                self.label_2.setText("PIN is not same")
        except FileNotFoundError:
            log.error("Hash file not found! Reinstall the application.")

    def new_pin(self):
        secret = self.lineEdit.text()

        with open(psw_key_path, 'x') as file:
            # write the string to the file
            salt = os.path.getctime(psw_key_path)
            file.write(get_hash(str(salt) + secret))
            # win32api.SetFileAttributes(psw_key_path, win32con.FILE_ATTRIBUTE_HIDDEN)
            os.chmod(psw_key_path, 0o444)
            self.close()
            w = ParentalWindow(self)
            w.exec_()
        log.info("New PIN create")


"""def changePin(secret, new_secret):
    if comparePin(secret):
        tk.messagebox.showinfo(title="Success", message="Your PIN has been change!")
    if os.path.exists(psw_key_path):
        os.chmod(psw_key_path, 0o777)
        os.remove(psw_key_path)"""
