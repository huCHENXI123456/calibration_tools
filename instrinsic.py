# -*- coding: utf-8 -*-

import numpy as np
import math

image_size = [1920, 1080]

def instrins_computer(name, camera_fov):
    f_c =[ math.radians(camera_fov[0]/2), math.radians(camera_fov[1]/2) ]
    f_x = image_size[0] / (2*math.tan(f_c[0]))
    f_y = image_size[1] / (2*math.tan(f_c[1]))
    print("name: ", name)
    print("x0: 0")
    print("fx: ", f_x)
    print("fy: ", f_y)
    print("cx: ", image_size[0]/2)
    print("cy: ", image_size[1]/2)    
    print("distortion: 0.0")    
    print("distortion: 0.0")
    print("distortion: 0.0")
    print("distortion: 0.0")
    print("distortion: 0.0")

if __name__ == '__main__':
    front_middle_camera = [61.2,34]
    front_long_camera   = [28.1, 15.9]
    front_wide_camera   = [118.4, 62.8]

    left_front_camera   = [118.4, 62.8]
    right_front_camera  = [118.4, 62.8]
    left_rear_camera    = [85.5, 47.3]
    right_rear_camera   = [85.5, 47.3]
    instrins_computer('front_middle_camera', front_middle_camera)
    instrins_computer('front_long_camera', front_long_camera)
    instrins_computer('front_wide_camera', front_wide_camera)
    instrins_computer('left_front_camera', left_front_camera)
    instrins_computer('right_front_camera', right_front_camera)
    instrins_computer('left_rear_camera', left_rear_camera)
    instrins_computer('right_rear_camera', right_rear_camera)
 

