import sys
import os
import time,datetime
import re
import argparse
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# timestamp_sec,current_lateral_error,current_ref_heading,
# current_heading,current_heading_error,heading_error_rate,
# lateral_error_rate,current_curvature,steer_angle_feedforward,
# steer_angle_lateral_contribution,steer_angle_lateral_rate_contribution,
# steer_angle_heading_contribution,steer_angle_heading_rate_contribution,
# steer_angle_feedback,steer_angle,steer_angle_before_pid,steer_angle_before_model,
# steering_position,current_speed,flc_part_feedforward,flc_part_heading_error,
# flc_part_lateral_error,flc_part_roll_angle,integrator_contribution,steer_angle_pid,position_x,
# position_y,angle_heading,target_point_x,target_point_y,target_point_heading,lateral_velocity,
# roll_angle,flc_heading_error_bias,wheel_angle,steer_ratio,mpc_steer_angle,heading_err_compensation,
# steering_compensation,angular_velocity,acceleration_x,acceleration_y,lateral_error_raw,d_rate,
# intergral_steer_angle,lat_override,
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False 

def process(path, id):
    # 读取外部数据
    print("-" * 40)
    print("read file: ", path)
    ydata = []
    xdata = []
    
    data = pd.read_csv(path,encoding='gbk')
    # xdata = data.iloc[:,0]
    xdata = data.loc[:, 'timestamp_sec']
    x_time = range(len(xdata))
    curvature_data = data.loc[:, 'current_curvature']
    heading_data = data.loc[:, 'current_heading_error']
    lateral_data = data.loc[:, 'current_lateral_error']
    print(len(lateral_data))
    plt.figure(1)
    
    plt.sca(plt.subplot(3, 1, 1))
    plt.title(u'current_curvature', size=10)
    plt.legend()
    plt.plot(x_time, curvature_data, color='b')
    plt.ylabel('y',size=10)
    plt.ylim(-0.0006,0.0006)
    plt.grid()
    
    plt.sca(plt.subplot(3, 1, 2))
    plt.title(u'current_heading_error', size=10)
    plt.legend()
    plt.plot(x_time, heading_data, color='b')
    plt.ylabel('y',size=10)
    plt.grid()
    
    plt.sca(plt.subplot(3, 1, 3))
    plt.title(u'current_lateral_error', size=10)
    plt.legend()
    plt.plot(x_time, lateral_data, color='b')
    plt.xlabel('x',size=10)
    plt.ylabel('y',size=10)
    plt.grid()
    plt.savefig('../'+id+'.jpg')
    plt.show()     
            
if __name__ == '__main__':
    car_id = "b04"
    # file = "/home/one/calib_data/1801/1801_5/ica/mlog/log-0/HAVP/lat_controller_log_2023-07-06_110555.csv"
    file = sys.argv[1]
    process(file, car_id)