#!/usr/bin/env python

from geometry_msgs.msg import PoseStamped
from styx_msgs.msg import Lane, Waypoint
from dbw_mkz_msgs.msg import ThrottleCmd, SteeringCmd, BrakeCmd, SteeringReport
from geometry_msgs.msg import PoseStamped, TwistStamped
from styx_msgs.msg import Lane, Waypoint, TrafficLightArray
from std_msgs.msg import Int32

import math
import rospy
import tf

def callback(msg):
    print("Received a /base_waypoints message!")
    print("Number of positions: %d"%(len(msg.waypoints)))
    # write points to csv file
    f = open("waypoints.csv", "w")
    for line in msg.waypoints:
        txt = "%f, %f\r"%(line.pose.pose.position.x, line.pose.pose.position.y)
        f.write(txt)
    f.close()
    print("file written")
    #print("Pose Position: [%f, %f, %f]"%(msg.pose.position.x, msg.pose.position.y, msg.pose.position.z))
    #print("Pose Orientation: [%f, %f, %f, %f]"%(msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w))

def listener():
    rospy.init_node('waypoint_listener')
    rospy.Subscriber("/base_waypoints", Lane, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
