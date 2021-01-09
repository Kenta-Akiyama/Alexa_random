#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import os

n = 0

def cb(message):

	global n
	n = message.data

if __name__ == '__main__': 
	rospy.init_node('spreadsheet')
	sub = rospy.Subscriber('random_num', Int32, cb) 
	pub = rospy.Publisher('spreadsheet_gs', Int32, queue_size=1) 
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		if n == 1:
			os.system('curl -X POST -d "rand=1" -o /dev/null https://script.google.com/macros/s/AKfycbwBJIqkjCFkG8WDRrMCWK5ABZJwQZwiTnB6LTnrEjkTdxwT3Lgv/exec')
		else:
			pub.publish(n)

		rate.sleep()
