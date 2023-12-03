from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QSize
from Funtionality.Config import get_config, abs_overlay_pic_path


class OverlayWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.width_geo = None
        self.pos = None
        self.pixmap = None
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.WindowTransparentForInput | Qt.SplashScreen
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.5)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(abs_overlay_pic_path)
        pixmap = pixmap.scaled(QSize(100, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.original_pixmap = pixmap.copy()
        self.win_geometry()

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
        self.animation_group = QParallelAnimationGroup()

        self.state = False

    def show_with_animation(self, target_geometry, duration=300):
        self.clear_animations()
        self.show()
        current_geometry = self.geometry()
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(duration)
        animation.setStartValue(current_geometry)
        animation.setEndValue(target_geometry)
        animation.setEasingCurve(QEasingCurve.OutQuad)  # Set easing curve here
        self.animation_group.addAnimation(animation)
        self.animation_group.start()

    def clear_animations(self):
        for i in range(self.animation_group.animationCount()):
            animation = self.animation_group.animationAt(i)
            self.animation_group.removeAnimation(animation)
            animation.deleteLater()

    def change_state(self, posture):

        if posture == "bad":
            if self.pos == "left":
                self.show_with_animation(QRect(-18, -15, 100, 100))
            else:
                self.show_with_animation(QRect(self.width_geo - 90, -10, 100, 100))
            self.setWindowOpacity(1.0)
            self.state = True
        elif posture == "good":
            if self.state:
                if self.pos == "left":
                    self.show_with_animation(QRect(-30, -30, 100, 100))
                else:
                    self.show_with_animation(QRect(self.width_geo - 80, -30, 100, 100))
                self.state = False
                self.setWindowOpacity(0.5)
        else:
            self.hide()

    def win_geometry(self):
        screen = self.screen().size()
        if screen is not None:
            values = get_config()
            if values['overlay'] == "Left":
                self.width_geo = 0
                self.pos = "left"
            else:
                self.width_geo = screen.width()
                self.pos = "right"

        if self.pos == "left":
            self.setGeometry(-30, -30, 100, 100)
            rotation = 180
        else:
            rotation = 0
            self.setGeometry(self.width_geo - 80, -30, 100, 100)

        pixmap = self.original_pixmap.transformed(QTransform().rotate(rotation))
        self.image_label.setPixmap(pixmap)
