
# -*- coding: utf-8 -*-
"""Module for example of listener."""

import sys
import os
import re
import csv
import numpy as np

def parasCameraLog(log_path):
    input_lane_heart = re.compile(r'read success')
    lane_valid = False
    lane_cnt = 0
    line_num = 0

    with open(log_path, 'r') as fp:
        lines = fp.readlines()
        line_nums = len(lines)        
        for line in lines:    
            line_num = line_num + 1
            if line_num > line_nums -3 :
                break   

            result_lane = input_lane_heart.findall(line)   # 
            if result_lane:
                lane_valid = True
                lane_cnt = 0
                print("-"*30)
                lane_size = line.split("camera")[-1].split(" ")[0].strip()
                print("camera", lane_size)
                continue

            if lane_valid:
                f0 = line.split()[0].strip()
                r0 = line.split()[-1].strip()
                if f0 == "k1" or f0 == "k2" or f0 == "k3" or f0 == "k4" or f0 == "k5" or f0 == "p1" or f0 == "p2":
                    f0 = "distortion"
                if f0 == "ksi":
                    f0 = "xi"
                ret = f0+": "+r0
                print(ret)
                lane_cnt = lane_cnt + 1
                if lane_cnt == 9:
                    lane_valid = False


       
if __name__ == '__main__':
    # log
    path_1 = "/home/one/src/baidu/baidu_calib_v1/anp_calibration/data/b_002/camera_param.txt"
    parasCameraLog(path_1)
