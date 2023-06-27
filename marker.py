# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#encoding:UTF-8

from tokenize import Double
import numpy as np
import math
import csv
import matplotlib as mpl
mpl.use('TkAgg')    # middle of matplotlib
import matplotlib.pyplot as plt

def get_radar_data(path, t, s, x, y, z, xf, yf, zf, err):
    # 读取外部数据
    print("-" * 40)
    print("read file: ", path)
    period = 5
    id = []
    with open(path) as file:
        lines = csv.reader(file)
        head = next(lines)
        for line in lines:
            t.append(int(line[0]))
            s.append(float(line[2])/1000.0)
            x.append(float(line[3]))
            y.append(float(line[4]))
            z.append(float(line[5]))
            xf.append(float(line[6]))
            yf.append(float(line[7]))
            zf.append(float(line[8]))
            err.append(float(line[9]))       


def main(path_) :
    x = []
    y = []
    z = []
    x_f = []
    y_f = []
    z_f = []
    time = []
    sa = []
    err = []
    get_radar_data(path_, time, sa, x, y, z, x_f, y_f, z_f, err)

    plt.figure(num=3,figsize=(8,5))
    plt.title('Marker')
    plt.xlabel('x')
    plt.ylabel('y') 
    plt.plot(time, x, marker='.', c='g')
    plt.plot(time, y, marker='o', c='b')
    plt.plot(time, z, marker='x', c='r')

    plt.plot(time, x_f, marker='8', c='g')
    plt.plot(time, y_f, marker='s', c='b')
    plt.plot(time, z_f, marker='p', c='r')

    # plt.plot(time, sa, marker='+', c='y') 

    plt.grid() 
    plt.show() 


    plt.figure(num=3,figsize=(8,5))
    plt.title('Error')
    # tx = 
    plt.plot(err, marker='8', c='g')

    plt.grid() 
    plt.show()     



if __name__ == "__main__":
    _path = "../output.csv"
    main(_path)