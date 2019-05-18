#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print("Received a /odom message!")
    print("Header: [%d, %d, %d, %s]"%(msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id))
    print("Child Frame Components: [%s]"%(msg.child_frame_id))
    print("Pose Components: [Pose:%f, %f, %f  Orient:%f, %f, %f, %f]"%(msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z, msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w))
    print("Twist Components: [Lin:%f, %f, %f  Ang:%f, %f, %f]"%(msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z, msg.twist.twist.angular.x, msg.twist.twist.angular.y, msg.twist.twist.angular.z))

def listener():
    rospy.init_node('odom_listener')
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
