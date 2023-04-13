
# -*- coding: utf-8 -*-
"""Module for example of listener."""
"usage: python3 diff_tool.py -f1 ../configs/dw_anp/hardware_configs/BASE/lane.log "

import sys
import os
import time
import re
import argparse
import csv
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def parasLog(log_path):
    lane_heart = re.compile(r'LANELOG-DRAW input-LaneLines-size')
    line_num = 0
    lane_valid = False
    coffe_num = 0
    lane_param = []
    with open(log_path, 'r') as fp:
        lines = fp.readlines()
        for line in lines:           
            result_lane = lane_heart.findall(line)
            if result_lane:
                lane_size = line.split("size: ")[-1].split(" ")[0].strip()
                timestamp = line.split("stamp: ")[-1].strip()
                lane_valid = True
                line_num = line_num + 1
                if True:
                    print("-"*60)
                    print("lane num:", line_num, ",timestamp:", timestamp, ",size:", lane_size)
                continue

            if lane_valid:
                curve_min = line.split("curve(min,max): ")[-1].split(" ")[0].strip()
                curve_max = line.split("curve(min,max): ")[-1].split(" ")[1].strip()
                position = line.split("position: ")[-1].split(" ")[0].strip()
                coeff_0 = line.split("coeffs: ")[-1].split(" ")[0].strip()
                coeff_1 = line.split("coeffs: ")[-1].split(" ")[1].strip()
                coeff_2 = line.split("coeffs: ")[-1].split(" ")[2].strip()
                coeff_3 = line.split("coeffs: ")[-1].split(" ")[3].strip()
                lane_id =  line.split("id: ")[-1].split(" ")[0].strip()
                lane_param.append([float(curve_min), float(curve_max), float(coeff_0), float(coeff_1), float(coeff_2), float(coeff_3)])

                coffe_num = coffe_num + 1
                if coffe_num == int(lane_size):
                    coffe_num = 0
                    lane_valid = False
                    plot_total(lane_param)
                    lane_param.clear()
                    
                print("lane sub:",coffe_num,",curve:[",curve_min, " ", curve_max,"],position:", position,",id:", lane_id,",coeffs: ", coeff_0, " ", coeff_1, " ", coeff_2, " ", coeff_3)
            line_num = line_num + 1

def plot_lane(c0,c1,c2,c3,min,max):
    c_min = float(min)
    c_max = float(max)
    x = np.linspace(int(c_min), int(c_max))
    y = float(c0) + float(c1)*x + float(c2)*pow(x,2) + float(c3)*pow(x,3)
    plt.plot(x, y, 'k-')
    # plt.grid()
    # plt.show()

def plot_total(param):
    plt.xlabel('Horizontal')
    plt.ylabel('Vertical')
    plt.xlim([-9, 9])
    plt.ylim([0, 70])
    plt.plot(0,0.5,'o')
    plt.grid()
    for i in range(len(param)):
        c_min = int(param[i][0])
        c_max = int(param[i][1])
        x = np.linspace(int(c_min), int(c_max))
        y = float(param[i][2]) + float(param[i][3])*x + float(param[i][4])*pow(x,2) + float(param[i][5])*pow(x,3)
        plt.plot(y, x, 'k-')
    plt.pause(1)
    # plt.show()
    plt.clf()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', type=str, default = '/home/one/calib_data/B/B04/log/')
    args = parser.parse_args()

    path_1 = args.f1 + "pavaro.EM_LANE.log"
    parasLog(path_1)
