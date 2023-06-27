
import math
import numpy as np


pi_2 = math.pi/2

def err_1(a,b):
    return a-b
# 
def W1(x,y):
    cx = 959.078
    cy = 540.696
    fx = 1007.07
    fy = 1006.85
    roll = 1.5875713
    yaw = 1.5702095
    # -: up, +: down
    r1 = (y - cy)/fy
    r_rad = math.atan(r1)
    r_deg = math.degrees(r_rad)

    y1 = (x - cx)/fx
    y_rad = math.atan(y1)
    y_deg = math.degrees(y_rad)

    err_r = err_1(pi_2-roll, r_rad)
    err_y = err_1(pi_2-yaw, y_rad)
    print("Wide calibration roll(rad):", pi_2-roll, ",messure(rad): ", r_rad, ",error(deg): ", math.degrees(err_r))
    print("Wide calibration yaw(rad):", pi_2-yaw, ",messure(rad): ", y_rad, ",error(deg): ", math.degrees(err_y))


def L1(x,y):
    cx = 963.521
    cy = 546.207
    fx = 3887.23
    fy = 3887.23
    roll = 1.5854493
    yaw = 1.5705814
    # -: up, +: down
    r1 = (y - cy)/fy
    r_rad = math.atan(r1)
    r_deg = math.degrees(r_rad)

    y1 = (x - cx)/fx
    y_rad = math.atan(y1)
    y_deg = math.degrees(y_rad)


    err_r = err_1(pi_2-roll, r_rad)
    err_y = err_1(pi_2-yaw, y_rad)
    print("Wide calibration roll(rad):", pi_2-roll, ",messure(rad): ", r_rad, ",error(deg): ", math.degrees(err_r))
    print("Wide calibration yaw(rad):", pi_2-yaw, ",messure(rad): ", y_rad, ",error(deg): ", math.degrees(err_y))


def M1(x,y):
    cx = 964.902
    cy = 533.478
    fx = 1839.78
    fy = 1839.15
    roll = 1.5801162
    yaw = 1.5707952
    # -: up, +: down
    r1 = (y - cy)/fy
    r_rad = math.atan(r1)
    r_deg = math.degrees(r_rad)

    y1 = (x - cx)/fx
    y_rad = math.atan(y1)
    y_deg = math.degrees(y_rad)

    err_r = err_1(pi_2-roll, r_rad)
    err_y = err_1(pi_2-yaw, y_rad)
    print("Wide calibration roll(rad):", pi_2-roll, ",messure(rad): ", r_rad, ",error(deg): ", math.degrees(err_r))
    print("Wide calibration yaw(rad):", pi_2-yaw, ",messure(rad): ", y_rad, ",error(deg): ", math.degrees(err_y))


def LR(x,y):
    cx = 964.902
    cy = 533.478
    fx = 1839.78
    fy = 1839.15
    roll = 1.5801162
    yaw = 1.5707952
    # -: up, +: down
    r1 = (y - cy)/fy
    r_rad = math.atan(r1)
    r_deg = math.degrees(r_rad)

    y1 = (x - cx)/fx
    y_rad = math.atan(y1)
    y_deg = math.degrees(y_rad)

    err_r = err_1(pi_2-roll, r_rad)
    err_y = err_1(pi_2-yaw, y_rad)
    print("LR calibration roll(rad):", pi_2-roll, ",messure(rad): ", r_rad, ",error(deg): ", math.degrees(err_r))
    print("LR calibration yaw(rad):", pi_2-yaw, ",messure(rad): ", y_rad, ",error(deg): ", math.degrees(err_y))

if __name__ == '__main__':
    print("-"*60)
    print("B02 calibration and laneline messure compare result >>>>>")
    print("-"*60)
    W1(956,516)
    print("-"*60)
    L1(948,468)
    print("-"*60)
    M1(960,503)
    print("-"*60)
    # LF(956,516)
    # RF(956,516) 
    LR(173,400)
               
    # RR(1,1)    


# cx =
# cy = 

# fx = 
# fy = 

# vpx = 

# vpy = 


# tx = (vpx - cx)/fx 

# x_yaw = atan(tx) 
# x_yaw_1 = math.degrees(x_yaw)


# y_roll = 

# # middle

# roll
# -0.9494064862815774
# -0.533989400249489
# yaw
# -0.1526613217511418
# 6.456059194632562e-05

# # long
# roll
# -1.1525756360163355
# -0.8395535219707135
# yaw
# -0.22877037582469645
# 0.012314398251845717

# # wide
# roll 
# -1.405068195771371
# -0.9611351660974717
# yaw 
# -0.17511777751123564
# 0.03362269865275992