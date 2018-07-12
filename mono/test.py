import numpy as np
import cv2

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

im1 = cv2.imread('000000.png')
im2 = cv2.imread('000001.png')

def featureTracking(prevImg, nextImg, prevPts):
    # keypoint should be numpy array
    nextPts, st, err = cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, None, **lk_params)
    return nextPts

def featureDetection(image1):
    
    fast= cv2.FastFeatureDetector_create(threshold=25, nonmaxSuppression=True)
    #fast = cv2.FastFeatureDetector_create()
    # FAST return list, convert to numpy array
    kp = fast.detect(image1, None) 
    kp = np.array([k.pt for k in kp], dtype=np.float32)
    #kp = np.asarray(kp ,dtype=np.float32)
    #img2 = cv2.drawKeypoints(image1, kp, None, color=(0,255,0))
    #kp = cv2.goodFeaturesToTrack(image1, mask = None, **feature_params)
    return kp 


im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

 
p0 = featureDetection(im1)
a = featureTracking(im1, im2, p0)
print p0.shape