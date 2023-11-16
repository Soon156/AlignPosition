from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QApplication

from PostureRecognize.ElapsedTime import read_elapsed_time_data, seconds_to_hms
from .changeStyleSheet import get_theme
from UI_Window.ui_MinWindow import Ui_minDialog
from UI_Window.ui_MinWindowDark import Ui_minDialog as Ui_minDialogDark
from PySide6.QtCore import Qt

if get_theme():
    ui_class = Ui_minDialog
else:
    ui_class = Ui_minDialogDark


class MinWindow(QDialog, ui_class):
    signal_bool = Signal(bool)

    def __init__(self, parent):
        super().__init__()
        self.dragPos = None
        self.parent = parent
        self.setupUi(self)
        self.icon_start = QIcon()
        self.icon_start.addFile(u":/icon/icons8-play-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_stop = QIcon()
        self.icon_stop.addFile(u":/icon/icons8-stop-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.stop_btn.clicked.connect(self.start_monitor)
        self.close_btn.clicked.connect(self.close_me)
        self.stick_threshold = 70
        self.setWindowOpacity(0.7)
        self.center()

    def init(self):
        if self.parent.monitoring_state:
            self.parent.posture_recognizer.save_usetime()
            self.stop_btn.setIcon(self.icon_stop)
        else:
            self.stop_btn.setIcon(self.icon_start)
        old_time, _ = read_elapsed_time_data()
        self.use_time_lbl.setText(seconds_to_hms(old_time))
        self.show()

    def close_me(self):
        self.parent.popout_btn.setEnabled(True)
        self.hide()
        if not self.parent.isVisible():
            self.parent.show()

    def start_monitor(self):
        self.parent.start_monitoring()

    def update_btn_state(self, condition=False):
        if condition:
            self.stop_btn.setIcon(self.icon_stop)
        else:
            self.stop_btn.setIcon(self.icon_start)
   # Hover Event
    def enterEvent(self, event):
        self.setWindowOpacity(1)

    def leaveEvent(self, event):
        self.setWindowOpacity(0.7)

    # Draggable handler
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def updatePosition(self):
        # Get the current screen geometry
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()

        # Calculate the distances to all four edges
        dist_left = self.pos().x()
        dist_right = screen_rect.right() - (self.pos().x() + self.width())
        dist_top = self.pos().y()
        dist_bottom = screen_rect.bottom() - (self.pos().y() + self.height())

        # Determine the nearest edge
        min_dist = min(dist_left, dist_right, dist_top, dist_bottom)

        # Calculate the new position for the window based on the nearest edge, with the threshold check
        new_x, new_y = self.pos().x(), self.pos().y()
        if min_dist <= self.stick_threshold:
            if min_dist == dist_left:
                new_x = screen_rect.left()
                if dist_top <= self.stick_threshold:
                    new_y = screen_rect.top()
                if dist_bottom <= self.stick_threshold:
                    new_y = screen_rect.bottom() - self.height()
            elif min_dist == dist_right:
                new_x = screen_rect.right() - self.width()
                if dist_top <= self.stick_threshold:
                    new_y = screen_rect.top()
                if dist_bottom <= self.stick_threshold:
                    new_y = screen_rect.bottom() - self.height()
            elif min_dist == dist_top:
                new_y = screen_rect.top()
            elif min_dist == dist_bottom:
                new_y = screen_rect.bottom() - self.height()

            self.move(new_x, new_y)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
        event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.updatePosition()
