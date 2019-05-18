#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from sensor_msgs.msg import Temperature

def callback(msg):
    print("Received a /temp message!")
    print("Header: [%d, %d, %d, %s]"%(msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id))
    print("Temperature: [%f]"%(msg.temperature))
    print("Variance: [%f]"%(msg.variance))

def listener():
    rospy.init_node('temp_listener')
    rospy.Subscriber("/temp", Temperature, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
