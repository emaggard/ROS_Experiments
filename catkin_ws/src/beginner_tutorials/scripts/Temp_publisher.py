#!/usr/bin/env python
# license removed for brevity
import rospy
import random
import numpy as np
from sensor_msgs.msg import Temperature

def talker():
    pub = rospy.Publisher('temp', Temperature, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = Temperature()
    seq = 0
    while not rospy.is_shutdown():
        seq += 1
        msg.header.seq = seq
        msg.temperature = random.random()*30.0
        msg.variance = 30.0

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
