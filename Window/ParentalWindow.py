import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from Funtionality.Config import desktop_path
from ParentalControl.Auth import read_table_data
from ParentalControl.Backup_Restore import zip_files, extract_zip
from Window.ui_ParentalSetting import Ui_Dialog
from Funtionality.Config import get_config
from Funtionality.UpdateConfig import write_config


class ParentalDialog(QDialog, Ui_Dialog):

    def __init__(self, parent):
        super().__init__()
        self.values = None
        self.parent = parent
        self.setupUi(self)
        self.changePIN_btn.clicked.connect(self.change_pin_page)
        self.exct_data_btn.clicked.connect(self.extract_data)
        self.restore_btn.clicked.connect(self.restore_data)
        self.reset_parental_btn.clicked.connect(self.reset_parental_settings)
        self.monitor_setting_box.toggled.connect(self.monitor_state_change)

    def change_pin_page(self):
        self.parent.cont_stackedwidget.setCurrentIndex(3)  # Set to Authorize page
        self.parent.PIN_stackedwidget.setCurrentIndex(0)  # Set to change psw page
        self.hide()

    def extract_data(self):
        path = os.path.join(desktop_path, "Use_Time_Extract.zip")
        zip_files(path)
        QMessageBox.information(self, "Success", f"Use time extract to {path}")
        self.hide()

    def restore_data(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle('Warning')
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText('This action will overwrite the exist data\nDo you wish to continue?')
        msgbox.addButton('Yes', QMessageBox.YesRole)
        msgbox.addButton('No', QMessageBox.NoRole)
        result = msgbox.exec()
        if result == 0:
            file_path, type = QFileDialog.getOpenFileName(self, "Open File", "", "(*.zip)")
            if file_path != "":
                try:
                    extract_zip(file_path)
                    data = read_table_data()
                    self.parent.reinit_parental_table()
                    if data and data[1]:
                        self.parent.start_parental_control_thread()
                    QMessageBox.information(self, "Success", "Data restored successfully")
                except Exception as e:
                    QMessageBox.warning(self, "Failed", f"{str(e)}")
        self.hide()

    def reset_parental_settings(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle('Warning')
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText('This action remove and reset all you parental control settings\nDo you wish to continue?')
        msgbox.addButton('Yes', QMessageBox.YesRole)
        msgbox.addButton('No', QMessageBox.NoRole)
        result = msgbox.exec()

        if result == 0:
            self.parent.w3_authorize_lock = True
            self.parent.request = "reset_parental_settings"
            self.parent.show_authorize_win()
            self.hide()

    def init_btn(self):
        self.values = get_config()
        if self.values.get('monitoring') == "True":
            self.monitor_setting_box.setText("Monitor activated")
            self.monitor_setting_box.setChecked(True)
        else:
            self.monitor_setting_box.setText("Monitor deactivated")
            self.monitor_setting_box.setChecked(False)

    def monitor_state_change(self, state):
        if state:
            self.values['monitoring'] = "True"
            write_config(self.values)
        else:
            data = None
            try:
                data = read_table_data()
            except Exception as e:
                QMessageBox.warning(self, "Warning", f"{e}")
            if data and data[1]:
                if self.values.get('monitoring') != "True":
                    self.values['monitoring'] = "True"
                    self.monitor_setting_box.setText("Monitor activated")
                    self.monitor_setting_box.setChecked(True)
                    write_config(self.values)
                QMessageBox.warning(self, "Warning", "The parental control is active, monitoring cannot be disable")
            else:
                self.values['monitoring'] = "False"
                self.monitor_setting_box.setText("Monitor deactivated")
                write_config(self.values)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
