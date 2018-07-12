import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('000000.png', 0)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )


# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
kpgood = cv2.goodFeaturesToTrack(img, mask = None, **feature_params)

img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
# Print all default params
'''
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
'''
#plt.imshow(img2)
#plt.show()
cv2.imwrite('fast_true1.png',img2)
print type(kpgood)
print type(kp), len(kp)