import time
import mediapipe as mp


class LandmarkResult:
    def __init__(self):
        self.result = mp.tasks.vision.PoseLandmarkerResult
        self.detector = mp.tasks.vision.PoseLandmarker
        self.create_detector()

    def create_detector(self):
        # callback function
        def update_result(result: mp.tasks.vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
            self.result = result

        # TODO add entry for model in config
        options = mp.tasks.vision.PoseLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path='pose_landmarker_heavy.task'),
            running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
            result_callback=update_result)

        self.detector = self.detector.create_from_options(options)

    def detect_async(self, frame):
        # convert np frame to mp image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        # detect landmarks
        self.detector.detect_async(image=mp_image, timestamp_ms=int(time.time() * 1000))

    def close(self):
        self.detector.close()
