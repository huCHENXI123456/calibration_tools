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

# CAR_ID = "1801"
# wheelbase = 5

CAR_ID = "2501"
wheelbase = 5.175

MARKER_TYPE = 2   # 0: 8, 1: 10, 2: all

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
            self.position = [[4.8626,2.9771,2.7820],
                             [5.3436,2.4678,2.7808],
                             [4.8622,2.9774,2.4819],
                             [5.3428,2.4680,2.4808]]   #  x>0 y>0 z>0

class FrontMarker_1:
      def __init__(self):
            self.name = "front_marker_1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.4883,0.9810,2.9944],
                             [6.7616,0.3361,2.9851],
                             [6.5044,0.9921,2.6952],
                             [6.7774,0.3476,2.6860]]   #  x>0 y>0 z>0
             

class FrontMarker_2:
      def __init__(self):
            self.name = "front_marker_2"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z                        
            self.position = [[7.1169,-0.4602,3.0274],
                             [6.8903,-1.1228,3.0215],
                             [7.1296,-0.4616,2.7278],
                             [6.9037,-1.1240,2.7219]]   #  x>0 y>0 z>0

class FrontMarker_3:
      def __init__(self):
            self.name = "front_marker_3"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.6865,-2.1768,2.7073],
                             [6.3397,-2.7849,2.6984],
                             [6.6899,-2.1738,2.4075],
                             [6.3421,-2.7820,2.3983]]   #  x>0 y>0 z>0
#################### LEFT ####################
class LeftMarker_F0:
      def __init__(self):
            self.name = "left_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-0.1515,3.5632,2.3891],
                             [0.5334,3.4153,2.3893],
                             [-0.1496,3.5695,2.0886],
                             [0.5351,3.4220,2.0889]]   #  x>0 y>0 z>0
           
class LeftMarker_R0:
      def __init__(self):
            self.name = "left_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.4745,2.8920,2.3722],
                             [-2.9969,3.4042,2.3853],
                             [-3.4745,2.8993,2.0723],
                             [-2.9954,3.4100,2.0851]]   #  x>0 y>0 z>0                         

class RightMarker_F0:
      def __init__(self):
            self.name = "right_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.5578,-3.3267,2.3976],
                             [-0.1101,-3.5385,2.4028],
                             [0.5573,-3.3321,2.0975],
                             [-0.1108,-3.5427,2.1024]]   #  x>0 y>0 z>0                                 

class RightMarker_R0:
      def __init__(self):
            self.name = "right_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.0468,-3.4606,2.3204],
                             [-3.5117,-2.9370,2.3351],
                             [-3.0472,-3.4527,2.0204],
                             [-3.5119,-2.9288,2.0352]]   #  x>0 y>0 z>0
            
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
            self.position = [[2.2371,0.2921,0.0236],
                             [2.2385,-0.4095,0.0171],
                             [1.9369,0.2916,0.0229],
                             [1.9377,-0.4098,0.0170]]   #  x>0 y>0 z>0  
                      
class LeftFishMarker_L0:
      def __init__(self):
            self.name = "fish_marker_l0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[1.4984,1.6548,0.0303],
                             [2.2004,1.6608,0.0302],
                             [1.5023,1.3557,0.0283],
                             [2.2019,1.3695,0.0302]]    #  x>0 y>0 z>0             
            
class LeftFishMarker_L1:
      def __init__(self):
            self.name = "fish_marker_l1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-0.2611,2.0612,0.0202],
                             [0.4406,2.0623,0.0306],
                             [-0.2610,1.7608,0.0209],
                             [0.4405,1.7606,0.0297]]   #  x>0 y>0 z>0  
            
class RightFishMarker_R0:
      def __init__(self):
            self.name = "fish_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.1794,-1.7059,0.0168],
                             [1.4777,-1.7060,0.0098],
                             [2.1756,-1.4002,0.0148],
                             [1.4760,-1.4074,0.0071]]   #  x>0 y>0 z>0 
            
class RightFishMarker_R1:
      def __init__(self):
            self.name = "fish_marker_r1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.4420,-2.0586,0.0089],
                             [-0.2598,-2.0541,0.0001],
                             [0.4437,-1.7576,0.0074],
                             [-0.2579,-1.7533,0.0002]]   #  x>0 y>0 z>0  
                                                     
