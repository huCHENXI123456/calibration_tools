# -*- coding: UTF-8 -*-

import numpy as np

######################################
########## Marker coordinate #########
######################################
# 左上->右上->左下->右下
# x水平, y向下
M = np.array([[0, 0, 0.0],    
            [0.7, 0.0, 0.0],
            [0.0, 0.3, 0.0],
            [0.7, 0.3, 0.0]])
# x朝下(used),标定算法使用，y朝右
M_I = np.array([[0, 0, 0.0],
            [0.0, 0.7, 0.0],
            [0.3, 0.0, 0.0],
            [0.3, 0.7, 0.0]])

POINT_N = 4

######################################
# 不同全站仪配置输出参数不同
# 徕卡坐标系和车体坐标系不一致，需要手动更改
######################################

# 0519,此站用于c+01,n06-3,n09,n10,n13,n16,n08,n17

CAR_ID = "tianjin"
MARKER_TYPE = 2   # 0: 8, 1: 10, 2: all
wheelbase = 5.175
# user setting
init_yaw = 0.0  # math.radians(0)   # radians, left is negative, -0.1,-0.3,-0.5,-0.8
init_p = [0.0, 0.0, 0.0] # position[x,y,z]
station_id = 0 # default: 0
###########################################
#################### FRONT ####################
class FrontMarker_0:
      def __init__(self):
            self.name = "front_marker_0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 车体坐标系 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[4.864, 2.930, 2.778],
                             [5.344, 2.422, 2.777],
                             [4.862, 2.930, 2.478],
                             [5.342, 2.421, 2.477]]   #  x>0 y>0 z>0

class FrontMarker_1:
      def __init__(self):
            self.name = "front_marker_1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.483,0.929,2.990],
                             [6.753,0.284,2.981],
                             [6.499,0.940,2.691],
                             [6.769,0.294,2.682]]   #  x>0 y>0 z>0
             

class FrontMarker_2:
      def __init__(self):
            self.name = "front_marker_2"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z                        
            self.position = [[7.107,-0.515,3.024],
                             [6.877,-1.176,3.017],
                             [7.118,-0.516,2.723],
                             [6.890,-1.177,2.717]]   #  x>0 y>0 z>0

class FrontMarker_3:
      def __init__(self):
            self.name = "front_marker_3"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.624,-2.215,2.680],
                             [6.371,-2.867,2.672],
                             [6.631,-2.214,2.380],
                             [6.376,-2.865,2.371]]   #  x>0 y>0 z>0
#################### LEFT ####################
class LeftMarker_F0:
      def __init__(self):
            self.name = "left_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            # new n_005       
            self.position = [[-0.146,3.536,2.387],
                             [0.536,3.383,2.387],
                             [-0.144,3.544,2.084],
                             [0.538,3.391,2.084]]   #  x>0 y>0 z>0
           
class LeftMarker_R0:
      def __init__(self):
            self.name = "left_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.496,2.888,2.217],
                             [-2.984,3.366,2.224],
                             [-3.497,2.893,1.917],
                             [-2.985,3.371,1.924]]   #  x>0 y>0 z>0

class RightMarker_F0:
      def __init__(self):
            self.name = "right_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.536,-3.352,2.395],
                             [-0.131,-3.561,2.402],
                             [0.533,-3.357,2.095],
                             [-0.133,-3.566,2.102]]   #  x>0 y>0 z>0

class RightMarker_R0:
      def __init__(self):
            self.name = "right_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.068,-3.475,2.319],
                             [-3.530,-2.947,2.333],
                             [-3.072,-3.463,2.019],
                             [-3.533,-2.936,2.033]]   #  x>0 y>0 z>0
            
#################### MIDDLE #################### 
class LeftMarker_M0:
      def __init__(self):
            self.name = "left_marker_m0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.198,1.628,0.029],
                             [2.195,1.327,0.030],
                             [1.499,1.630,0.027],
                             [1.497,1.328,0.029]]   #  x>0 y>0 z>0
class RightMarker_M0:
      def __init__(self):
            self.name = "right_marker_m0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-1.3077,-3.4187,2.0372],
                             [-1.9916,-3.2691,2.0423],
                             [-1.3112,-3.4241,1.7369],
                             [-1.9951,-3.2748,1.7422]]   #  x>0 y>0 z>0

#################### FISHEYE #################### 
class FrontFishMarker_F0:
      def __init__(self):
            self.name = "fish_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.224,0.262,0.024],
                             [2.220,-0.438,0.018],
                             [1.939,0.265,0.012],
                             [1.936,-0.441,0.004]]   #  x>0 y>0 z>0  
                      
class LeftFishMarker_L0:
      def __init__(self):
            self.name = "fish_marker_l0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.198,1.628,0.029],
                             [2.195,1.327,0.030],
                             [1.499,1.630,0.027],
                             [1.497,1.328,0.029]]    #  x>0 y>0 z>0            
            
class LeftFishMarker_L1:
      def __init__(self):
            self.name = "fish_marker_l1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.442,2.041,0.031],
                             [0.445,1.756,0.015],
                             [-0.259,2.046,0.020],
                             [-0.262,1.760,0.007]]   #  x>0 y>0 z>0  
            
class RightFishMarker_R0:
      def __init__(self):
            self.name = "fish_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.150,-1.430,0.015],
                             [2.154,-1.731,0.016],
                             [1.451,-1.431,0.009],
                             [1.455,-1.734,0.007]]   #  x>0 y>0 z>0  
            
class RightFishMarker_R1:
      def __init__(self):
            self.name = "fish_marker_r1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.7132,3.6356,3.7048,3.6258]
            self.position = [[0.422,-1.791,-0.007],
                             [0.413,-2.074,0.010],
                             [-0.285,-1.784,-0.016],
                             [-0.288,-2.075,-0.007]]   #  x>0 y>0 z>0  
                                                     
