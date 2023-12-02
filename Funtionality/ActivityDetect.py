from PySide6.QtCore import QObject, QMutexLocker, QMutex
from pynput import mouse, keyboard


class ActivityDetector(QObject):
    def __init__(self):
        super().__init__()
        self.activity_detected = False
        self.mutex = QMutex()

        # Set up mouse listener
        self.mouse_listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.mouse_listener.start()

        # Set up keyboard listener
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.keyboard_listener.start()

    def on_move(self, x, y):
        with QMutexLocker(self.mutex):
            self.activity_detected = True

    def on_click(self, x, y, button, pressed):
        with QMutexLocker(self.mutex):
            self.activity_detected = True

    def on_scroll(self, x, y, dx, dy):
        with QMutexLocker(self.mutex):
            self.activity_detected = True

    def on_press(self, key):
        with QMutexLocker(self.mutex):
            self.activity_detected = True

    def on_release(self, key):
        pass

    def check_activity(self):
        with QMutexLocker(self.mutex):
            return self.activity_detected

    def reset_activity(self):
        with QMutexLocker(self.mutex):
            self.activity_detected = False

    def waiting_join(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.mouse_listener.join()
        self.keyboard_listener.join()
