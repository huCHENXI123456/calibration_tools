
# -*- coding: utf-8 -*-
"""Module for example of listener."""
"usage: python3 diff_tool.py -f1 ../configs/dw_anp/hardware_configs/BASE/hardware_config.prototxt "
"    -f2 ../configs/dw_anp/hardware_configs/DW/hardware_config.prototxt"
import sys
import os
import time
import re
import argparse
import csv
import numpy as np
import pandas as pd
import math
from flask import Flask, render_template

app = Flask(__name__)

cam_name = ["front_wide_camera", "front_long_camera", "front_middle_camera",
            "left_front_camera", "right_front_camera", "left_rear_camera", "right_rear_camera"]
cam_param = ["name","yaw","pitch","roll","x","y","z"]
cam_param_1 = [[],[],[],[]] # item,base,b_002,error

wheel_base = 5.17

def find_camera(line,cam_n):
    r1 = re.findall(pattern=cam_n, string=line, flags=re.S)
    return r1

def add_item(id):
    cam_param_1[id].append("name")
    cam_param_1[id].append("yaw")
    cam_param_1[id].append("pitch")
    cam_param_1[id].append("roll")
    cam_param_1[id].append("x")
    cam_param_1[id].append("y")
    cam_param_1[id].append("z") 

# find camera name, and offset 15 is rotation and translate
def save_param_col(lines, i, j):
    cam_param_1[j].append(lines[i].strip().lstrip("name:").strip())
    cam_param_1[j].append(lines[i+15].strip().lstrip("yaw:").strip())
    cam_param_1[j].append(lines[i+16].strip().lstrip("pitch:").strip())
    cam_param_1[j].append(lines[i+17].strip().lstrip("roll:").strip())
    cam_param_1[j].append(lines[i+20].strip().lstrip("x:").strip())
    cam_param_1[j].append(lines[i+21].strip().lstrip("y:").strip())
    cam_param_1[j].append(lines[i+22].strip().lstrip("z:").strip()) 

def cameras_extrinsic_col(path, k, item):
    i = 0

    with open(path, 'r') as fp:
        lines = fp.readlines()
        for line in lines:    
            for j in range(len(cam_name)):     
                ret_all = find_camera(line,cam_name[j])
                if ret_all:
                    if item:
                        add_item(0)   # first colume add item
                    save_param_col(lines, i, k)   # data

            i = i + 1
        fp.close()

def write_file(i_param, file_name):
    str = '\n'
    fp = open(file_name,"w")
    for i in range(len(i_param[0])):
        for j in range(len(i_param)):
            fp.write(i_param[j][i]+",")
        fp.write("\n")
    fp.close()

def diff_statify(id):
    for i in range(len(cam_param_1[0])):
        if i%7 == 0:
            cam_param_1[id].append("error(degree)(m)")
        elif i%7 == 1 or i%7 == 2 or i%7 == 3:  # rotation
            cam_param_1[id].append(str(math.degrees(float(cam_param_1[1][i]) - float(cam_param_1[2][i]))))    # 
        else:   # translate
            cam_param_1[id].append(str(float(cam_param_1[1][i]) - float(cam_param_1[2][i])))

@app.route('/')
def index():
    return render_template('result.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', type=str, default = '../configs/dw_anp/hardware_configs/BASE_REAR')
    parser.add_argument('-f2', type=str, default = "../data/n_007")

    args = parser.parse_args()

    path_1 = args.f1 + "/hardware_config.prototxt"
    path_2 = args.f2 + "/hardware_config.prototxt"

    file_name = "../n_005.csv"
    cameras_extrinsic_col(path_1, 1, True)   # add title
    cameras_extrinsic_col(path_2, 2, False)
    diff_statify(3)
    write_file(cam_param_1, file_name)

    a = pd.read_csv(file_name)
    a.to_html("templates/result.html")

    app.run(debug=True)
