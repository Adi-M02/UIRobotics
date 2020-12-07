#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def arm_base():

    rospy.init_node('arm_base')
    rospy.Subscriber('base', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    arm_base()
