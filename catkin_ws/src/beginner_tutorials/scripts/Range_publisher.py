#!/usr/bin/env python
# license removed for brevity
import rospy
import random
import numpy as np
from sensor_msgs.msg import Range

def talker():
    pub = rospy.Publisher('range', Range, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = Range()
    seq = 0
    while not rospy.is_shutdown():
        seq += 1
        msg.header.seq = seq
        msg.radiation_type = 0
        msg.field_of_view = 30.0
        msg.min_range = 0.2
        msg.max_range = 2.0
        msg.range = random.random()*2.0

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
