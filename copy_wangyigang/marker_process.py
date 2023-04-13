import numpy as np
import time
import icp
from scipy.spatial.transform import Rotation as R
import math
import scipy.linalg as linalg

np.set_printoptions(suppress=True)

# 记Z,X,Y对应的角度分别为yaw,roll,pitch.
# 内旋 YPR
# 行为：Rotate X --> Rotate Y --> Rotate Z
# 结果：R_yaw(Z) * R_pitch(Y) * R_roll(X)

# Constants
N = 10                                    # number of random points in the dataset
num_tests = 1                             # number of test iterations
dim = 3                                     # number of dimensions of the points
noise_sigma = .01                           # standard deviation error to be added
translation = .1                            # max translation of the test set
rotation = .1                               # max rotation (radians) of the test set

# transform 'XYZ'->ZYX->[2,1,0] 'ZYX'->XYZ->[2,1,0],百度使用的是Z->Y->X旋转顺序
def rot_to_eular(Ri):
    # RM_inv = np.linalg.inv(Ri)
    r = R.from_matrix(Ri)
    euler_ = r.as_euler('ZYX', degrees=False)  
    return euler_

def convert_eular(rotation):
    # EulerOrder::XYZ
    n = rotation[:,0]   # col(0)
    o = rotation[:,1]
    a = rotation[:,2]
    y = math.atan2(n[1], n[0])
    p = math.atan2(-n[2], n[0]*math.cos(y) + n[1]*math.sin(y))
    r = math.atan2(a[0]*math.sin(y) - a[1]*math.cos(y), -o[0]*math.sin(y) + o[1]*math.cos(y))
    return y,p,r
        
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

def validration(R1, R2):
    # image to calibration board
    ret = np.dot(R1,R2)
    euler_ = rot_to_eular(ret)
    print("-"*50)

    print("image to car rotoation: \n", ret)
    print("Calibration eular(XYZ)->Rotate order is revert:", euler_) 
    
# R is A to B
def computer_translate(A,B):
    assert A.shape == B.shape
    # print("input dim: ", A.shape[1])
    # Find best fit transform front 
    T, R1, t1 = icp.best_fit_transform(A, B)
    euler_ = rot_to_eular(R1)
    print("-" * 60)
    print("R1: ", R1)
    print("t1: ", t1)
    print("-" * 60) 
    print("Calibration eular(XYZ)->Rotate order is:") 
    print("X: roll {:.2f} or {:.4f}".format(euler_[0], math.radians(euler_[0])))
    print("Y: pitch {:.2f} or {:.4f}".format(euler_[1], math.radians(euler_[1])))
    print("Z: yaw {:.2f} or {:.4f}".format(euler_[2], math.radians(euler_[2])))
    print("-" * 60) 
    return T,R1,t1

if __name__ == "__main__":
    # Marker Corridtion (x,y,z)
    # p1:左上 p2:右上 p3:左下 p4:右下
    # x水平
    M = np.array([[0, 0, 0.0],
                [0.7, 0.0, 0.0],
                [0.0, 0.3, 0.0],
                [0.7, 0.3, 0.0]])
    # x朝下(used)
    M_ = np.array([[0, 0, 0.0],
                [0.0, 0.7, 0.0],
                [0.3, 0.0, 0.0],
                [0.3, 0.7, 0.0]])

    # Vehicle Corridtion
    B_s = np.array([[-0.34701378522480253, -4.59815646444894, 1.98],
                    [-0.9956638082615394, -4.33369945275531, 1.997],
                    [-0.35511679994704193, -4.596285888689118, 1.68],
                    [-1.005814241465687, -4.341858669813336, 1.698]])

    T,R,t = computer_translate(M_,B_s)

    # convert eular
    y1, p1, r1 = convert_eular(R)
    print("-" * 40)
    print("euler_order: XYZ")
    print("yaw:", y1)
    print("pitch:", p1)
    print("roll:", r1)

    # convert
    R1 = convert_rotation(y1, p1, r1)
    print("-" * 40)
    print("R convert: ", R1)
    # validration
    B_o = np.dot(R,M.T)
   
    B_o[:,0] = B_o[:,0] + t
    B_o[:,1] = B_o[:,1] + t
    B_o[:,2] = B_o[:,2] + t
    B_o[:,3] = B_o[:,3] + t

    print("-"*50)
    print("The reprojection: ", B_o)
