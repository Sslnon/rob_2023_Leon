distance = [400]

class DistanceSensor:
    def __init__(self,ep_robot,ep_chassis):
        """ construct/init the dis sensor
        :param ep_robot: robot object
        :param ep_chassis: ep_chassis object
        :return:
        """
        self.ep_sensor = ep_robot.sensor
        self.ep_sensor.sub_distance(freq=5, callback=self.sub_data_handler)
        self.ep_chassis =ep_chassis

    def sub_data_handler(self,sub_info):
        """ get dis info
        :param sub_info: a info
        :return:
        """
        global distance
        distance = sub_info

    def dis_check(self):
        """ check distance
        :param:
        :return: return the distance at present
        """
        if 400 >= distance[0] > 300:  # 减速区
            self.ep_chassis.drive_speed(x=0.1, y=0, z=0)

        elif 300 >= distance[0] > 100:
            self.ep_chassis.drive_speed(x=0, y=0, z=0)

        elif 50 >= distance[0] > 1:  # 后退区
            self.ep_chassis.drive_speed(x=-0.1, y=0, z=0)

        return distance[0]
