from robomaster import robot
import cv2
from info.PointInfo import PointInfo

line = []
class LineDetector:
    def __init__(self, ep_robot, ep_chassis):
        """ construct/init the vision function
        :param ep_robot: robot object
        :param ep_chassis: ep_chassis object
        :return:
        """
        self.ep_vision = ep_robot.vision
        self.ep_vision.sub_detect_info(name="line", color="blue", callback=self.on_detect_line)
        self.ep_chassis = ep_chassis
    def cancelDetect(self):
        """ cancel detector
        :param:
        :return:
        """
        self.ep_vision.unsub_detect_info(name="line")

    def on_detect_line(self,line_info):
        """ detect the car on the line
        :param line_info: line info
        :return:
        """
        number = len(line_info)
        line.clear()
        if number > 0:
            line_type = line_info[0]
            for i in range(1, number):
                x, y, ceta, c = line_info[i]
                line.append(PointInfo(x, y, ceta, c))
        else:
            print('no line')

    def followLine(self,img):
        """ let the car run and follow line
        :param img: cv2 img
        :return:
        """
        line_tmp = line.copy()
        for j in range(0, len(line_tmp)):
            cv2.circle(img, line_tmp[j].pt, 3, line_tmp[j].color, -1)
        if len(line_tmp) > 0:
            point_x_3 = line_tmp[4]._x
            error_3 = point_x_3 - 0.5
            angle_output = 90 * error_3

            point_x_8 = line_tmp[8]._x
            error_8 = 0.5 - point_x_8

            self.ep_chassis.drive_speed(x=0.25, y=0, z=angle_output)
        # else:
        #     self.ep_chassis.drive_speed(x=-0.1, y=0, z=0)

