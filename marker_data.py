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
CAR_ID = "N_001"
MARKER_TYPE = 1   # 徕卡: init_position 和 position
wheelbase = 5.175
# user setting
init_yaw = 0   # math.radians(0)   # degrees, left is negative, -0.1,-0.3,-0.5,-0.8
init_p = [0, 0, 0.0] # position[x,y,z]
station_id = 0 # default: 0
###########################################
class FrontMarker_0:
      def __init__(self):
            self.name = "front_marker_0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 车体坐标系 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [6.9593,7.0483,6.9539,7.0430]
            self.HAR = [[21,37,10],
                        [15,56,17],
                        [21,36,56],
                        [15,55,48]]
            self.V = [2.1326,2.1328,1.8327,1.8329]
            self.S = [6.9880,7.0767,6.9619,7.0509]
            self.ZA  = [[275,11,38],
                        [275,7,49],
                        [272,44,20],
                        [272,42,22]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0


class FrontMarker_1:
      def __init__(self):
            self.name = "front_marker_1"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [8.1857,8.2019,8.1885,8.2050]
            self.HAR = [[9,41,39],
                        [4,48,3],
                        [9,38,52],
                        [4,45,15]]
            self.V = [2.4361,2.4518,2.1364,2.1521]
            self.S = [8.2390,8.2569,8.2132,8.2309]
            self.ZA  = [[276,31,24],
                        [276,37,10],
                        [274,26,37],
                        [274,32,37]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0
             

class FrontMarker_2:
      def __init__(self):
            self.name = "front_marker_2"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.6611,3.6039,3.6610,3.6034]
            self.HAR = [[73,21,23],
                        [62,20,5],
                        [73,24,28],
                        [62,   23,6]]
            self.V = [1.7028,1.6954,1.4029,1.3954]
            self.S = [3.6667,3.6092,3.6623,3.6049]
            self.ZA  = [[273,10,16],
                        [273,6,14],
                        [268,28,48],
                        [268,20,11]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0


class FrontMarker_3:
      def __init__(self):
            self.name = "front_marker_3"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [4.0064,3.8720,4.0116,3.8761]
            self.HAR = [[300,1,40],
                        [290,1,23],
                        [300,1,47],
                        [290,2,16]]
            self.V = [1.6810,1.6780,1.3811,1.3780]
            self.S = [4.0105,3.8761,4.0134,3.8780]
            self.ZA  = [[272,35,13],
                        [272,37,55],
                        [268,18,5],
                        [268,11,48]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0

class LeftMarker_F0:
      def __init__(self):
            self.name = "left_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.6567,3.8376,3.6596,3.8428]
            self.HAR = [[127,55,8],
                        [117,34,8],
                        [127,46,13],
                        [117,26,11]]
            self.V = [1.6491,1.6728,1.3492,1.3730]
            self.S = [3.6597,3.8415,3.6627,3.8449]
            self.ZA  = [[272,20,3],
                        [272,34,42],
                        [267,38,26],
                        [268,6,24]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0

class LeftMarker_M0:
      def __init__(self):
            self.name = "left_marker_m0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.6567,3.8376,3.6596,3.8428]
            self.HAR = [[127,55,8],
                        [117,34,8],
                        [127,46,13],
                        [117,26,11]]
            self.V = [1.6491,1.6728,1.3492,1.3730]
            self.S = [3.6597,3.8415,3.6627,3.8449]
            self.ZA  = [[272,20,3],
                        [272,34,42],
                        [267,38,26],
                        [268,6,24]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0
                             
class LeftMarker_R0:
      def __init__(self):
            self.name = "left_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.7132,3.6356,3.7048,3.6258]
            self.HAR = [[239,46,45],
                        [228,54,51],
                        [239,50,9],
                        [228,56,43]]
            self.V = [1.6648,1.6609,1.3650,1.3611]
            self.S = [3.7169,3.6392,3.7073,3.6285]
            self.ZA  = [[272,32,26],
                        [272,32,4],
                        [267,54,45],
                        [267,48,21]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0

class RightMarker_F0:
      def __init__(self):
            self.name = "right_marker_f0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.6567,3.8376,3.6596,3.8428]
            self.HAR = [[127,55,8],
                        [117,34,8],
                        [127,46,13],
                        [117,26,11]]
            self.V = [1.6491,1.6728,1.3492,1.3730]
            self.S = [3.6597,3.8415,3.6627,3.8449]
            self.ZA  = [[272,20,3],
                        [272,34,42],
                        [267,38,26],
                        [268,6,24]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0

class RightMarker_M0:
      def __init__(self):
            self.name = "right_marker_m0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.6567,3.8376,3.6596,3.8428]
            self.HAR = [[127,55,8],
                        [117,34,8],
                        [127,46,13],
                        [117,26,11]]
            self.V = [1.6491,1.6728,1.3492,1.3730]
            self.S = [3.6597,3.8415,3.6627,3.8449]
            self.ZA  = [[272,20,3],
                        [272,34,42],
                        [267,38,26],
                        [268,6,24]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0

class RightMarker_R0:
      def __init__(self):
            self.name = "right_marker_r0"
            self.init_angle_h = [0,0,0]
            self.init_angle_v = [0,0,0]
            self.init_position = [wheelbase,0.0,0.0]     # 全站仪和后轴中心点位置偏差: x,y,z
            self.H = [3.7132,3.6356,3.7048,3.6258]
            self.HAR = [[239,46,45],
                        [228,54,51],
                        [239,50,9],
                        [228,56,43]]
            self.V = [1.6648,1.6609,1.3650,1.3611]
            self.S = [3.7169,3.6392,3.7073,3.6285]
            self.ZA  = [[272,32,26],
                        [272,32,4],
                        [267,54,45],
                        [267,48,21]]
            self.position = [[],
                             [],
                             [],
                             []]   #  x>0 y>0 z>0