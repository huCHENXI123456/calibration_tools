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

# offset: 0.01
M_OFFSET = [0.2-0.01, 0.2-0.01, 0.0]
M_L = np.array([[0.01, 0.01, 0.0],
                [0.01, 0.8-0.01, 0.0],
                [0.7-0.01, 0.01, 0.0],
                [0.7-0.01, 0.8-0.01, 0.0]])
######################################
# 不同全站仪配置输出参数不同
# 徕卡坐标系和车体坐标系不一致，需要手动更改
######################################
# CAR_ID = "1801"
# wheelbase = 5

CAR_ID = "2501"
wheelbase = 5.175

MARKER_TYPE = 2   # 0: 8, 1: 10, 2: all

# user setting
init_yaw = 0.0  # math.radians(0)   # radians, left is negative, -0.1,-0.3,-0.5,-0.8
init_p = [0.0, 0.0, 0.0] # position[x,y,z]
station_id = 0 # default: 0

######################################################
#################### FRONT CAMERA ####################
class FrontMarker_0:
      def __init__(self):
            self.name = "front_marker_0"
            self.init_position = [wheelbase,0.0,0.0]     # 车体坐标系 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[4.8484,3.0836,2.5008],
                             [5.2210,2.4912,2.5024],
                             [4.8615,3.0908,2.2015],
                             [5.2337,2.4986,2.2032]]   #  x>0 y>0 z>0

class FrontMarker_1:
      def __init__(self):
            self.name = "front_marker_1"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.5176,1.0030,2.4958],
                             [6.7340,0.3374,2.4860],
                             [6.5330,1.0126,2.1964],
                             [6.7502,0.3469,2.1866]]   #  x>0 y>0 z>0
             

class FrontMarker_2:
      def __init__(self):
            self.name = "front_marker_2"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z                        
            self.position = [[7.1213,-0.4585,2.3780],
                             [6.9071,-1.1252,2.3722],
                             [7.1333,-0.4595,2.0785],
                             [6.9202,-1.1264,2.0723]]   #  x>0 y>0 z>0

class FrontMarker_3:
      def __init__(self):
            self.name = "front_marker_3"                  
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[6.7191,-2.2737,2.4851],
                             [6.2467,-2.7892,2.4637],
                             [6.7343,-2.2747,2.1860],
                             [6.2619,-2.7905,2.1643]]   #  x>0 y>0 z>0
#################### LEFT ####################
class LeftMarker_F0:
      def __init__(self):
            self.name = "left_marker_f0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-0.1556,3.5507,2.3839],
                             [0.5294,3.4046,2.3842],
                             [-0.1539,3.5583,2.0838],
                             [0.5311,3.4127,2.0845]]   #  x>0 y>0 z>0
           
class LeftMarker_R0:
      def __init__(self):
            self.name = "left_marker_r0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.4766,2.8757,2.3676],
                             [-2.9999,3.3882,2.3805],
                             [-3.4757,2.8824,2.0678],
                             [-2.9990,3.3947,2.0804]]   #  x>0 y>0 z>0           
                         
#################### RIGHT ####################
class RightMarker_F0:
      def __init__(self):
            self.name = "right_marker_f0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.5672,-3.3343,2.3925],
                             [-0.1001,-3.5461,2.3975],
                             [0.5666,-3.3396,2.0926],
                             [-0.1006,-3.5516,2.0976]]   #  x>0 y>0 z>0                               

class RightMarker_R0:
      def __init__(self):
            self.name = "right_marker_r0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-3.0360,-3.4750,2.3157],
                             [-3.5019,-2.9528,2.3305],
                             [-3.0369,-3.4674,2.0158],
                             [-3.5023,-2.9445,2.0306]]   #  x>0 y>0 z>0
            
#################### LEFT/RIGHT MIDDLE ################
class LeftMarker_M0:
      def __init__(self):
            self.name = "left_marker_m0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.198,1.628,0.029],
                             [2.195,1.327,0.030],
                             [1.499,1.630,0.027],
                             [1.497,1.328,0.029]]   #  x>0 y>0 z>0
