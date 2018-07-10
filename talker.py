#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import Image
from cv_bridge import CvBridge

def imtalker():
    pub = rospy.Publisher('imchatter', Image, queue_size=10)
    rospy.init_node('imtalker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    bridge = CvBridge()
    while not rospy.is_shutdown():
        msg = Image()
        rospy.loginfo(msg)
        pub.publish(bridge.imgmsg_to_cv2(msg))
        rate.sleep()

if __name__ == '__main__':
    try:
        imtalker()
    except rospy.ROSInterruptException:
        pass
