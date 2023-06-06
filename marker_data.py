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
            self.position = [[4.857, 2.981, 2.783],
                             [5.340, 2.475, 2.782],
                             [4.854, 2.980, 2.482],
                             [5.338, 2.475, 2.481]]   #  x>0 y>0 z>0

class FrontMarker_1:
      def __init__(self):
            self.name = "front_marker_1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.490,0.992,2.994],
                             [6.765,0.348,2.985],
                             [6.506,1.003,2.695],
                             [6.781,0.359,2.686]]   #  x>0 y>0 z>0
             

class FrontMarker_2:
      def __init__(self):
            self.name = "front_marker_2"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z                        
            self.position = [[7.123,-0.447,3.027],
                             [6.899,-1.111,3.021],
                             [7.136,-0.449,2.728],
                             [6.913,-1.113,2.721]]   #  x>0 y>0 z>0

class FrontMarker_3:
      def __init__(self):
            self.name = "front_marker_3"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.653,-2.151,2.683],
                             [6.402,-2.804,2.675],
                             [6.658,-2.149,2.383],
                             [6.408,-2.804,2.375]]   #  x>0 y>0 z>0
#################### LEFT ####################
class LeftMarker_F0:
      def __init__(self):
            self.name = "left_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            # new n_005       
            self.position = [[-0.120,3.679,1.805],
                             [0.467,3.299,1.812],
                             [-0.115,3.681,1.505],
                             [0.472,3.301,1.512]]   #  x>0 y>0 z>0
           
class LeftMarker_R0:
      def __init__(self):
            self.name = "left_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.458,2.858,2.159],
                             [-3.019,3.402,2.171],
                             [-3.454,2.861,1.859],
                             [-3.013,3.404,1.871]]   #  x>0 y>0 z>0

class RightMarker_F0:
      def __init__(self):
            self.name = "right_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.573,-3.332,2.399],
                             [-0.093,-3.545,2.405],
                             [0.572,-3.338,2.099],
                             [-0.095,-3.550,2.105]]   #  x>0 y>0 z>0

class RightMarker_R0:
      def __init__(self):
            self.name = "right_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.030,-3.480,2.324],
                             [-3.496,-2.957,2.339],
                             [-3.030,-3.471,2.024],
                             [-3.496,-2.949,2.039]]   #  x>0 y>0 z>0
            
#################### MIDDLE #################### 
class LeftMarker_M0:
      def __init__(self):
            self.name = "left_marker_m0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-1.9858,3.1227,1.9818],
                             [-1.3453,3.4055,1.9858],
                             [-1.9881,3.1322,1.6819],
                             [-1.3479,3.4158,1.6859]]   #  x>0 y>0 z>0
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
            self.position = [[2.234,0.297,0.028],
                             [2.236,-0.404,0.022],
                             [1.952,0.299,0.015],
                             [1.949,-0.407,0.012]]   #  x>0 y>0 z>0  
                      
class LeftFishMarker_L0:
      def __init__(self):
            self.name = "fish_marker_l0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.197,1.662,0.035],
                             [2.199,1.362,0.034],
                             [1.498,1.659,0.032],
                             [1.499,1.356,0.034]]   #  x>0 y>0 z>0            
            
class LeftFishMarker_L1:
      def __init__(self):
            self.name = "fish_marker_l1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.438,2.061,0.037],
                             [0.444,1.778,0.020],
                             [-0.212,2.061,0.026],
                             [-0.264,1.779,0.011]]   #  x>0 y>0 z>0  
            
class RightFishMarker_R0:
      def __init__(self):
            self.name = "fish_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.175,-1.396,0.019],
                             [2.179,-1.697,0.020],
                             [1.475,-1.402,0.013],
                             [1.480,-1.704,0.013]]   #  x>0 y>0 z>0  
            
class RightFishMarker_R1:
      def __init__(self):
            self.name = "fish_marker_r1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.7132,3.6356,3.7048,3.6258]
            self.position = [[0.450,-1.772,-0.003],
                             [0.443,-2.054,0.014],
                             [-0.258,-1.768,-0.010],
                             [-0.260,-2.068,-0.008]]   #  x>0 y>0 z>0  
                                                     
