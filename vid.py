import cv2
from matplotlib import pyplot as plt
import numpy as np
import skvideo.io
import skvideo.utils

m = 600
n = 600

img_dir = 'results/'


# An empty matrix to hold all the sequence of images
#outVideo = np.empty([5291, 360, 490, 3], dtype = np.uint8)
#outVideo = np.empty([2384, 480, 720, 3], dtype = np.uint8)
outVideo = np.empty([565, m, n, 3], dtype = np.uint8)

outVideo = outVideo.astype(np.uint8)
#outVideo = np.empty((5291, 360, 490))
#outVideo = outVideo.astype(np.uint8)


for i in range(565):
    #print(frame.shape)
    frame = cv2.imread(img_dir+'maps{!s}.png'.format(i))
    #print(frame.shape)
    outVideo[i] = frame

# Writes the the output image sequences in a video file
skvideo.io.vwrite("outputvideo2.mp4", outVideo)
