import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve
import Window.resource_rc
from Funtionality.Config import get_config

image_path = u":/icon/eyes.png"


class OverlayWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.width_geo, self.pos = self.win_geometry()
        print(self.width_geo, self.pos)
        if self.pos == "left":
            self.setGeometry(-30, -50, 100, 100)
        else:
            self.setGeometry(self.width_geo - 80, -50, 100, 100)

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.WindowTransparentForInput
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.5)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
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
                self.show_with_animation(QRect(0, -15, 100, 100))
            else:
                self.show_with_animation(QRect(self.width_geo - 120, -15, 100, 100))
            self.setWindowOpacity(1.0)
            self.state = True
        else:
            if self.state:
                if self.pos == "left":
                    self.show_with_animation(QRect(-30, -50, 100, 100))
                else:
                    self.show_with_animation(QRect(self.width_geo - 80, -50, 100, 100))
                self.state = False
                self.setWindowOpacity(0.5)

    def win_geometry(self):
        screen = self.screen().size()
        if screen is not None:
            values = get_config()
            if values['overlay'] == "Left":
                width = 0
                pos = "left"
            else:
                width = screen.width()
                pos = "right"

            return width, pos
        return None
