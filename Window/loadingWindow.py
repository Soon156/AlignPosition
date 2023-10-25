from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout

from Funtionality.Config import check_logo, check_model, check_process, clear_log, check_key, get_config, \
    retrieve_filter
from Funtionality.ErrorMessage import WarningMessageBox
from Funtionality.UpdateConfig import tracking_app_use_time
from Window.main import MainWindow


class GifAnimationDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.resize(300, 100)
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet("""
                        background-color: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 rgb(26, 16, 57), stop:0.5 rgb(41, 14, 47), stop:1 rgb(26, 16, 57));
                """)

        self.title_label = QLabel(self)
        self.title_label.setPixmap(QPixmap(u":/icon/new-title-resize.png"))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.movie = QMovie(u":/icon/ezgif.com-gif-maker.gif")
        self.gif_label = QLabel(self)
        self.gif_label.setMovie(self.movie)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.movie.start()

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.gif_label)
        self.background = False
        self.show()
        self.check_condition()

    def check_condition(self):

        values = get_config()
        if check_logo() and check_model():
            if not check_process():
                try:
                    get_config()
                    retrieve_filter()
                    clear_log()
                except Exception as e:  # warning when file in use
                    title = "Warning"
                    hint = str(e)
                    error = "Something Wrong"
                    WarningMessageBox(title, hint, error)

                if values['app_tracking'] == "True" and check_key():
                    tracking_app_use_time()

                window = MainWindow()
                window.setScreen(self.screen())

                if self.background:
                    window.hide()
                else:
                    window.show()

            else:
                title = "Warning"
                hint = "The 'Align Position' process is already running."
                error = "Application Running"
                WarningMessageBox(title, hint, error)
        else:
            title = "Error"
            hint = "Missing Critical Resources, please reinstall the application"
            error = "File Not Found"
            WarningMessageBox(title, hint, error)

        self.close()

    def check_background(self, background):
        self.background = background
