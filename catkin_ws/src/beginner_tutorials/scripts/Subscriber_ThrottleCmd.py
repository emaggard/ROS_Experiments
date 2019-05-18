#!/usr/bin/env python

import rospy
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
    print("Received a /vehicle/throttle_cmd message!")
    print("Throttle: %f, %d"%(pedal_cmd, pedal_cmd_type))
    print("Booleans: %d, %d, %d, %d"%(enable, clear, ignore, count))

def listener():
    rospy.init_node('throttle_cmd_listener')
    rospy.Subscriber("/vehicle/throttle_cmd", ThrottleCmd, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
