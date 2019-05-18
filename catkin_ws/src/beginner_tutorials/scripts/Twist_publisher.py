#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = Twist()
    while not rospy.is_shutdown():
        msg.linear.x = float('%1.3f'%random.random())
        msg.linear.y = float('%1.3f'%random.random())
        msg.linear.z = float('%1.3f'%random.random())
        msg.angular.x = float('%1.3f'%random.random())
        msg.angular.y = float('%1.3f'%random.random())
        msg.angular.z = float('%1.3f'%random.random())
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
