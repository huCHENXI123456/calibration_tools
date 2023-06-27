
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

def parasEmOutLog(log_path):
    output_lane_heart = re.compile(r'LANELOG-DRAW output_LaneLines_size')
    inital_time = 1678780873.071529
    line_num = 0
    lane_valid = False    
    lane_left = []
    lane_right = []
    coffe_num = 0
    with open(log_path, 'r') as fp:
        lines = fp.readlines()
        line_nums = len(lines)        
        for line in lines:           
            result_lane = output_lane_heart.findall(line)   # 
            if result_lane:
                lane_size = line.split("output_LaneLines_size: ")[-1].split(" ")[0].strip()
                if int(lane_size) == 2: # two line
                    lane_valid = True
                line_num = line_num + 1
                if True:
                    print("-"*60)
                    print("lane output size:", lane_size)
                continue
            if lane_valid:
                coeff_0 = line.split("coeffs: ")[-1].split(" ")[0].strip()
                coeff_1 = line.split("coeffs: ")[-1].split(" ")[1].strip()
                coeff_2 = line.split("coeffs: ")[-1].split(" ")[2].strip()
                position = line.split("position: ")[-1].split(" ")[0].strip()
                print("position: ", position, ",c0:", coeff_0, ",c2:", coeff_2)
                if int(position) == 1:
                    lane_left.append([int(position), float(coeff_0), float(coeff_1), float(coeff_2)])
                if int(position) == -1:
                    lane_right.append([int(position), float(coeff_0), float(coeff_1), float(coeff_2)])

                coffe_num = coffe_num + 1
                if coffe_num == int(lane_size):
                    coffe_num = 0
                    lane_valid = False
            line_num = line_num + 1
            if line_num > line_nums -3 :
                break

    return lane_right, lane_left

def parasEmLog(log_path):
    input_lane_heart = re.compile(r'LANELOG-DRAW input-LaneLines-size')
    line_num = 0
    lane_valid = False
    coffe_num = 0
    lane_param = []
    position_coffes_r = []
    position_coffes_l = []
    inital_time = 1678780873.071529
    both_position = [0,0,0,0,0,0,0,0]
    all_both_position = []
    with open(log_path, 'r') as fp:
        lines = fp.readlines()
        line_nums = len(lines)        
        for line in lines:           
            result_lane = input_lane_heart.findall(line)   # 
            if result_lane:
                lane_size = line.split("size: ")[-1].split(" ")[0].strip()
                timestamp = line.split("stamp: ")[-1].strip()
                if int(lane_size) > 0:
                    lane_valid = True
                line_num = line_num + 1
                if True:
                    print("-"*60)
                    print("lane num:", line_num, ",timestamp:", timestamp, ",size:", lane_size)
                continue
            # one lane
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
                if int(position) == 1:
                    position_coffes_l.append([float(timestamp), int(position),float(coeff_0), float(coeff_1), float(coeff_2)])
                    both_position[0] = float(timestamp)
                    both_position[1] = int(position)
                    both_position[2] = float(coeff_1)
                    both_position[3] = float(coeff_2)

                if int(position) == -1:
                    position_coffes_r.append([float(timestamp), int(position),float(coeff_0), float(coeff_1), float(coeff_2)])
                    both_position[4] = float(timestamp)
                    both_position[5] = int(position)
                    both_position[6] = float(coeff_1)
                    both_position[7] = float(coeff_2)                

                print("lane sub:",coffe_num,",curve:[",curve_min, " ", curve_max,"],position:", position,",id:", lane_id,",coeffs: ", coeff_0, " ", coeff_1, " ", coeff_2, " ", coeff_3)
                coffe_num = coffe_num + 1
                if coffe_num == int(lane_size):
                    coffe_num = 0
                    lane_valid = False
                    ## Display current lane line
                    # plot_total(lane_param)
                    lane_param.clear()
                    if both_position[1] == 1 and both_position[5] == -1:
                        all_both_position.append(both_position)
                        both_position = [0,0,0,0,0,0,0,0]
                    
                
            line_num = line_num + 1
            if line_num > line_nums -3 :
                break
    return position_coffes_r, position_coffes_l, all_both_position

