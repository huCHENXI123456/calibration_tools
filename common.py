import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import cv2
from scipy.spatial.transform import Rotation as R


# https://vimsky.com/zh-tw/examples/detail/python-method-cv2.solvePnP.html
# https://codingdict.com/sources/py/cv2/4595.html
# https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html
# https://github.com/kwea123/VTuber_Unity



def rot_to_eular(_R):
    # RM_inv = np.linalg.inv(_R)
    r = R.from_matrix(_R)
    euler_ = r.as_euler('ZYX', degrees=True)  
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

if __name__ == "__main__":
    # R_ = np.array([[0.00482843,  -0.0212809,    0.999762],[-0.999966,  0.00650889,  0.00496796],[-0.00661306,   -0.999752,  -0.0212488]])
    # R_ = np.array([[-0.595678, 0.0687144, -0.800279],[0.802759, 0.0847991, -0.590243],[0.0273048, -0.994026, -0.105674]])
    # R_ = np.array([[0.567744,  0.0612593,  -0.820923],[ 0.822822, -0.0726512,   0.563636],[-0.0251131,  -0.995474, -0.0916528]])
    # R_ = np.array([[-0.000772621,   -0.0213232,     0.999772 ],[  -0.999984,  -0.00567145, -0.000893745],[0.00568921,    -0.999757,   -0.0213185]])
    R_ = np.array([[0.0292771,  -0.0525226,     0.99819],[-0.999551, -0.00786624,   0.0289031],[0.00633394,   -0.998589,  -0.0527293 ]])
    print("R_:",R_)
    y1, p1, r1 = convert_eular(R_)
    print("-"*50)
    print("euler_order: XYZ")
    print("yaw:", y1)
    print("pitch:", p1)
    print("roll:", r1)
    print("degree.")
    print("yaw:", math.degrees(y1))
    print("pitch:", math.degrees(p1))
    print("roll:", math.degrees(r1))