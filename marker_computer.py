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

# 绘制四个角点
def plota(p):
    #3D Plotting
    fig = plt.figure()
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
    ret1 = [m0.position[0][0]+m0.init_position[0], m0.position[0][1], m0.position[0][2]]
    ret2 = [m0.position[1][0]+m0.init_position[0], m0.position[1][1], m0.position[1][2]]
    ret3 = [m0.position[2][0]+m0.init_position[0], m0.position[2][1], m0.position[2][2]]
    ret4 = [m0.position[3][0]+m0.init_position[0], m0.position[3][1], m0.position[3][2]]

    pointSet = [ret1,ret2,ret3,ret4]
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    return pointSet

if __name__ == '__main__':
    print(">>>>>>>>>>>>> CAR ID: ", m_c.CAR_ID)
    ret = []
    # Marker of station, adjust the number of marker class
    # step 1: define class
    m0 = m_c.FrontMarker_0()
    m1 = m_c.FrontMarker_1()    
    m2 = m_c.FrontMarker_2()
    m3 = m_c.FrontMarker_3()
    m4 = m_c.LeftMarker_F0()    
    m5 = m_c.LeftMarker_R0() 
    m6 = m_c.RightMarker_F0()    
    m7 = m_c.RightMarker_R0() 

    # old station
    if m_c.MARKER_TYPE == 0:
        ret.append(markerdata(m0))
        ret.append(markerdata(m1))
        ret.append(markerdata(m2))
        ret.append(markerdata(m3))
        ret.append(markerdata(m4))
        ret.append(markerdata(m5))
        ret.append(markerdata(m6))
        ret.append(markerdata(m7))    
        if True:
            plota(ret[0])
            plota(ret[1])
            plota(ret[2])
            plota(ret[3])
            plota(ret[4])
            plota(ret[5])
            plota(ret[6])
            plota(ret[7])

    elif m_c.MARKER_TYPE == 1:  # laika station
        ret.append(markerpostion(m0))    
        ret.append(markerpostion(m1))
        ret.append(markerpostion(m2))
        ret.append(markerpostion(m3))
        ret.append(markerpostion(m4))
        ret.append(markerpostion(m5))
        ret.append(markerpostion(m6))
        ret.append(markerpostion(m7))        
        if True:
            plota(ret[0])
            plota(ret[1])
            plota(ret[2])
            plota(ret[3])
            plota(ret[4])
            plota(ret[5])
            plota(ret[6])
            plota(ret[7])          
    else:
        print("noting to do!")
    print("#"*60)
    if False:
        print("The lenght of marker nums: ", len(ret))
        for i in range(len(ret)):
            print(">>>>>> The car of marker position: ")
            print("the leftFront of 1: ", ret[i][0])
            print("the rightFront of 2: ", ret[i][1])
            print("the leftDown of 3: ", ret[i][2])
            print("the rightDown of 4: ", ret[i][3])

    with open('anp_station.prototxt','w+') as f:
        f.write("name: " +"\"Deepway\"" + "\n")
        f.write("id: 1"+ "\n")
        f.write("frame_id: " + "\"world\"" + "\n")
        f.write("rear_load: true"+ "\n")
        
        for i in range(len(ret)) :
            print("="*30, "ret[", i, "]", "="*30)
            B_s = np.array(ret[i])
            T,R,t = m_p.computer_translate(m_c.M_I, B_s)
            y1, p1, r1 = m_p.convert_eular(R)
            euler_out = m_p.rot_to_eular(R)
            
            # eular
            if False: 
                print("yaw: ", y1, "pitch: ", p1, "roll: ", r1)
                print("euler(x->y->z): ", euler_out)
                print("x: ", t[0], "y: ", t[1], "z: ", t[2])
            
            # verify
            if False:
                R1 = m_p.convert_rotation(y1, p1, r1)
                print("[main] verify R convert: ", R1)

            f.write("markers { \n")
            f.write("\tid: " + str(i) + "\n")
            if i == 0:
                f.write("\tname: " + "\"" + str(m0.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m0.name) + "\"" + "\n")
            if i == 1:
                f.write("\tname: " + "\"" + str(m1.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m1.name) + "\"" + "\n")
            if i == 2:
                f.write("\tname: " + "\"" +  str(m2.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m2.name) + "\"" + "\n")
            if i == 3:
                f.write("\tname: " + "\"" + str(m3.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m3.name) + "\"" + "\n")
            if i == 4:
                f.write("\tname: " + "\"" + str(m4.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m4.name) + "\"" + "\n")
            if i == 5:
                f.write("\tname: " + "\"" + str(m5.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m5.name) + "\"" + "\n")
            if i == 6:
                f.write("\tname: " + "\"" + str(m6.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m6.name) + "\"" + "\n")
            if i == 7:
                f.write("\tname: " + "\"" + str(m7.name) + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + str(m7.name) + "\"" + "\n")  

            f.writelines("\ttype: CHESS_BOARD" + "\n")
            f.writelines("\tpose {" + "\n")
            f.writelines("\t\tframe_id: "+"\"world\""+ "\n")
            f.writelines("\t\tposition {" + "\n")
            f.write("\t\t\tx: " + str(t[0]) + "\n")
            f.write("\t\t\ty: " + str(t[1]) + "\n")
            f.write("\t\t\tz: " + str(t[2]) + "\n")
            f.writelines("\t\t} \n")
            f.writelines("\t\teuler_angles { \n\t\t\teuler_order: XYZ" + "\n")
            f.write("\t\t\tyaw: "+ str(y1) + "\n")
            f.write("\t\t\tpitch: " + str(p1) + "\n")
            f.write("\t\t\troll: " + str(r1) + "\n")
            f.writelines("\t\t} \n")
            f.writelines("\t} \n")
            f.writelines("\t# observers: FRONT_WIDE_CAMERA " + "\n")
            f.writelines("\t# observers: FRONT_MIDDLE_CAMERA " + "\n")
            f.writelines("\t# observers: FRONT_LONG_CAMERA " + "\n")
            f.writelines("\t# observers: RIGHT_FRONT_CAMERA " + "\n")
            f.writelines("\t# observers: RIGHT_REAR_CAMERA " + "\n")
            f.writelines("\t# observers: LEFT_FRONT_CAMERA " + "\n")
            f.writelines("\t# observers: LEFT_REAR_CAMERA " + "\n")
            f.writelines("\tused: true"+"\n")
            f.writelines("\tdata:" + "\"rows: 5\\ncols: 9\\nsquare_size: 0.10\\ninner_only: true\\n\"" +"\n")
            f.writelines("\troi { \n\t\tauto_roi: true \n\t\tscale: 2.5" + "\n")
            f.writelines("\t} \n")
            f.writelines("\tsolve_pose: true" + "\n")
            f.writelines("\tscale: 2.5" + "\n")
            f.writelines("\tuse_opencv: true" + "\n")
            f.writelines("} \n")
    f.close()

    print("generator done!!!!!!!!!")
