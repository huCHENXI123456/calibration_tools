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

def norm_2(p1,p2):
    dist = np.sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]),2) + pow((p1[2]-p2[2]),2))
    return dist


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

if __name__ == '__main__':
    print(">>>>>>>>>>>>> CAR ID: ", m_c.CAR_ID)
    ret = []
    ###########################################
    file_name = "anp_station_tianjin_" + m_c.CAR_ID + '.prototxt'
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
    # # add middle marker
    m8 = m_c.LeftMarker_M0()   # P9
    m9 = m_c.RightMarker_M0()  # P10 
    # add fisheye
    m10 = m_c.FrontFishMarker_F0()  # F1
    m11 = m_c.LeftFishMarker_L0()   # F2
    m12 = m_c.LeftFishMarker_L1()   # F3
    m13 = m_c.RightFishMarker_R0()  # F4
    m14 = m_c.RightFishMarker_R1()  # F5
    # add lidar
    m15 = m_c.FrontLidarMarker_L()  #L0
    m16 = m_c.FrontLidarMarker_R()  #L1
    m17 = m_c.LeftLidarMarker_F0()  #L2
    m18 = m_c.LeftLidarMarker_R0()  #L3
    m19 = m_c.RightLidarMarker_F0() #L4
    m20 = m_c.RightLidarMarker_R0() #L5

    # new station
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
    ret.append(markerpostion(m15)) 
    ret.append(markerpostion(m16)) 
    ret.append(markerpostion(m17))
    ret.append(markerpostion(m18))
    ret.append(markerpostion(m19))
    ret.append(markerpostion(m20))

    if False:
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
    if False:
        plota(ret[10], m10.name)
        plota(ret[11], m11.name)
        plota(ret[12], m12.name)
        plota(ret[13], m13.name)
        plota(ret[14], m14.name)                      
    if True:
        plota(ret[15], m15.name)
        plota(ret[16], m16.name)
        # plota(ret[17], m17.name)
        # plota(ret[18], m18.name)
        # plota(ret[19], m19.name)
        # plota(ret[20], m20.name)   

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
    print("--- generator ", file_name, " done!!!!!!!!! ---")