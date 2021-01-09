#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('random')                                # ノード名「count」に設定
pub = rospy.Publisher('random_num', Int32, queue_size=1)  # パブリッシャ「count_up」を作成
rate = rospy.Rate(1)                                   # 10Hzで実行
n = 0

while not rospy.is_shutdown():
    n = random.randint(1,50)
    pub.publish(n)
    rate.sleep()
