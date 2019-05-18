#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from sensor_msgs.msg import Imu

def talker():
    pub = rospy.Publisher('imu', Imu, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = Imu()
    seq = 0
    while not rospy.is_shutdown():
        seq += 1
        msg.header.seq = seq
        msg.orientation.x = float('%1.3f'%random.random())
        msg.orientation.y = float('%1.3f'%random.random())
        msg.orientation.z = float('%1.3f'%random.random())
        msg.orientation.w = float('%1.3f'%random.random())
        msg.angular_velocity.x = float('%1.3f'%random.random())
        msg.angular_velocity.y = float('%1.3f'%random.random())
        msg.angular_velocity.z = float('%1.3f'%random.random())
        msg.linear_acceleration.x = float('%1.3f'%random.random())
        msg.linear_acceleration.y = float('%1.3f'%random.random())
        msg.linear_acceleration.z = float('%1.3f'%random.random())
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
