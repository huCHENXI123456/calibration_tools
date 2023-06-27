import numpy as np
import time
import icp
from scipy.spatial.transform import Rotation as R
import math
import scipy.linalg as linalg

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

  
# 参数分别是旋转轴和旋转弧度值
def rotate_mat(axis, radian):
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    return rot_matrix


if __name__ == "__main__":


    egoPos = np.array([3360,2979.6,1837.7,-0.00531602,1.94998,-0.00304643,-0.00110345])
    objPos = np.array([3360,2983.87,1827.12,-0.00498733,1.95492,-0.00833314,-0.000311598])
    relativePos = np.array([3360,-11.4013,-0.0569906,0.0349992,0.0049329,-0.00528907,0.000827186])

    # 
    y1 = egoPos[4]
    p1 = egoPos[5]
    r1 = egoPos[6]
    # convert
    R1 = convert_rotation(y1, p1, r1)
    print("-" * 40)
    print("R convert: ", R1)

    R1_inv = np.linalg.inv(R1)
    t1 = np.array([egoPos[1], egoPos[2], egoPos[3]])
    t1_inv = -np.dot(R1_inv, t1)
    P0 = np.array([objPos[1], objPos[2], objPos[3]])

    P0_ = np.dot(R1_inv, P0) + t1_inv

    print("-"*40)
    print("result: ", P0_)