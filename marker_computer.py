# -*- coding: UTF-8 -*-
import sys
sys.path.append('tools')
import math
import yaml
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
# import tools.marker_data.Marker_0 as m
# from tools.marker_data import Marker_0
import marker_data as m_c
import marker_process as m_p
import marker_station as m_s

# 绘制四个角点
def plota(p, name):
    #3D Plotting
    fig = plt.figure(name)
    ax = plt.axes(projection="3d")
    ax.scatter(p[0][0],p[0][1],p[0][2],color='b')
    ax.scatter(p[1][0],p[1][1],p[1][2],color='g')
    ax.scatter(p[2][0],p[2][1],p[2][2],color='r')
    ax.scatter(p[3][0],p[3][1],p[3][2],color='y')
    #Labeling
    ax.set_xlabel('X Axes')
    ax.set_ylabel('Y Axes')
    ax.set_zlabel('Z Axes')
    plt.show()

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

# vehicle coordinates 车辆坐标
def marker_point(H,ZA,HAR,V,S,bias):
    point = []
    ZA_ = deg2rad(ZA)
    HAR_ = deg2rad(HAR)
    V_H = V*math.tan(ZA_)
    H1 = math.sqrt(S*S - V*V)
    Hx = H1*math.cos(HAR_)
    Hy = -H1*math.sin(HAR_)    
    point.append(Hx+bias[0])
    point.append(Hy+bias[1])
    point.append(V+bias[2])
    if False:
        print("-"*60)
        print("ZA_ : ", ZA_)
        print("HAR_ : ", HAR_)
        print("H:",H, ",H1:", H1)
        print("H error: ", H1-H)
    if True:
        print("-"*40)
        print(point[0], " ", point[1], " ", point[2])

    return point

def norm_2(p1,p2):
    dist = np.sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]),2) + pow((p1[2]-p2[2]),2))
    return dist

def markerdata(m0):
    # offset 
    print("------------------- ", m0.name, " -----------------")
    for h in range(m_c.POINT_N):      
        # result = np.sum([m0.HAR[h], m0.init_angle_h], axis=0).tolist()
        m0.HAR[h][0] = m0.HAR[h][0] - m0.init_angle_h[0]   # 度
        m0.HAR[h][1] = m0.HAR[h][1] - m0.init_angle_h[1]   # 分
        m0.HAR[h][2] = m0.HAR[h][2] - m0.init_angle_h[2]   # 秒

        m0.ZA[h][0] = -m0.ZA[h][0] + m0.init_angle_v[0]   # 度
        m0.ZA[h][1] = -m0.ZA[h][1] + m0.init_angle_v[1]   # 分
        m0.ZA[h][2] = -m0.ZA[h][2] + m0.init_angle_v[2]   # 秒        
    ret1 = marker_point(m0.H[0],m0.ZA[0],m0.HAR[0],m0.V[0],m0.S[0],m0.init_position)
    ret2 = marker_point(m0.H[1],m0.ZA[1],m0.HAR[1],m0.V[1],m0.S[1],m0.init_position)
    ret3 = marker_point(m0.H[2],m0.ZA[2],m0.HAR[2],m0.V[2],m0.S[2],m0.init_position)
    ret4 = marker_point(m0.H[3],m0.ZA[3],m0.HAR[3],m0.V[3],m0.S[3],m0.init_position)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    pointSet = [ret1,ret2,ret3,ret4]
    return pointSet

def markerpostion(m0):
    print("------------------- ", m0.name, " -----------------")
    # 测量位置为前轴中心点，标定使用后轴中心点
    ret1 = [m0.position[0][0]+m0.init_position[0], m0.position[0][1], m0.position[0][2]]
    ret2 = [m0.position[1][0]+m0.init_position[0], m0.position[1][1], m0.position[1][2]]
    ret3 = [m0.position[2][0]+m0.init_position[0], m0.position[2][1], m0.position[2][2]]
    ret4 = [m0.position[3][0]+m0.init_position[0], m0.position[3][1], m0.position[3][2]]

    pointSet = [ret1,ret2,ret3,ret4]
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print("error1: ", 0.7615773 - norm_2(ret1, ret4), ",error2: ", 0.7615773 - norm_2(ret2, ret3))        
    return pointSet

def markerComponent(m0, yaw, offset):
    print("test")    

if __name__ == '__main__':
    print(">>>>>>>>>>>>> CAR ID: ", m_c.CAR_ID)
    ret = []
    ###########################################
    file_name = m_c.CAR_ID + "_" + str(m_c.station_id) + '.prototxt'
    file_name_n = m_c.CAR_ID + "_" + str(m_c.station_id) + '_c.prototxt'
    # Marker of station, adjust the number of marker class
    # step 1: define class
    m0 = m_c.FrontMarker_0()   # P1
    m1 = m_c.FrontMarker_1()   # P2    
    m2 = m_c.FrontMarker_2()   # P3
    m3 = m_c.FrontMarker_3()   # P4
    m4 = m_c.LeftMarker_F0()   # P5   
    m5 = m_c.LeftMarker_R0()   # P6 
    m6 = m_c.RightMarker_F0()  # P7 
    m7 = m_c.RightMarker_R0()  # P8 
    # add rear
    m8 = m_c.LeftMarker_M0()   # P9
    m9 = m_c.RightMarker_M0()  # P10 
    # add fisheye
    m10 = m_c.FrontFishMarker_F0()      # F1
    m11 = m_c.LeftFishMarker_L0()       # F2
    m12 = m_c.LeftFishMarker_L1()       # F3
    m13 = m_c.RightFishMarker_R0()      # F4
    m14 = m_c.RightFishMarker_R1()      # F5

    ret.append(markerpostion(m0))    
    ret.append(markerpostion(m1))
    ret.append(markerpostion(m2))
    ret.append(markerpostion(m3))
    ret.append(markerpostion(m4))
    ret.append(markerpostion(m5))
    ret.append(markerpostion(m6))
    ret.append(markerpostion(m7))          
    ret.append(markerpostion(m8))
    ret.append(markerpostion(m9)) 
    ret.append(markerpostion(m10)) 
    ret.append(markerpostion(m11)) 
    ret.append(markerpostion(m12)) 
    ret.append(markerpostion(m13)) 
    ret.append(markerpostion(m14)) 
        
    if True:
        plota(ret[0], m0.name)
        plota(ret[1], m1.name)
        plota(ret[2], m2.name)
        plota(ret[3], m3.name)
        plota(ret[4], m4.name)
        plota(ret[5], m5.name)
        plota(ret[6], m6.name)
        plota(ret[7], m7.name)   
    if False: 
        plota(ret[8], m8.name)
        plota(ret[9], m9.name)
    if True:
        plota(ret[10], m10.name)
        plota(ret[11], m11.name)
        plota(ret[12], m12.name)
        plota(ret[13], m13.name)
        plota(ret[14], m14.name)                      


    print("#"*60)
    if False:
        print("The lenght of marker nums: ", len(ret))
        for i in range(len(ret)):
            print(">>>>>> The car of marker position: ")
            print("the leftFront of 1: ", ret[i][0])
            print("the rightFront of 2: ", ret[i][1])
            print("the leftDown of 3: ", ret[i][2])
            print("the rightDown of 4: ", ret[i][3])

    m_s.save_station(ret, file_name, m_c.station_id)
    # m_s.save_station_cp(ret, file_name_n, m_c.station_id, m_c.init_yaw, m_c.init_p)

    print("--- generator ", file_name, " done!!!!!!!!! ---")
    print("--- generator ", file_name_n, " done!!!!!!!!! ---")
