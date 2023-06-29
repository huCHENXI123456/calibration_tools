# -*- coding: UTF-8 -*-

import numpy as np
import marker_process as m_p
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
######################################
########## Marker coordinate #########
######################################
# 左上->右上->左下->右下
# 0 -- 1
# |    |
# 2 -- 3

# x朝下(used),标定算法使用，y朝右
M_I = np.array([[0.0, 0.0, 0.0],
                [0.0, 0.8, 0.0],
                [0.7, 0.0, 0.0],
                [0.7, 0.8, 0.0]])

M_C = np.array([[0.2, 0.2, 0.0],
                [0.2, 0.6, 0.0],
                [0.5, 0.2, 0.0],
                [0.5, 0.6, 0.0]])

POINT_N = 4
wheelbase = 5.175
# user setting
init_yaw = 0.0  # math.radians(0)   # radians
init_p = [0.0, 0.0, 0.0] # position[x,y,z]
station_id = 0 # default: 0
#################### FRONT Lidar ####################
class Lidar_FrontMarker_0:
    def __init__(self):
        self.name = "lidar_front_marker_0"
        self.init_angle_h = [0,0,0]
        self.init_angle_v = [0,0,0]
        self.init_position = [wheelbase,0.0,0.0]     # 车体坐标系 全站仪和后轴中心点位置偏差: x,y,z
        self.position = [[4.8602, 2.9775, 2.7821],
                            [5.3424, 2.4697, 2.7804],
                            [4.8588, 2.9772, 2.4818],
                            [5.3418, 2.4699, 2.4803]]   #  x>0 y>0 z>0
            
    def markerpostion(self):
        print("------------------- ", self.name, " -----------------")
        # 测量位置为前轴中心点，标定使用后轴中心点
        ret1 = [self.position[0][0]+self.init_position[0], self.position[0][1], self.position[0][2]]
        ret2 = [self.position[1][0]+self.init_position[0], self.position[1][1], self.position[1][2]]
        ret3 = [self.position[2][0]+self.init_position[0], self.position[2][1], self.position[2][2]]
        ret4 = [self.position[3][0]+self.init_position[0], self.position[3][1], self.position[3][2]]

        pointSet = [ret1,ret2,ret3,ret4]
        print(ret1)
        print(ret2)
        print(ret3)
        print(ret4)
        return pointSet


    # 绘制四个角点
    def plotf(self,a, b):
        #3D Plotting
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.scatter(a[0][0],a[0][1],a[0][2],color='b')
        ax.scatter(a[1][0],a[1][1],a[1][2],color='g')
        ax.scatter(a[2][0],a[2][1],a[2][2],color='r')
        ax.scatter(a[3][0],a[3][1],a[3][2],color='y')
        
        ax.scatter(b[0][0],b[0][1],b[0][2],color='b')
        ax.scatter(b[1][0],b[1][1],b[1][2],color='g')
        ax.scatter(b[2][0],b[2][1],b[2][2],color='r')
        ax.scatter(b[3][0],b[3][1],b[3][2],color='y')        
        #Labeling
        ax.set_xlabel('X Axes')
        ax.set_ylabel('Y Axes')
        ax.set_zlabel('Z Axes')
        plt.show()
                    
m0 = Lidar_FrontMarker_0()   # P1
ret = m0.markerpostion()

print("ret: \n", ret)
B_s = np.array(ret)
T, R, t = m_p.computer_translate(M_I, B_s)

print("R: \n", R)
print("t: \n", t)

B_o = []
for i in range(len(M_C)) :
    B_C = np.dot(R, M_C[i].T)
    B_C = B_C + t
    B_o.append(B_C)
    
print("B_o: \n", B_o)



m0.plotf(ret, B_o)

