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

class altitude:
    
     def __init__(self):
        
         self.image_pub = rospy.Publisher("altitude/image_raw/compressed", CompressedImage, queue_size=1)

         self.subscriber = rospy.Subscriber("/zed/rgb/image_rect_color", Image, self.callback, queue_size = 1)

         if VERBOSE :
           print "Subscribed to /zed/rgb/image_rect_color"


      def callback(self, ros_data):

          if VERBOSE :
            print 'received image o ftype: "%s"' % ros_data.format
          
      
          ## conversion to cv2 ##
          np_arr = np.fromstring(ros_data.data, np.uint8) 
          image_np = cv2.imdecode(np_Arr, cv2.CV_LOAD_IMAGE_COLOR)

          ## convert to grayscale ##
          image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
          time2 = time.time()
   
          if VERBOSE :
            print 'Image converted to grayscale'

          cv2.imshow('gray', image)
          cv2.waitKey(2)
           
          msg = CompressedImage()
          msg.header.stamp = rospy.Time.now()
          msg.format = "jpeg"
          msg.data = np.array(cv2.imdecode('.jpg', image)[1].tostring())

          # Publish new image
          self.image_pub.publish(msg)


def main(args):
   ic = altitude()
   rospy.init_node('altitude', anonymous=True)
   try:
     rospy.spin()
   except KeyboardInterrupt:
     print "Shutting down ROS altitude module"
   cv2.destroyAllWindows()

if __name__ == '__main__':
   main(sys.argv)           
