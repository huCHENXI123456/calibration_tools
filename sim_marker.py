# -*- coding: UTF-8 -*-
import sys
sys.path.append('tools')
import math
import yaml
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import marker_data as m_c
import marker_process as m_p

# 绘制四个角点
def plotf(p1,p2,p3,p4):
    #3D Plotting
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter(p1[0],p1[1],p1[2],color='b')
    ax.scatter(p2[0],p2[1],p2[2],color='g')
    ax.scatter(p3[0],p3[1],p3[2],color='r')
    ax.scatter(p4[0],p4[1],p4[2],color='y')
    #Labeling
    ax.set_xlabel('X Axes')
    ax.set_ylabel('Y Axes')
    ax.set_zlabel('Z Axes')
    plt.show()

def deg2rad(d):
    deg = d[0] + d[1]/60.0 + d[2]/3600.0
    # print("deg: ", deg)
    return math.radians(deg)    #2*math.pi

if __name__ == '__main__':

    if True:
        ret = []
        ret.append([10.95237785474636, 1.0869273542792774, 2.365])
        ret.append([11.029851298424308, 0.39049773429881385, 2.365])
        ret.append([10.96338218571466, 1.0871188093896813, 2.066])
        ret.append([11.041712795996407, 0.39263098353105846, 2.065])

        print(">>>>>> The car of marker position: ")
        print("the leftFront of 1: ", ret[0])
        print("the rightFront of 2: ", ret[1])
        print("the leftDown of 3: ", ret[2])
        print("the rightDown of 4: ", ret[3])


        B_s = np.array(ret)
        T,R,t = m_p.computer_translate(m_c.M_I, B_s)
        y1, p1, r1 = m_p.convert_eular(R)
        euler_out = m_p.rot_to_eular(R)
        
