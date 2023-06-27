# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import os
import math
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip

camera_model = 1   # PINHOLE
M_K = np.float32([[1836.71,0.0,956.355],[0.0,1836.13,531.307],[0,0,1]])
M_D = np.float32([-0.377455,0.145382,-0.000328851,-8.23094e-05,0.0])
M_yaw = -1.5721246
M_pitch = -0.0
M_roll = -1.5604497
M_R = np.array([[-0.00132827,   0.0103423,    0.999946],
                [ -0.999994, -0.00308776,  -0.0012964],
                [0.00307419,   -0.999942,   0.0103464]])

M_t = np.array([5.23928, 0.0182697, 2.76158])


R_x = np.array([[1, 0, 0],
                [0, math.cos(M_roll), -math.sin(M_roll)],
                [0, math.sin(M_roll), math.cos(M_roll)]
                ])

R_y = np.array([[math.cos(M_pitch), 0, math.sin(M_pitch)],
                [0, 1, 0],
                [-math.sin(M_pitch), 0, math.cos(M_pitch)]
                ])

R_z = np.array([[math.cos(M_yaw), -math.sin(M_yaw), 0],
                [math.sin(M_yaw), math.cos(M_yaw), 0],
                [0, 0, 1]
                ])
S_R = np.dot(R_z, np.dot(R_y, R_x))

print("R \n", S_R)

def interested_region(img, vertices):
    if len(img.shape) > 2: 
        mask_color_ignore = (255,) * img.shape[2]
    else:
        mask_color_ignore = 255
    
    pz = np.zeros_like(img)
    
    cv.fillPoly(pz, vertices, mask_color_ignore)
    ret = cv.bitwise_and(img, pz)
        
    return ret

def weighted_img(img, initial_img, yaw=0.8, pitch=1., roll=0.):
    return cv.addWeighted(initial_img, yaw, img, pitch, roll)

def lines_drawn(img, lines, color=[255, 0, 0], thickness=6):
    global cache
    global first_frame
    slope_l, slope_r = [],[]
    lane_l,lane_r = [],[]
    yaw = 0.2
    min_len = img.shape[0]
    print("="*60)
    for line in lines:
        for x1,y1,x2,y2 in line:
            slope = (y2-y1)/(x2-x1)
            if slope > 1.3:
                slope_r.append(slope)
                lane_r.append(line)
                cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            elif slope < -1.6:
                slope_l.append(slope)
                lane_l.append(line)
                cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
        #2
        min_len = min(y1,y2,min_len)
        
    if((len(lane_l) == 0) or (len(lane_r) == 0)):
        print ('no lane detected')
        return 1
    #3
    slope_mean_l = np.mean(slope_l,axis =0)
    slope_mean_r = np.mean(slope_r,axis =0)
    mean_l = np.mean(np.array(lane_l),axis=0)
    mean_r = np.mean(np.array(lane_r),axis=0)
    
    if ((slope_mean_r == 0) or (slope_mean_l == 0 )):
        print('dividing by zero')
        return 1
    print("min len: ", min_len)
    # print("Line left: ", slope_mean_l, " ", mean_l, ",right: ", slope_mean_r, " ", mean_r)
    #6
    x1_l = int((min_len - mean_l[0][1] + (slope_mean_l * mean_l[0][0]))/slope_mean_l) 
    x2_l = int((img.shape[0] - mean_l[0][3] + (slope_mean_l * mean_l[0][2]))/slope_mean_l)   
    x1_r = int((min_len - mean_r[0][1] + (slope_mean_r * mean_r[0][0]))/slope_mean_r)
    x2_r = int((img.shape[0] - mean_r[0][3] + (slope_mean_r * mean_r[0][2]))/slope_mean_r)
    # print("Line Point x: ", x1_l, " ", x2_l, " ", x1_r, " ", x2_r)
    if x1_r > x1_l:     
        y1_l = int((slope_mean_l * x1_l ) + mean_l[0][1] - (slope_mean_l * mean_l[0][0]))
        y2_l = int((slope_mean_l * x2_l ) + mean_l[0][1] - (slope_mean_l * mean_l[0][0]))        
        y1_r = int((slope_mean_r * x1_r ) + mean_r[0][1] - (slope_mean_r * mean_r[0][0]))
        y2_r = int((slope_mean_r * x2_r ) + mean_r[0][1] - (slope_mean_r * mean_r[0][0]))
    else:
        y1_l = min_len
        y2_l = min_len
        y1_r = min_len
        y2_r = min_len
    
    # print("Line Point y: ", y1_l, " ", y2_l, " ", y1_r, " ", y2_r)
    present_frame = np.array([x1_l,y1_l,x2_l,y2_l,x1_r,y1_r,x2_r,y2_r],dtype ="float32")
    if first_frame == 1:
        next_frame = present_frame        
        first_frame = 0        
    else :
        prev_frame = cache
        next_frame = (1-yaw)*prev_frame+yaw*present_frame
             
    cv.line(img, (int(next_frame[0]), int(next_frame[1])), (int(next_frame[2]),int(next_frame[3])), color, thickness)
    cv.line(img, (int(next_frame[4]), int(next_frame[5])), (int(next_frame[6]),int(next_frame[7])), color, thickness)

    cache = next_frame
    # show_pic(img)
    # print("-"*60)
    ret1 = inverse_project(np.float32([next_frame[0], next_frame[1]]), M_K, M_D, S_R, M_t)
    ret2 = inverse_project(np.float32([next_frame[2], next_frame[3]]), M_K, M_D, S_R, M_t)
    ret3 = inverse_project(np.float32([next_frame[4], next_frame[5]]), M_K, M_D, S_R, M_t)
    ret4 = inverse_project(np.float32([next_frame[6], next_frame[7]]), M_K, M_D, S_R, M_t)
    print("-"*60)
    k_l = (ret1[1] - ret2[1]) / (ret1[0] - ret2[0])
    b_l = ret2[1] - k_l * ret2[0]
    deg_l = math.degrees(math.atan(k_l))
    print("left: ", deg_l, " ", b_l)    
    k_r = (ret3[1] - ret4[1]) / (ret3[0] - ret4[0])
    b_r = ret4[1] - k_l * ret4[0]
    deg_r = math.degrees(math.atan(k_r))
    print("right: ", deg_r, " ", b_r)     
    print("yaw diff: ", deg_l-deg_r, ", distance: ", b_l - b_r)         
    plt.plot([ret1[0],ret2[0]], [ret1[1],ret2[1]])
    plt.plot([ret3[0],ret4[0]], [ret3[1],ret4[1]])
    plt.show()
    
    
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    # show_pic(line_img)
    lines_drawn(line_img,lines)
    # show_pic(line_img)
    return line_img

