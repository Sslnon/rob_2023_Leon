import cv2
from robomaster import *
from runner.CameraController import *
from runner.DistanceSensor import *
from runner.LineDetector import *
import time



class RobotController:
    def __init__(self):
        self.ep_robot = robot.Robot()
        self.ep_robot.initialize(conn_type="ap")
        self.ep_robot.set_robot_mode(mode='chassis_lead')

        self.ep_led = self.ep_robot.led
        self.ep_chassis = self.ep_robot.chassis


    def drive(self):
        self.ep_led.set_led(comp=led.COMP_ALL, r=180, g=255, b=120, effect=led.EFFECT_ON)
        ep_camera = CameraController(self.ep_robot)
        ep_sensor = DistanceSensor(self.ep_robot,self.ep_chassis)
        ep_vison = LineDetector(self.ep_robot,self.ep_chassis)

        while True:
            img = ep_camera.readImage()
            distance = ep_sensor.dis_check()
            if(distance > 400):
                ep_vison.followLine(img)

            time.sleep(0.001)

            cv2.imshow("Line",img)

            key = cv2.waitKey(1)
            if key == 27:
                print("视频结束")
                self.ep_chassis.drive_speed(x=0, y=0, z=0)
                break

        ep_vison.cancelDetect()
        cv2.destroyAllWindows()
        ep_camera.cancelCamera()
        self.ep_robot.close()
