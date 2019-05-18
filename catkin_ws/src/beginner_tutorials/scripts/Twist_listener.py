#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from geometry_msgs.msg import Twist

def callback(msg):
    print("Received a /cmd_vel message!")
    print("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    print("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

def listener():
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
