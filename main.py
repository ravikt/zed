from visual_odometry import PinholeCamera, VisualOdometry
import numpy as np
import cv2
import time

#poses_dir = 'data/poses/00.txt' #for ground truth
img_dir = 'data/'

# Pinhole(width, height, fx, fy, cx, cy, k1, k2, p1, p2, p3)
cam = PinholeCamera(1824, 992, 375.88, 375.88, 909, 469)
#with open(poses_dir) as f: 
#   poses = f.readlines()#poses

print("Mobileye data loaded.")

############ Perform Visual Odometry ############

vo = VisualOdometry(cam)

traj = np.zeros((600,600,3), dtype=np.uint8)

predicted = []
# predicted = np.array(predicted)
# actual = np.array(actual)

frames_arr= []
import time
start = time.time()
frames = 565
#drawing trajectories for each frame starting form the 3rd
for img_id in range(frames):
    img = cv2.imread(img_dir+str(img_id).zfill(6)+'.png', 0)
    #print(img_dir+str(img_id).zfill(6)+'.png', 0)
    
    vo.update(img, img_id)

    cur_t = vo.cur_t
    
    if(img_id > 2): 
        x, y, z = cur_t[0], cur_t[1], cur_t[2]
    else: 
        x, y, z = 0., 0., 0.
        
    #offset so the 2 trajectories do not overlap
    x_offset, y_offset = 0, 0
    draw_x, draw_y = int(x)+(290-x_offset), int(z)+(90-y_offset)
    #true_x, true_y = int(vo.trueX)+290, int(vo.trueZ)+90
    
    #for drawing error line
    predicted.append((x,y))
    #actual.append((vo.trueX, vo.trueY))
    
     
    cv2.circle(traj, (draw_x,draw_y), 1, (0,255,0), 1)
    #actual trajectory
    #cv2.rectangle(traj, (10, 20), (600, 60), (0,0,0), -1)

    #disaplying the current coordinates in the window     
    #text = "Coordinates: x=%2fm y=%2fm z=%2fm"%(x,y,z)
    #cv2.putText(traj, text, (20,40), cv2.FONT_HERSHEY_PLAIN, 1, 
    #            (255,255,255), 1, 8)
    #disaplying the current frame in the window     

    sec = time.time()
    curr_secs = sec - start
    curr_fps = img_id/curr_secs
    sec = time.time()
    curr_secs = sec - start
    frames_arr.append(curr_fps)
    
    #frame = "Frame: " + str(img_id) + " FPS: " + str(curr_fps)
    #cv2.putText(traj, frame, (20,60), cv2.FONT_HERSHEY_PLAIN, 1, 
    #            (255,255,255), 1, 8)
    #cv2.rectangle(traj, (10, 40), (600, 60), (0,0,0), -1)    
    
    #disaplying the current fps in the window     
    #fps = "FPS: " + str(curr_fps)
    #cv2.putText(traj, frame, (30,60), cv2.FONT_HERSHEY_PLAIN, 1, 
    #            (255,255,255), 1, 8)
    
    #cv2.imwrite('map%s.png' %(img_id), traj)
    cv2.imwrite('results/maps{!s}.png'.format(img_id), traj)
