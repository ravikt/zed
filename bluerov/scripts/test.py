#!/usr/bin/env python

import rospy
import numpy as np
import sys, time
import cv2
import message_filters

import roslib
import rospy

from sensor_msgs.msg import Image, 
from cv_bridge import CvBridge, CvBridgeError


def disp():
    
    rospy.init_node('disparity', anonymous=True)

    bridgeleft = CvBridge()
    bridgeright= CvBridge()

    disp_pub = rospy.Publisher("disparity", Image, queue_size=1)

    imleft_sub = message_filters.Subscriber("/left/image_rect_color", Image, queue_size=1)
    imright_sub = message_filters.Subscriber("/right/image_rect_color", Image, queue_size=1)
            
    ts = message_filters.TimeSynchronizer([self.imleft_sub, self.imright_sub], 1)
    ts.registerCallback(self.processImage)
    
    rospy.loginfo("disparity initialized")
    rospy.spin()

def processImage(self, imleft, imright):
        
    left  = self.bridgeleft.imgmsg_to_cv2(imleft)
    right = self.bridgeright.imgmsg_to_cv2(imright)

    stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
    disp = stereo.compute(left,right)
        
    image_ros_msg = self.bridge.cv2_to_imgmsg(disp, "mono8")
    self.disp_pub.publish(image_ros_msg) 


if __name__ == '__main__':
   
   disp()
