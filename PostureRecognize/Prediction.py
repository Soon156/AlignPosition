import time
from mediapipe import tasks, Image, ImageFormat

from Funtionality.Config import abs_detection_file_path


class LandmarkResult:
    def __init__(self):
        self.result = tasks.vision.PoseLandmarkerResult
        self.detector = tasks.vision.PoseLandmarker
        self.create_detector()

    def create_detector(self):
        # callback function
        def update_result(result: tasks.vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
            self.result = result

        options = tasks.vision.PoseLandmarkerOptions(
            base_options=tasks.BaseOptions(model_asset_path=abs_detection_file_path),
            running_mode=tasks.vision.RunningMode.LIVE_STREAM,
            result_callback=update_result)

        self.detector = self.detector.create_from_options(options)

    def detect_async(self, frame):
        # convert np frame to mp image
        mp_image = Image(image_format=ImageFormat.SRGB, data=frame)
        # detect landmarks
        self.detector.detect_async(image=mp_image, timestamp_ms=int(time.time() * 1000))

    def close(self):
        self.detector.close()
