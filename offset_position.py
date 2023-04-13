import sys
import math
import numpy as np
from scipy.spatial.transform import Rotation as R
import scipy.linalg as linalg

# car axis x: car rear, y: car right 
# point position
#     p1
#  p2 p4 p3
base_offset = 4.656 # 激光探头到前轴中心点距离
messure_long = 7.830762 # 结构上对应p1和p2的距离
messure_left_rear = [6.575878, -0.424, 0]    # 对应p3
messure_right_rear = [6.575878, 0.424, 0]  # 对应p4
p1 = [3.364, 0.1]
p2 = [11.198, -0.49]
p3 = [11.216, 0.348]
p4 = [11.206, -0.075]

# 参数分别是旋转轴和旋转弧度值
def rotate_mat(axis, radian):
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    return rot_matrix

def convert_rotation(yaw, pitch, roll):
    # EulerOrder::XYZ
    axis_x, axis_y, axis_z = [1,0,0], [0,1,0], [0, 0, 1]
    rotation_yaw = rotate_mat(axis_z, yaw)
    rotation_pitch = rotate_mat(axis_y, pitch)
    rotation_roll = rotate_mat(axis_x, roll)

    # rotation_yaw * rotation_pitch * rotation_roll
    P1 = np.dot(rotation_yaw, rotation_pitch)
    P2 = np.dot(P1, rotation_roll)

    return P2

def computer(p_1, p_2, p_3, p_4):
    x_f = p_4[0] - p_1[0]
    y_f = p_4[1] - p_1[1]
    # atan(delta_y / delta_x)
    yaw = math.atan(y_f/x_f)
    print(">>> result front yaw: ", math.degrees(yaw), ",rad: ", yaw)

    x_h = -(p_2[0] - p_3[0])
    y_h = p_2[1] - p_3[1]
    yaw_p = math.atan(x_h/y_h)
    print(">>> result left yaw: ", math.degrees(yaw_p), " ", yaw_p)

    R_c = convert_rotation(yaw_p, 0, 0)
    P1_t = np.dot(R_c, messure_left_rear)
    P2_t = np.dot(R_c, messure_right_rear)

    p1_m = np.array([p_2[0]-base_offset, p_2[1]])
    p2_m = np.array([p_3[0]-base_offset, p_3[1]])

    p1_sub = np.array([p1_m[0] - P1_t[0], p1_m[1] - P1_t[1], 0.0])
    p2_sub = np.array([p2_m[0] - P2_t[0], p2_m[1] - P2_t[1], 0.0])

    p_avg = (p1_sub + p2_sub)/2

    print("-"*60)
    print("left point rot: ", P1_t[0:2])
    print("right point rot: ", P2_t[0:2])

    print("left point mess: ", p1_m)
    print("right point mess: ", p2_m)

    print("left point sub: ", p1_sub)
    print("right point sub: ", p2_sub)

    print("-"*60)
    print("Final yaw: ", yaw_p)
    print("Final offset: ", p_avg)

if __name__ == '__main__':   
    computer(p1, p2, p3, p4)