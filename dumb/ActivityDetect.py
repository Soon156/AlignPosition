import time
from PySide6.QtCore import QThread, Signal
import pyautogui
import cv2
import numpy as np
from pynput import keyboard, mouse


class ScreenCaptureWorker(QThread):
    change_detected = Signal(bool)

    def run(self):
        old_frame = None
        while True:
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            if old_frame is not None:
                mse = np.mean((frame - old_frame) ** 2)
                print(mse)
                if mse > 0.5:  # You need to define an appropriate threshold
                    change = True
                else:
                    change = False
            else:
                change = False
            old_frame = frame
            print(change)
            self.change_detected.emit(change)
            time.sleep(1)


class InputListener(QThread):
    activity_detected = Signal()

    def __init__(self):
        super().__init__()
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.is_active = False

    def on_key_press(self, key):
        self.is_active = True

    def on_mouse_move(self, x, y):
        self.is_active = True

    def run(self):
        with self.keyboard_listener as kl, self.mouse_listener as ml:
            self.is_active = False
            kl.join()
            ml.join()

    def stop(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
