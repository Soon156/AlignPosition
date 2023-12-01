import socket
import subprocess
from Funtionality import Config
import logging as log
import time

from PySide6.QtCore import QThread, Signal, QMutexLocker, QMutex
service_name = "EventDetectService"


class EventHandler(QThread):
    event_type = Signal(str)
    error_msg = Signal(str)
    finished = Signal(bool)

    def __init__(self):
        super().__init__()
        self.port = None
        self.waiting = False
        self.mutex = QMutex()

    def change_waiting(self, state):
        self.waiting = state

    def start_windows_service_with_arguments(self):
        try:
            cmd = ['sc', 'start', service_name] + self.port
            subprocess.run(cmd, check=True)
            log.info(f"The {service_name} service has been started on port: {self.port}")
        except subprocess.CalledProcessError as e:
            log.error(f"Error starting {service_name} service: {e}")

    def run(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 0))
        server.listen()

        self.port = server.getsockname()[1]

        log.info(f"Event handler start on port {self.port}")

        self.start_windows_service_with_arguments()

        while True:
            time.sleep(0.5)
            client_socket, client_address = server.accept()
            response = "Success"
            try:
                request = client_socket.recv(1024)  # receive data from the client
                msg = request.decode('utf-8')
                log.info(f"Event detected: {msg}")
                self.event_type.emit(msg)
                wait_time = time.time()
                while self.waiting:
                    if time.time() - wait_time > 15:
                        response = "Failed"
                        log.warning("Waiting too long for response from main thread! Data may be lost")
                        break
            except Exception as e:
                log.error(f"Error handling client: {e}")
                response = "Failed"
            finally:
                with QMutexLocker(self.mutex):
                    client_socket.send(response.encode('utf-8'))  # send a response back to the client
                    client_socket.close()
                break

        server.close()
