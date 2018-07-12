import numpy as np
import cv2
from matplotlib import pyplot as plt

# Lucas-kanade default parameters
# lk_params = dict( winSize  = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))   




def featureTracking(prevImg, nextImg, prevPts):
    
    nextPts, st, err = cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, None, **lk_params)
         
    return nextPts

def featureDetection(image1):

    fast = cv2.FastFeatureDetector_create()
    kp = fast.detect(image1, None) # Keypoints detetcted from FAST algorithm
    img2 = cv2.drawKeypoints(image1, kp, None, color=(0,255,0))
    return kp


