import cv2
from robomaster import *


class CameraController:
    def __init__(self,ep_robot):
        """ construct/init the camera
        :param ep_robot: robot object
        :return:
        """
        self.ep_camera = ep_robot.camera
        self.ep_camera.start_video_stream(display=False)

    def readImage(self):
        """ read cv2 video stream
        :return: cv2 image stream
        """
        return self.ep_camera.read_cv2_image(strategy="newest")

    def cancelCamera(self):
        """ close the stream
        """
        self.ep_camera.stop_video_stream()