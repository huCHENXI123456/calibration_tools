
#encoding:UTF-8

# camera to camera extrinsics conversion
# 已知：camera1 to lidar16 extrinsics, and camera2 to lidar16 extrinsics, 求解 camera1 -> camera2 or camera2 -> camera1 extrinsics.


import numpy as np
from scipy.spatial.transform import Rotation as R


def qtor(q_):
    # 四元数到旋转矩阵
    r = R.from_quat(q_)
    R_ = r.as_matrix()
    return R_

def rtoq(r_):
    # 旋转矩阵到四元数
    _r = R.from_matrix(r_)
    q_ = _r.as_quat()
    return q_

# From c1 to c2 
def main(c1, c2):
    c12 = []
    print("c1[0:4]", c1[0:4])
    R1 = qtor(c1[0:4])
    R2 = qtor(c2[0:4])
    R2_ = np.matrix(R2).I
    R12 = np.dot(R2_, R1)
    q12 = rtoq(R12)
    print("R12: \n", R12)
    t12_ = np.array(c1[4:]) - np.array(c2[4:])
    print("t12_ shape: ", t12_.shape)
    t12 = np.dot(R2_, t12_)
    print("t12: ", t12)
    return c12

if __name__ == "__main__":
    K6 = [2.0861597172498164e+03, 0., 9.5057223449235289e+02, 0.,2.0878898342380035e+03,5.2959928591229880e+02, 0., 0., 1.]
    K12 = [3.9928730702442631e+03, 0., 9.6803105595291413e+02, 0.,3.9938781972371780e+03, 5.7696760488326117e+02, 0., 0., 1.]


    c12mm = [-0.4895608893727003, 0.4947581384304134, -0.4975291324513065, 0.517696129419308, 0.09809876978397369, -0.1160668432712555, 1.301018834114075]
    c6mm = [-0.4943262508793445, 0.4862925849778401, -0.5095878953871362, 0.5093930273983447, -0.06302474439144135, -0.06466559320688248, 1.298461437225342]
    print("-" * 50)
    print("camera(6mm) intrisic: ", K6)
    print("camera(12mm) intrisic: ", K12)
    print("--------------- camera6mm to camera12mm: ")
    cout = main(c6mm, c12mm)    
    print("--------------- camera(12mm) to camera(6mm): ")
    cout = main(c12mm, c6mm)      