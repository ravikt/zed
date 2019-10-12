#!/usr/bin/env python

import rospy
import numpy as np
import sys, time
import cv2
import message_filters

import roslib
import rospy

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class disp:
    
     def __init__(self):

         self.bridgeleft = CvBridge()
         self.bridgeright= CvBridge()
         self.bridgedisp = CvBridge()

         self.disp_pub = rospy.Publisher("disparity", Image, queue_size=1)

         self.imleft_sub = message_filters.Subscriber("/left/image_rect_color", Image, queue_size=1)
         self.imright_sub = message_filters.Subscriber("/right/image_rect_color", Image, queue_size=1)
        
         ts = message_filters.TimeSynchronizer([self.imleft_sub, self.imright_sub], 1)
         ts.registerCallback(self.processImage)
 
         rospy.loginfo("disparity initialized")


     def processImage(self, imleft, imright):
        
         left  = self.bridgeleft.imgmsg_to_cv2(imleft)
         right = self.bridgeright.imgmsg_to_cv2(imright)

         # convert to grayscale
         left  = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
         right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
         
         stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
         disp = stereo.compute(left,right)
        
         image_ros_msg = self.bridgedisp.cv2_to_imgmsg(disp, "passthrough")
         self.disp_pub.publish(image_ros_msg) 

def main(args):
    ic = disp()
    rospy.init_node('disp', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down disparity module"
    cv2.destroyAllWindows()

if __name__ == '__main__':
   
    main(sys.argv)