class RightMarker_M0:
      def __init__(self):
            self.name = "right_marker_m0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-1.3077,-3.4187,2.0372],
                             [-1.9916,-3.2691,2.0423],
                             [-1.3112,-3.4241,1.7369],
                             [-1.9951,-3.2748,1.7422]]   #  x>0 y>0 z>0
            
#################################################
#################### FISHEYE #################### 
class FrontFishMarker_F0:
      def __init__(self):
            self.name = "fish_marker_f0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.2369,0.2943,0.0243],
                             [2.2387,-0.4074,0.0179],
                             [1.9362,0.2937,0.0237],
                             [1.9375,-0.4079,0.0176]]   #  x>0 y>0 z>0  
                      
class LeftFishMarker_L0:
      def __init__(self):
            self.name = "fish_marker_l0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[1.4973,1.6567,0.0310],
                             [2.1999,1.6627,0.0308],
                             [1.5012,1.3574,0.0292],
                             [2.2010,1.3613,0.0310]]    #  x>0 y>0 z>0             
            
class LeftFishMarker_L1:
      def __init__(self):
            self.name = "fish_marker_l1"                  
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[-0.2622,2.0630,0.0211],
                             [0.4392,2.0635,0.0320],
                             [-0.2624,1.7627,0.0219],
                             [0.4392,1.7625,0.0303]]   #  x>0 y>0 z>0  
            
class RightFishMarker_R0:
      def __init__(self):
            self.name = "fish_marker_r0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[2.1801,-1.6991,0.0174],
                             [1.4783,-1.7045,0.0102],
                             [2.1757,-1.3978,0.0160],
                             [1.4765,-1.4057,0.0078]]   #  x>0 y>0 z>0 
            
class RightFishMarker_R1:
      def __init__(self):
            self.name = "fish_marker_r1"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[0.4432,-2.0574,0.0099],
                             [-0.2587,-2.0535,0.0004],
                             [0.4449,-1.7567,0.0081],
                             [-0.2568,-1.7522,0.0011]]   #  x>0 y>0 z>0  
                                                     

#####################################################
#################### FRONT LIDAR #################### 
class FrontLidarMarker_L:
      def __init__(self):
            self.name = "lidar_marker_f0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[3.7317,1.7801,2.0159],
                             [4.0246,1.0575,2.0079],
                             [3.7475,1.7971,1.3367],
                             [4.0401,1.0763,1.3295]]   #  x>0 y>0 z>0  

class FrontLidarMarker_R:
      def __init__(self):
            self.name = "lidar_marker_f1"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[4.0733,-1.1264,1.9889],
                             [3.8190,-1.8637,2.9960],
                             [4.0777,-1.1346,1.3087],
                             [3.8218,-1.8708,1.3164]]   #  x>0 y>0 z>0 
            
#################### LEFT LIDAR #################### 
class LeftLidarMarker_F0:
      def __init__(self):
            self.name = "lidar_marker_l0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[3.7317,1.7801,2.0159],
                             [4.0246,1.0575,2.0079],
                             [3.7475,1.7971,1.3367],
                             [4.0401,1.0763,1.3295]]   #  x>0 y>0 z>0  

class LeftLidarMarker_R0:
      def __init__(self):
            self.name = "lidar_marker_l1"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[4.0733,-1.1264,1.9889],
                             [3.8190,-1.8637,2.9960],
                             [4.0777,-1.1346,1.3087],
                             [3.8218,-1.8708,1.3164]]   #  x>0 y>0 z>0  
#################### RIGHT LIDAR ####################             
class RightLidarMarker_F0:
      def __init__(self):
            self.name = "lidar_marker_r0"                        
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[3.7317,1.7801,2.0159],
                             [4.0246,1.0575,2.0079],
                             [3.7475,1.7971,1.3367],
                             [4.0401,1.0763,1.3295]]   #  x>0 y>0 z>0  

class RightLidarMarker_R0:
      def __init__(self):
            self.name = "lidar_marker_r1"                   
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.position = [[4.0733,-1.1264,1.9889],
                             [3.8190,-1.8637,2.9960],
                             [4.0777,-1.1346,1.3087],
                             [3.8218,-1.8708,1.3164]]   #  x>0 y>0 z>0              
