#!/usr/bin/env python
# license removed for brevity
import rospy
import random
import numpy as np
from sensor_msgs.msg import LaserScan

def talker():
    pub = rospy.Publisher('laser', LaserScan, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = LaserScan()
    seq = 0
    while not rospy.is_shutdown():
        seq += 1
        msg.header.seq = seq
        msg.angle_min = 0.0
        msg.angle_max = 0.0
        msg.angle_increment = 0.95
        msg.time_increment = 0.003
        msg.scan_time = 0.23
        msg.range_min = 0.2
        msg.range_max = 5.0
        msg.ranges = np.zeros(100)
        msg.intensities = np.zeros(100)

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
