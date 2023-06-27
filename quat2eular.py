
import numpy as np
from scipy.spatial.transform import Rotation as R
import math



def fun1(q_i) :
    # 四元数到旋转矩阵
    r = R.from_quat(q_i)
    R_o = r.as_matrix()
    return R_o

def convert_eular(rotation, translation):
    # EulerOrder::XYZ
    n = rotation[:,0]   # col(0)
    o = rotation[:,1]
    a = rotation[:,2]
    y = math.atan2(n[1], n[0])
    p = math.atan2(-n[2], n[0]*math.cos(y) + n[1]*math.sin(y))
    r = math.atan2(a[0]*math.sin(y) - a[1]*math.cos(y), -o[0]*math.sin(y) + o[1]*math.cos(y))

    print("The lidar to Novatel degree of Yaw(z): ", math.degrees(y), " Pitch(y): ", math.degrees(p), " roll(x): ", math.degrees(r))
    print("The lidar to Novatel translation(x,y,z(m)) ", translation)
    return y,p,r


if __name__ == "__main__":
    t_i = [0.006672002530040285, 4.605818569865533, -0.01]    
    q_i = [ 0.00486933
            ,0.001981509
            ,0.697969
            ,0.71610856] 

    q_l2g = [0.00812208, -0.00280499, 0.70070796, 0.71339646]   
    r_o = fun1(q_l2g)
    print("rotation: \n", r_o)
    convert_eular(r_o, t_i)

    r_i = np.array([0.00382471,-0.999992,-0.00070554,-0.0125114],
                    [-0.0132276,0.000654817,-0.999912,-0.379526],
                    [0.999905,0.00383377,-0.0132251,-0.551037])


