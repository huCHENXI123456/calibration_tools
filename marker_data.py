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

CAR_ID = "B_004"
MARKER_TYPE = 2   # 0: 8, 1: 10, 2: all
wheelbase = 5
# user setting
init_yaw = 0.0  # math.radians(0)   # radians, left is negative, -0.1,-0.3,-0.5,-0.8
init_p = [0.0, 0.0, 0.0] # position[x,y,z]
station_id = 4 # default: 0
###########################################
#################### FRONT ####################
class FrontMarker_0:
      def __init__(self):
            self.name = "front_marker_0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 车体坐标系 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[4.8602, 2.9775, 2.7821],
                             [5.3424, 2.4697, 2.7804],
                             [4.8588, 2.9772, 2.4818],
                             [5.3418, 2.4699, 2.4803]]   #  x>0 y>0 z>0

class FrontMarker_1:
      def __init__(self):
            self.name = "front_marker_1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.4907,0.9853,2.9942],
                             [6.7647,0.3407,2.9849],
                             [6.5064,0.9961,2.6945],
                             [6.7799,0.3519,2.6854]]   #  x>0 y>0 z>0
             

class FrontMarker_2:
      def __init__(self):
            self.name = "front_marker_2"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z                        
            self.position = [[7.1221,-0.4549,3.0273],
                             [6.8963,-1.1179,3.0211],
                             [7.1332,-0.4561,2.7273],
                             [6.9092,-1.1193,2.7213]]   #  x>0 y<0 z>0

class FrontMarker_3:
      def __init__(self):
            self.name = "front_marker_3"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.6515,-2.1588,2.6835],
                             [6.4009,-2.8129,2.6752],
                             [6.6569,-2.1571,2.3834],
                             [6.4063,-2.8112,2.3751]]   #  x>0 y<0 z>0
#################### LEFT ####################
class LeftMarker_F0:
      def __init__(self):
            self.name = "left_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            # new n_005       
            self.position = [[-0.1561,3.5513,2.3884],
                             [0.5292,3.4053,2.3889],
                             [-0.1544,3.5592,2.0882],
                             [0.5310,3.4126,2.0885]]   #  x>0 y>0 z>0
           
class LeftMarker_R0:
      def __init__(self):
            self.name = "left_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.4941,2.8889,2.2084],
                             [-2.9848,3.3691,2.2151],
                             [-3.4952,2.8839,1.9084],
                             [-2.9849,3.3733,1.9148]]   #  x>0 y>0 z>0

class RightMarker_F0:
      def __init__(self):
            self.name = "right_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.5696,-3.3365,2.3963],
                             [-0.0976,-3.5501,2.4031],
                             [0.5684,-3.3421,2.0963],
                             [-0.0990,-3.5554,2.1029]]   #  x>0 y>0 z>0

class RightMarker_R0:
      def __init__(self):
            self.name = "right_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.0349,-3.4791,2.3198],
                             [-3.5003,-2.9563,2.3344],
                             [-3.0354,-3.4712,2.0199],
                             [-3.5004,-2.9480,2.0345]]   #  x>0 y>0 z>0
            
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
                                                     
