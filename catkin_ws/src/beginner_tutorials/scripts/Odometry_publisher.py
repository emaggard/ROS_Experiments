#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from nav_msgs.msg import Odometry

def talker():
    pub = rospy.Publisher('odom', Odometry, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = Odometry()
    seq = 0
    while not rospy.is_shutdown():
        seq += 1
        msg.header.seq = seq
        msg.pose.pose.position.x = float('%1.3f'%random.random())
        msg.pose.pose.position.y = float('%1.3f'%random.random())
        msg.pose.pose.position.z = float('%1.3f'%random.random())
        msg.pose.pose.orientation.x = float('%1.3f'%random.random())
        msg.pose.pose.orientation.y = float('%1.3f'%random.random())
        msg.pose.pose.orientation.z = float('%1.3f'%random.random())
        msg.pose.pose.orientation.w = float('%1.3f'%random.random())
        msg.twist.twist.linear.x = float('%1.3f'%random.random())
        msg.twist.twist.linear.y = float('%1.3f'%random.random())
        msg.twist.twist.linear.z = float('%1.3f'%random.random())
        msg.twist.twist.angular.x = float('%1.3f'%random.random())
        msg.twist.twist.angular.y = float('%1.3f'%random.random())
        msg.twist.twist.angular.z = float('%1.3f'%random.random())
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
