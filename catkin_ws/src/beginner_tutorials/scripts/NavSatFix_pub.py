#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
import pynmea2
from sensor_msgs.msg import NavSatFix

s = serial.Serial('/dev/ttyS0', 9600)

def talker():
    pub = rospy.Publisher('navsat', NavSatFix, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = NavSatFix()
    seq = 0
    while not rospy.is_shutdown():
        seq += 1
        msg.header.seq = seq
        msg.status.status = int(1)
        msg.status.service = int(0)
        msg.latitude = float('%1.3f'%random.random())*100
        msg.longitude = float('%1.3f'%random.random())*100
        msg.altitude = float('%1.3f'%random.random())*1000

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
