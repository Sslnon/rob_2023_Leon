import cv2
from robomaster import *


class CameraController:
    def __init__(self,ep_robot):
        self.ep_camera = ep_robot.camera
        self.ep_camera.start_video_stream(display=False)

    def readImage(self):
        return self.ep_camera.read_cv2_image(strategy="newest")

    def cancelCamera(self):
        self.ep_camera.stop_video_stream()