# !/usr/bin/env/python

import rospy
import numpy as np
import sys, time
import cv2
import scipy.ndimage import filters

import roslib
import rospy

from sensor_msgs.msg import Image, CompressedImage 
from cv_bridge import CvBridge, CvBridgeError

VERBOSE = True

class disparity:
    
     def __init__(self):

         self.bridge = CvBridge()
        
         self.disp_pub = rospy.Publisher("disparity", Image, queue_size=1)

         self.subscriber = rospy.Subscriber("/left/image_rect_color", Image, self.imleft, queue_size = 1)
 
         self.subscriber = rospy.Subscriber("/right/image_rect_color", Image, self.imright, queue_size = 1)
        
         rospy.loginfo("disparity initialized")

     def imleft(self, leftimage):

         leftimage = self.bridge.imgmsg_to_cv2(leftimage)
         return leftimage
          
     def imleft(self, rightimage):

         rightimage = self.bridge.imgmsg_to_cv2(rightimage)
         return rightimage

     def processImage(self, image_msg):
        # convert rosmsg to cv2 type
        image_cv = self.bridge.imgmsg_to_cv2(image_msg)            
      
        self.disp_pub.publish(altitude_mtrs) 


def main(args):
   ic = disparity
   rospy.init_node('disparity', anonymous=True)
   try:
     rospy.spin()
   except KeyboardInterrupt:
     print "Shutting down ROS altitude module"
   cv2.destroyAllWindows()

if __name__ == '__main__':
   main(sys.argv)           
