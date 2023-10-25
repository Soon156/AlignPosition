from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QSplashScreen


class GifAnimationDialog(QSplashScreen):

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
