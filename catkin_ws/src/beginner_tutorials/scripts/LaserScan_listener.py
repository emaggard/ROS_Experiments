#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print("Received a /laser message!")
    print("Header: [%d, %d, %d, %s]"%(msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id))
    print("Angle Min: [%f]"%(msg.angle_min))
    print("Angle Max: [%f]"%(msg.angle_max))
    print("Angle Increment: [%f]"%(msg.angle_increment))
    print("Time Increment: [%f]"%(msg.time_increment))
    print("Scan Time: [%f]"%(msg.scan_time))
    print("Range Min: [%f]"%(msg.range_min))
    print("Range Max: [%f]"%(msg.range_max))
    print("Ranges: " + str(msg.ranges))
    print("Intensities: " + str(msg.intensities))

def listener():
    rospy.init_node('laser_listener')
    rospy.Subscriber("/laser", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
