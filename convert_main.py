# -*- coding: UTF-8 -*-

import imp
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
# import tools.marker_data.Marker_0 as m
from tools.marker_data import Marker_0
import tools.marker_process as cp

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

def plot2d(p1,p2,p3,p4):
    fig = plt.figure()
    plt.scatter(p1[0],p1[1],color='b')
    plt.scatter(p2[0],p2[1],color='b')
    plt.scatter(p3[0],p3[1],color='b')
    plt.scatter(p4[0],p4[1],color='b')    
    plt.xlabel('X Axes')
    plt.ylabel('Y Axes')
    plt.show()

def deg2rad(d):
    deg = d[0] + d[1]/60.0 + d[2]/3600.0
    # print("deg: ", deg)
    return math.radians(deg)    #2*math.pi

def init():
    _ZA_ = [90,0,0]
    _HAR_ = [0,0,0]

def marker_point(H,ZA,HAR,V,S,bias):
    ret = []
    # print("+" * 40)
    # print("bias: ", bias)

    ZA_ = deg2rad(ZA)
    HAR_ = deg2rad(HAR)
    V_H = V*math.tan(ZA_)
    H1 = math.sqrt(S*S - V*V)
    Hx = H1*math.cos(HAR_)
    Hy = -H1*math.sin(HAR_)    
    ret.append(Hx+bias[0])
    ret.append(Hy)
    ret.append(V+bias[1])

    print("-"*60)
    print("ZA_ : ", ZA_)
    print("HAR_ : ", HAR_)
    print("V-H:",V_H, ",H:",H, ",H1:", H1)
    print("H error: ", H1-H)
    return ret


def markerdata():
    # offset 
    print("---->> the point of marker: ", len(m.HAR))
    for h in range(len(m.HAR)):      
        result = np.sum([m.HAR[h], m.init_offset], axis=0).tolist()
        m.HAR[h] = result    

    ret1 = marker_point(m.H[0],m.ZA[0],m.HAR[0],m.V[0],m.S[0],m.init_center)
    print("The vehicle of marker_left_1 data: ", ret1)
    ret2 = marker_point(m.H[1],m.ZA[1],m.HAR[1],m.V[1],m.S[1],m.init_center)
    print("The vehicle of marker_left_2 data: ", ret2)
    ret3 = marker_point(m.H[2],m.ZA[2],m.HAR[2],m.V[2],m.S[2],m.init_center)
    print("The vehicle of marker_left_3 data: ", ret3)
    ret4 = marker_point(m.H[3],m.ZA[3],m.HAR[3],m.V[3],m.S[3],m.init_center)
    print("The vehicle of marker_left_4 data: ", ret4)

    plotf(ret1,ret2,ret3,ret4)
    # plot2d([m.H[0],m.V[0]],[m.H[1],m.V[1]],[m.H[2],m.V[2]],[m.H[3],m.V[3]])

    point4 = [ret1,ret2,ret3,ret4]
    return point4

if __name__ == '__main__':
    ret = markerdata()
    B_s = np.array(ret)
    print("-" * 60)
    print("four point: ", B_s.shape)
    print(B_s)
    T,R,t = cp.computer_translate(m.M_,B_s)

    # convert eular
    y1, p1, r1 = cp.convert_eular(R)
    print("-" * 40)
    print("euler_order: XYZ")
    print("yaw:", y1)
    print("pitch:", p1)
    print("roll:", r1)    