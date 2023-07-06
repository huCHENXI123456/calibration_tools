import sys
import math
import numpy as np
from scipy.spatial.transform import Rotation as R
import scipy.linalg as linalg
import marker_process as m_p

# car axis x: car rear, y: car right 
# point position
wheel_len = 5
# # 1801
# left_struct = [-3.972+wheel_len,0.515,0]    # 对应p3
# right_struct = [-3.972+wheel_len,-0.515, 0]  # 对应p4
# 2501
left_struct = [-4.036+wheel_len,0.52,0]    # 对应p3
right_struct = [-4.036+wheel_len,-0.52, 0]  # 对应p4


# 参数分别是旋转轴和旋转弧度值
def rotate_mat(axis, radian):
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    return rot_matrix

# rotation z(yaw)
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

def computer_1(pl, pr):
    x_f = pr[0] - pl[0]
    y_f = pr[1] - pl[1]
    # atan(delta_y / delta_x)
    yaw = math.atan(x_f/y_f)
    print(">>> The result yaw (left+,right-)degree: ", math.degrees(yaw), ",rad: ", yaw)
    R_c = convert_rotation(yaw, 0, 0)
    R_c_v = convert_rotation(-yaw, 0, 0) # np.linalg.inv(R_c)
    P1_t = np.dot(R_c, pl)
    P2_t = np.dot(R_c, pr)

    p1_sub = np.array([left_struct[0]-P1_t[0], left_struct[1]-P1_t[1], 0.0])
    p2_sub = np.array([right_struct[0]-P2_t[0], right_struct[1]-P2_t[1], 0.0])

    p_avg = (p1_sub + p2_sub)/2

    pl_p = P1_t + p_avg
    pr_p = P2_t + p_avg

    # 
    t_s_m = -np.dot(R_c_v, p_avg)
    pstruct_l_rot = np.dot(R_c_v, left_struct)
    pstruct_r_rot = np.dot(R_c_v, right_struct)
    pstruct_l = pstruct_l_rot + t_s_m
    pstruct_r = pstruct_r_rot + t_s_m

    #
    R_z_set = m_p.convert_rotation(-yaw, 0, 0)
    y1_c, p1_c, r1_c = m_p.convert_eular(R_z_set)
                
    print("-"*60)
    print("-"*60)
    print("left point structure: ", left_struct)
    print("right point structure: ", right_struct)
    print("-"*60)
    print("left point messure: ", pl)
    print("right point messure: ", pr)
    print("-"*60)
    print("left point rotation reproject: ", P1_t)
    print("right point rotation reproject: ", P2_t)    
    print("left point reproject: ", pl_p)
    print("right point reproject: ", pr_p)  
    print("-"*60)
    print(">>> messure to structure x ", p_avg[0], ",y ", p_avg[1], ",yaw ", yaw)
    print("-"*60)
    print("-"*60)
    print("left structure rotation reproject: ", pstruct_l_rot)
    print("right structure rotation reproject: ", pstruct_r_rot)      
    print("left structure reproject: ", pstruct_l)
    print("right structure reproject: ", pstruct_r)  
    print("-"*60)
    print("This is used for cpp calibration...")
    print(">>> The result structure to messure yaw: ", -yaw, ",translate: ", t_s_m)
    # print(">>> The result of rotation: \n", R_z_set)
    # print(">>> The verify yaw: ", y1_c, ",pitch: ", p1_c, ",roll: ", r1_c)
    print("-"*60)
    print("This is used for update stations calibration...")
    print(">>> If yaw is positive, mean stations yaw is growing")    
    print(">>> The result messure to structure x ", p_avg[0], ",y ", p_avg[1], ",yaw ", yaw)
    print("-"*60)

    return t_s_m[0], t_s_m[1], -yaw
    
if __name__ == '__main__':   
    #1801-5   
    # p3 = [-3.9852+wheel_len,0.4816,0]
    # p4 = [-4.0142+wheel_len,-0.5323,0]  
    # #b_002
    # p3 = [-4.0178+wheel_len,0.4168,0]
    # p4 = [-4.0129+wheel_len,-0.6071,0] 

    #b_004-0630
    # p3 = [-4.0199+wheel_len,0.5578,0]
    # p4 = [-4.0465+wheel_len,-0.4660,0] 

    #1801-3  -0630
    p3 = [-4.0203+wheel_len,0.6014,0]
    p4 = [-4.0324+wheel_len,-0.4157,0] 
    # computer(p1, p2, p3, p4)
    x,y,yaw = computer_1(p3, p4)
    if True:
        R_t = convert_rotation(yaw, 0, 0)
        pt_l = np.dot(R_t, left_struct) + np.array([x,y,0])
        pt_r = np.dot(R_t, right_struct) + np.array([x,y,0])
        print("test data 1: ", pt_l)
        print("test data 2: ", pt_r)
