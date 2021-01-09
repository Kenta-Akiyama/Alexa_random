#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('rand')
pub = rospy.Publisher('rand_num', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0

while not rospy.is_shutdown():
    n = random.randint(1,50)
    pub.publish(n)
    rate.sleep()
