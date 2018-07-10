#!/usr/bin/env python

import cv2  
import rospy 
from sensor_msgs.msg import Image
from std_msgs.msg import Float32  
from cv_bridge import CvBridge 

class altimeter:
    def __init__(self):
        
        self.bridge = CvBridge()
         
        self.pub_altitude = rospy.Publisher("altitude",\
                Float32, queue_size=1)
        
        self.sub_image = rospy.Subscriber("/zed/depth/depth_registered",\
                Image, self.processImage, queue_size=1)
        
        rospy.loginfo("zedros initialized")

    def processImage(self, image_msg):
        # convert rosmsg to cv2 type
        image_cv = self.bridge.imgmsg_to_cv2(image_msg)            
           
        # take minimum value from depth image
        minimum = np.min(image_cv)
   
        # convert cv2 message back to rosmsg
        altitude_mtrs = self.bridge.cv2_to_imgmsg(image_cv, "bgr8")

        # publish rosmsg 
        self.pub_altitude.publish(altitude_mtrs) 


if __name__=="__main__":
   
    rospy.init_node('zedros')
    e = zedros()
    rospy.spin()
