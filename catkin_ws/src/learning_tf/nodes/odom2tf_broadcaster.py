#!/usr/bin/env python

# odom2tf_broadcaster
# subscribes to /odom topic and repubishes the data to the /tf topic

import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

def odom_transform(msg):
    tf_broadcaster = tf.TransformBroadcaster()
    current_time = rospy.Time.now()

    # since all odometry is 6DOF we'll need a quaternion created from yaw
    th = msg.twist.twist.angular.z
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    # publish the transform over tf
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    tf_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "base_footprint",
        "odom_combined"
    )
    
    
def listener():
    rospy.init_node('odom_listener')
    rospy.Subscriber("/odom", Odometry, odom_transform)
    rospy.spin()

if __name__ == '__main__':
    listener()
