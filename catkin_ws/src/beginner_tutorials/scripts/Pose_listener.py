#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from geometry_msgs.msg import Pose

def callback(msg):
    print("Received a /pose message!")
    print("Position Components: [%f, %f, %f]"%(msg.position.x, msg.position.y, msg.position.z))
    print("Orientation Components: [%f, %f, %f, %f]"%(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w))

def listener():
    rospy.init_node('pose_listener')
    rospy.Subscriber("/pose", Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
