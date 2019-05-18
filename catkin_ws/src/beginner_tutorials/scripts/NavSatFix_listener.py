#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from sensor_msgs.msg import NavSatFix

def callback(msg):
    print("Received a /navsat message!")
    print("Header: [%d, %d, %d, %s]"%(msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id))
    print("Status Components: [%d, %d]"%(msg.status.status, msg.status.service))
    print("Latitude: [%f]"%(msg.latitude))
    print("Longitude: [%f]"%(msg.longitude))
    print("Altitude: [%f]"%(msg.altitude))
    print("Position Covariance: " + str(msg.position_covariance) + "]")
    print("Covariance Type: [%d]"%(msg.position_covariance_type))
    
def listener():
    rospy.init_node('navsat_listener')
    rospy.Subscriber("/navsat", NavSatFix, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
