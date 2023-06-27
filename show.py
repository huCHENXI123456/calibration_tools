# -*- coding: UTF-8 -*-
import numpy as np
import os
import cv2

path = '/home/one/calib_data/test/slave'
channel = '2'
init = 0
showname = "camera_" + channel
cv2.namedWindow(showname, cv2.WINDOW_FULLSCREEN)
for dir in os.listdir(path):
    if dir.split(".")[0].split("_")[0] == '2':
        index = dir.split(".")[0].split("_")[1]
        child_path = os.path.join(path, dir)
        print("filename: {}".format(index))
        print("filepath: {}".format(child_path))

        img = cv2.imread(child_path, cv2.IMREAD_COLOR)
        size = img.shape
        print("image size: ", size)
        cv2.circle(img, (size[1]/2, size[0]/2), 10, (255,0,0), 2)
        cv2.line(img, (0,size[0]/2), (size[1], size[0]/2), (0,0,255), 3)
        cv2.line(img, (size[1]/2, 0), (size[1]/2, size[0]), (0,0,255), 3)
        cv2.imshow(showname, img)
        key = cv2.waitKey()
        
        if key == "q" or key == 27:
            break    