def save_csv_1(data_0, data_1):
    np.savetxt("../out_both.csv",
            data_0,
            delimiter =", ", 
            fmt ='%s') 

def save_csv(data_c0, data_c1, data_all):
    np.savetxt("../left.csv", 
            data_c0,
            delimiter =", ", 
            fmt ='% s')
    np.savetxt("../right.csv", 
            data_c1,
            delimiter =", ", 
            fmt ='%s')                 

    np.savetxt("../both.csv",
            data_all,
            delimiter =", ", 
            fmt ='%s')

def plot_total(param):
    plt.xlabel('Horizontal')
    plt.ylabel('Vertical')
    plt.xlim([-9, 9])
    plt.ylim([0, 90])
    plt.plot(0,0.5,'o')
    plt.grid()
    for i in range(len(param)):
        c_min = int(param[i][0])
        c_max = int(param[i][1])
        x = np.linspace(int(c_min), int(c_max))
        y = float(param[i][2]) + float(param[i][3])*x + float(param[i][4])*pow(x,2) + float(param[i][5])*pow(x,3)
        plt.plot(y, x, 'k-')
    plt.pause(0.5)
    # plt.show()
    plt.clf()

def plot_coffes(param_0, param_1):

    plt.figure(num='c1-c2', figsize=(14,8))

    plt.subplot(2, 2, 1)
    plt.title("c1_l")
    plt.ylim([-0.5, 0.5])
    for i in range(len(param_0)):
        plt.scatter(i, param_0[i][3], marker='.', c='g')
    plt.grid()

    plt.subplot(2, 2, 3)
    plt.title("c1_r")
    plt.ylim([-0.5, 0.5])
    for i in range( len(param_1)):
        plt.scatter(i, param_1[i][3], marker='.', c='b')
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.title("c2_l")
    plt.ylim([-0.05, 0.05])
    for i in range(len(param_0)) :
        plt.scatter(i, param_0[i][4], marker='.', c='r')
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.title("c2_r")
    plt.ylim([-0.05, 0.05])
    for i in range(len(param_1)) :
        plt.scatter(i, param_1[i][4], marker='.', c='b')
    plt.grid()

    plt.show()

def plot_coffes_both_c2(params) :
    plt.figure(num='c2-c2', figsize=(14,8))
    x0 = []
    y0 = []
    y1 = []
    for i in range(len(params)):
        x0.append(i)
        y0.append(float(params[i][3]))

    for i in range(len(params)):
        y1.append(float(params[i][7]))

    plt.subplot(1, 2, 1)
    plt.title("c2_l")
    plt.ylim([-0.05, 0.05])   
    plt.plot(x0,y0)
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.title("c2_r")
    plt.ylim([-0.05, 0.05])
    plt.plot(x0,y1)
    plt.grid()

    plt.show()


def plot_coffes_both_c1(params) :
    plt.figure(num='c1-c1', figsize=(14,8))
    x0 = []
    y0 = []
    y1 = []
    for i in range(len(params)):
        x0.append(i)
        y0.append(float(params[i][2]))

    for i in range(len(params)):
        y1.append(float(params[i][6]))

    plt.subplot(1, 2, 1)
    plt.title("c1_l")
    plt.ylim([-0.5, 0.5])   
    plt.plot(x0,y0)
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.title("c1_r")
    plt.ylim([-0.5, 0.5])
    plt.plot(x0,y1)
    plt.grid()

    plt.show()


       
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', type=str, default = '/home/one/Downloads/n_04HAVP_slave/opt/log/HAVP/')
    args = parser.parse_args()
    # log
    path_1 = args.f1 + "pavaro.EM_LANE.log"
    c_r, c_l, c_all = parasEmLog(path_1)
    o_r, o_l = parasEmOutLog(path_1)

    # save
    # save_csv(c_r, c_l, c_all)
    # save_csv_1(c_r, c_l)
    # display
    plot_coffes_both_c2(c_all)
    # plot_coffes(c_r, c_l)