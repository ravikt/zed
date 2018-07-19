#!/usr/bin/env python

import cv2  
import rospy 
import roslib
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Float32, String  
from rospy.numpy_msg import numpy_msg

from cv_bridge import CvBridge 

class altimeter:
    def __init__(self):
        
        self.bridge = CvBridge()
         
        self.pub_altitude = rospy.Publisher("altitude",\
               numpy_msg(Float32), queue_size=1)
        
        self.sub_image = rospy.Subscriber("/depth/depth_registered",\
                Image, self.processImage, queue_size=1)
        #if VERBOSE: 
           #print "subscribed to /depth/depth_registered"
        
        rospy.loginfo("altimeter initialized")

    def processImage(self, image_msg):
        # convert rosmsg to cv2 type
        image_cv = self.bridge.imgmsg_to_cv2(image_msg)            
        
        #print image_cv.dtype
        altitude_mtrs = np.nanmin(image_cv)
        #cv2.imshow('depth', image_cv)
        #cv2.waitKey(0)
        
        #image_cv = numpy_msg(image_msg)    
        # take minimum value from depth image
        #altitude_mtrs = image_cv.min()
        #altitude_mtrs = np.min(image_cv)
        # convert cv2 message back to rosmsg
        #altitude_mtrs = self.bridge.cv2_to_imgmsg(image_cv, "bgr8")

        # publish rosmsg 
        #msg = Float32()
        #msg.data = altitude_mtrs
        #msg = np.array(image_cv, dtype=np.float32)
        #mini = np.min(msg)
        #msg = np.array(altitude_mtrs, dtype=np.float32)
        self.pub_altitude.publish(altitude_mtrs) 


if __name__=="__main__":
   
    rospy.init_node('altimeter')
    e = altimeter()
    rospy.spin()
