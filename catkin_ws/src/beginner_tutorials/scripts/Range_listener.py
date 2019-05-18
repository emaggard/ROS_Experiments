#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from sensor_msgs.msg import Range

def callback(msg):
    print("Received a /range message!")
    print("Header: [%d, %d, %d, %s]"%(msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id))
    print("Radiation Type: [%f]"%(msg.radiation_type))
    print("Field Of View: [%f]"%(msg.field_of_view))
    print("Range Min: [%f]"%(msg.min_range))
    print("Range Max: [%f]"%(msg.max_range))
    print("Range: [%f]"%(msg.range))

def listener():
    rospy.init_node('range_listener')
    rospy.Subscriber("/range", Range, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