def show_pic(img):
    cv.imshow("Img", img)
    cv.waitKey(1000)
    
    # plt.imshow(img)
    # plt.show()
    
def process_image(image):
    global first_frame
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    img_hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
    gray_channels = cv.split(img_hsv)
    
    lower_yellow = np.array([20, 100, 100], dtype = "uint8")
    upper_yellow = np.array([30, 255, 255], dtype = "uint8")
    
    mask_yellow = cv.inRange(img_hsv, lower_yellow, upper_yellow)
    mask_white = cv.inRange(gray_image, 230, 255)
    mask_yw = cv.bitwise_or(mask_white, mask_yellow)
    mask_yw_image = cv.bitwise_and(gray_image, mask_yw)
    
    gauss_gray = cv.GaussianBlur(mask_yw_image, (5, 5), 0)
    canny_edges = cv.Canny(gauss_gray, 50, 150)
    
    imshape = image.shape
    # print("image shape: ", imshape)
    lower_left = [imshape[1]/9,imshape[0]]
    lower_right = [imshape[1]-imshape[1]/9,imshape[0]]
    top_left = [imshape[1]/2-imshape[1]/8,imshape[0]/2+imshape[0]/10]
    top_right = [imshape[1]/2+imshape[1]/8,imshape[0]/2+imshape[0]/10]
    vertices = [np.array([lower_left,top_left,top_right,lower_right],dtype=np.int32)]
    roi_image = interested_region(canny_edges, vertices)
    # print("roi vertices: \n", vertices)
    
    theta = np.pi/180
    rho = 1.0
    threshold = 30
    min_line_len = 100
    max_line_gap = 180
        
    line_image = hough_lines(roi_image, rho, theta, threshold, min_line_len, max_line_gap)
    result = weighted_img(line_image, image, yaw=0.8, pitch=1., roll=0.)
    return result
    
def inverse_project(img_pt, K_, distCoeffs, R_, t_):
    undistort_pts = cv.undistortPoints(img_pt, K_, distCoeffs)
    # print("image points: ", img_pt)
    # print("undistort points: ", undistort_pts[0][0])
    pc_3d = np.array([undistort_pts[0][0][0], undistort_pts[0][0][1], 1])
    point_3d = np.dot(R_, pc_3d)
    obj_pt = []

    obj_pt.append(point_3d[0] * (-t_[2]) / point_3d[2] + t_[0])
    obj_pt.append(point_3d[1] * (-t_[2]) / point_3d[2] + t_[1])
    obj_pt.append(0)  
    # print("ground points: ", obj_pt[0], " ", obj_pt[1])  
    return obj_pt     
    
if __name__ == '__main__':
    if True:
        global first_frame
        first_frame = 1
        file_path = "/home/one/calib_data/C/C03/front_middle_camera/"
        for i in range(10):
            idx = i + 1
            file_name = str(idx)+".bmp"
        
            img = cv.imread(file_path+file_name)
            pic = cv.cvtColor(img, cv.COLOR_BGR2RGB)     
            # img_ = Image.fromarray(pic)    
            img_o = process_image(pic)
            # show_pic(img_o)

    if False:
        p_l = np.float32([748, 877])
        p_r = np.float32([1194, 877])
        p_d = [20.4552,1.7448,20.4883,-2.0208]
        ret1 = inverse_project(p_l, M_K, M_D, M_R, M_t)
        print(ret1)
        ret2 = inverse_project(p_r, M_K, M_D, M_R, M_t)
        print(ret2)
                