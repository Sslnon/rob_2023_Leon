import time

from info.MarkerInfo import MarkerInfo

markers = []
class markerFinding:
    def __init__(self, ep_robot, ep_chassis):
        self.ep_chassis = ep_chassis
        self.ep_vision = ep_robot.vision


    def detect(self):
        self.ep_vision.sub_detect_info(name="marker", callback=self.on_detect_marker)

    def cancelDetect(self):
        """ cancel detector
        :param:
        :return:
        """
        self.ep_vision.unsub_detect_info(name="marker")

    def on_detect_marker(self,marker_info):
        number = len(marker_info)
        markers.clear()
        for i in range(0, number):
            x, y, w, h, info = marker_info[i]
            markers.append(MarkerInfo(x, y, w, h, info))


    def stop(self,img):
        if len(markers) > 0:
            print("Finding")






