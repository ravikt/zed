#!/usr/bin/env python

import cv2  
import rospy 
from sensor_msgs.msg import Image  
from cv_bridge import CvBridge 

class zedros:
    def __init__(self):
        
        self.bridge = CvBridge()
         
        self.pub_image = rospy.Publisher("rgb_image",\
                Image, queue_size=1)
        
        self.sub_image = rospy.Subscriber("/zed/rgb/image_rect_color",\
                Image, self.processImage, queue_size=1)
        
        rospy.loginfo("zedros initialized")

    def processImage(self, image_msg):
        # convert rosmsg to cv2 type
        image_cv = self.bridge.imgmsg_to_cv2(image_msg)            
        
        # convert cv2 message back to rosmsg
        image_ros_msg = self.bridge.cv2_to_imgmsg(image_cv, "bgr8")

        # publish rosmsg 
        self.pub_image.publish(image_ros_msg) 


if __name__=="__main__":
   
    rospy.init_node('zedros')
    e = zedros()
    rospy.spin()
