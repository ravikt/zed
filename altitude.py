#!/usr/bin/env python 
import rospy
import roslib
import numpy as np 

from sensor_msgs.msg import Image

def callback(data):
   rospy.loginfo(rospy.get_caller_id())

def altitude():
   rospy.init_node('altitude', anonymous=True)
   rospy.Subscriber("/zed/depth/depth_registered", Image, callback)
   rospy.spin()

if __name__ == '__main__':

   altitude()
