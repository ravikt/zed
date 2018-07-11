# !/usr/bin/env/python

import rospy
import numpy as np
import sys, time
import cv2

from matplotlib import pyplot as plt

import roslib
import rospy

from sensor_msgs.msg import Image, CompressedImage 
from cv_bridge import CvBridge, CvBridgeError


class disparity:
    
     def __init__(self):

         self.bridge = CvBridge()
         self.stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
         self.disp_pub = rospy.Publisher("disparity", Image, queue_size=1)

         self.imleft_sub = rospy.Subscriber("/left/image_rect_color", Image, self.imleft, queue_size = 1)
 
         self.imright_sub = rospy.Subscriber("/right/image_rect_color", Image, self.imright, queue_size = 1)

         self.last_right_image=None
         self.last_left_image=None
         
         rospy.loginfo("disparity initialized")

     def imleft(self, leftimage):
	    if self.last_right_image:
		    disp = self.stereo.compute(leftimage, self.last_right_image)
		    self.disp_pub.publish(disp)
		    self.last_right_image=None
	    else:
		    self.last_left_image = leftimage
            rospy.loginfo("subscribed to left image") 
          
     def imright(self, rightimage):
	    if self.last_left_image:
		    disp = self.stereo.compute(rightimage, self.last_left_image)
		    self.disp_pub.publish(disp)
		    self.last_left_image=None
	    else:
		    self.last_right_image = rightimage
            rospy.loginfo("subscribed to right image")


if __name__ == '__main__':
   
   rospy.init_node('disparity', anonymous=True)
   ic = disparity
   rospy.spin()          