from PySide6.QtCore import QObject, QMutexLocker, QMutex, Qt, QThread
from pynput import mouse, keyboard


class InputListenerThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.activity_detector = parent
        self.stop_flag = False

    def run(self):
        # Set up mouse listener
        mouse_listener = mouse.Listener(on_move=self.activity_detector.on_move,
                                        on_click=self.activity_detector.on_click,
                                        on_scroll=self.activity_detector.on_scroll)
        mouse_listener.start()

        # Set up keyboard listener
        keyboard_listener = keyboard.Listener(on_press=self.activity_detector.on_press,
                                              on_release=self.activity_detector.on_release)
        keyboard_listener.start()

        # Run the listeners until the stop flag is set
        while not self.stop_flag:
            self.msleep(100)  # Sleep for a short interval to check the flag

        mouse_listener.stop()
        keyboard_listener.stop()

        mouse_listener.join()
        keyboard_listener.join()

    def stop_listening(self):
        self.stop_flag = True


class ActivityDetector(QObject):
    def __init__(self):
        super().__init__()
        self.activity_detected = False
        self.mutex = QMutex()

        self.input_listener_thread = InputListenerThread(self)

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

    def start_listening(self):
        self.input_listener_thread.start()

    def stop_listening(self):
        self.input_listener_thread.stop_listening()
        self.input_listener_thread.wait()

    def check_activity(self):
        with QMutexLocker(self.mutex):
            return self.activity_detected

    def reset_activity(self):
        with QMutexLocker(self.mutex):
            self.activity_detected = False