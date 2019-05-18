#!/usr/bin/env python
import roslib; #roslib.load_manifest('YOUR_PACKAGE_NAME_HERE')
import rospy
from sensor_msgs.msg import Imu

def callback(msg):
    print("Received a /imu message!")
    print("Header: [%d, %d, %d, %s]"%(msg.header.seq, msg.header.stamp.secs, msg.header.stamp.nsecs, msg.header.frame_id))
    print("Orientation Components: [%f, %f, %f, %f]"%(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w))
    print("Angular_Vel Components: [%f, %f, %f]"%(msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z))
    print("Linear_Accel Components: [%f, %f, %f]"%(msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z))

def listener():
    rospy.init_node('imu_listener')
    rospy.Subscriber("/imu", Imu, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
