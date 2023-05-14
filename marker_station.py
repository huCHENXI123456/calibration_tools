import sys
import math
import yaml
import csv
import numpy as np
import marker_data as m_c
import marker_process as m_p

def save_station(ret, file_name, station_id):
    with open(file_name, 'w+') as f:
        f.write("name: " + "\"Deepway\"" + "\n")
        f.write("id: " + str(station_id) + "\n")
        f.write("frame_id: " + "\"world\"" + "\n")
        f.write("rear_load: true" + "\n")

        for i in range(len(ret)):
            print("="*30, "ret[", i, "]", "="*30)
            B_s = np.array(ret[i])
            T, R, t = m_p.computer_translate(m_c.M_I, B_s)
            # Raw Pose
            y1, p1, r1 = m_p.convert_eular(R)
            euler_out = m_p.rot_to_eular(R)

            # eular
            if False:
                print("yaw: ", y1, "pitch: ", p1, "roll: ", r1)
                print("euler(p[0]->p[1]->z): ", euler_out)
                print("x: ", t[0], "y: ", t[1], "z: ", t[2])

            # verify
            if False:
                R1 = m_p.convert_rotation(y1, p1, r1)
                print("[main] verify R convert: ", R1)

            f.write("markers { \n")
            f.write("\tid: " + str(i+1) + "\n")
            if i == 0:
                f.write("\tname: " + "\"" + "P1" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P1" + "\"" + "\n")
            if i == 1:
                f.write("\tname: " + "\"" + "P2" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P2" + "\"" + "\n")
            if i == 2:
                f.write("\tname: " + "\"" + "P3" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P3" + "\"" + "\n")
            if i == 3:
                f.write("\tname: " + "\"" + "P4" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P4" + "\"" + "\n")
            if i == 4:
                f.write("\tname: " + "\"" + "P5" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P5" + "\"" + "\n")
            if i == 5:
                f.write("\tname: " + "\"" + "P6" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P6" + "\"" + "\n")
            if i == 6:
                f.write("\tname: " + "\"" + "P7" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P7" + "\"" + "\n")
            if i == 7:
                f.write("\tname: " + "\"" + "P8" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P8" + "\"" + "\n")
            if i == 8:
                f.write("\tname: " + "\"" + "P9" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P9" + "\"" + "\n")
            if i == 9:
                f.write("\tname: " + "\"" + "P10" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P10" + "\"" + "\n")

            f.writelines("\ttype: CHESS_BOARD" + "\n")
            f.writelines("\tpose {" + "\n")
            f.writelines("\t\tframe_id: "+"\"world\"" + "\n")
            f.writelines("\t\tposition {" + "\n")
            f.write("\t\t\tx: " + str(t[0]) + "\n")
            f.write("\t\t\ty: " + str(t[1]) + "\n")
            f.write("\t\t\tz: " + str(t[2]) + "\n")
            f.writelines("\t\t} \n")
            f.writelines("\t\teuler_angles { \n\t\t\teuler_order: XYZ" + "\n")
            f.write("\t\t\tyaw: " + str(y1) + "\n")
            f.write("\t\t\tpitch: " + str(p1) + "\n")
            f.write("\t\t\troll: " + str(r1) + "\n")
            f.writelines("\t\t} \n")
            f.writelines("\t} \n")
            
            if i == 0:    # The Front marker
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_MIDDLE_CAMERA " + "\n")
            if i == 1 or i == 2:    # The Front marker
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_MIDDLE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_LONG_CAMERA " + "\n")
            if i == 3:    # The Front marker
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_MIDDLE_CAMERA " + "\n")
            
            if i == 4:    # The leftFront marker
                f.writelines("\tobservers: LEFT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
            if i == 5:    # The leftRear marker
                f.writelines("\tobservers: LEFT_REAR_CAMERA " + "\n")
            if i == 6:    # The rightFront marker
                f.writelines("\tobservers: RIGHT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
            if i == 7:      # The rightRear marker
                f.writelines("\tobservers: RIGHT_REAR_CAMERA " + "\n")

            if i == 8:      # The leftMiddle marker
                f.writelines("\tobservers: LEFT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: LEFT_REAR_CAMERA " + "\n")
            if i == 9:      # The rightMiddle marker
                f.writelines("\tobservers: RIGHT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: RIGHT_REAR_CAMERA " + "\n")

            f.writelines("\tused: true"+"\n")
            f.writelines(
                "\tdata:" + "\"rows: 5\\ncols: 9\\nsquare_size: 0.10\\ninner_only: true\\n\"" + "\n")
            f.writelines(
                "\troi { \n\t\tauto_roi: true \n\t\tscale: 2.0" + "\n")
            f.writelines("\t} \n")
            f.writelines("\tsolve_pose: true" + "\n")
            f.writelines("\tscale: 2.5" + "\n")
            f.writelines("\tuse_opencv: true" + "\n")
            f.writelines("} \n")
    f.close()

def save_station_cp(ret, file_name, station_id, init_yaw, poffset):
    with open(file_name, 'w+') as f:
        f.write("name: " + "\"Deepway\"" + "\n")
        f.write("id: " + str(station_id) + "\n")
        f.write("frame_id: " + "\"world\"" + "\n")
        f.write("rear_load: true" + "\n")

        for i in range(len(ret)):
            print("="*25, "ret[", i, "]", "="*25)
            B_s = np.array(ret[i])
            T, R, t = m_p.computer_translate(m_c.M_I, B_s)
            # Raw Pose
            y1, p1, r1 = m_p.convert_eular(R)
            euler_out = m_p.rot_to_eular(R)
            # component angle and translation
            # R_z_set = m_p.convert_rotation(yaw, 0, 0)
            R_z_set = m_p.convert_rotation(init_yaw, 0, 0)
            R_c = np.dot(R_z_set, R)
            t_c = np.dot(R_z_set, t) + np.array(poffset)
            y1_c, p1_c, r1_c = m_p.convert_eular(R_c)

            # eular
            if False:
                print("-"*60)
                print("raw yaw: ", math.degrees(y1), "pitch: ", math.degrees(p1), "roll: ", math.degrees(r1))
                print("raw euler(p[0]->p[1]->z): ", euler_out)
                print("raw t: ", t)
                print("-"*60)
                print("new degrees yaw:", math.degrees(y1_c), ",pitch:", math.degrees(p1_c), ",roll:", math.degrees(r1_c))
                print("new t1: ", t_c)
            # verify
            if False:
                R1 = m_p.convert_rotation(y1, p1, r1)
                print("[main] verify R convert: ", R1)


            f.write("markers { \n")
            f.write("\tid: " + str(i+1) + "\n")
            if i == 0:
                f.write("\tname: " + "\"" + "P1" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P1" + "\"" + "\n")
            if i == 1:
                f.write("\tname: " + "\"" + "P2" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P2" + "\"" + "\n")
            if i == 2:
                f.write("\tname: " + "\"" + "P3" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P3" + "\"" + "\n")
            if i == 3:
                f.write("\tname: " + "\"" + "P4" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P4" + "\"" + "\n")
            if i == 4:
                f.write("\tname: " + "\"" + "P5" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P5" + "\"" + "\n")
            if i == 5:
                f.write("\tname: " + "\"" + "P6" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P6" + "\"" + "\n")
            if i == 6:
                f.write("\tname: " + "\"" + "P7" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P7" + "\"" + "\n")
            if i == 7:
                f.write("\tname: " + "\"" + "P8" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P8" + "\"" + "\n")
            if i == 8:
                f.write("\tname: " + "\"" + "P9" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P9" + "\"" + "\n")
            if i == 9:
                f.write("\tname: " + "\"" + "P10" + "\"" + "\n")
                f.write("\tframe_id: " + "\"" + "P10" + "\"" + "\n")

            f.writelines("\ttype: CHESS_BOARD" + "\n")
            f.writelines("\tpose {" + "\n")
            f.writelines("\t\tframe_id: "+"\"world\"" + "\n")
            f.writelines("\t\tposition {" + "\n")
            f.write("\t\t\tx: " + str(t_c[0]) + "\n")
            f.write("\t\t\ty: " + str(t_c[1]) + "\n")
            f.write("\t\t\tz: " + str(t_c[2]) + "\n")
            f.writelines("\t\t} \n")
            f.writelines("\t\teuler_angles { \n\t\t\teuler_order: XYZ" + "\n")
            f.write("\t\t\tyaw: " + str(y1_c) + "\n")
            f.write("\t\t\tpitch: " + str(p1_c) + "\n")
            f.write("\t\t\troll: " + str(r1_c) + "\n")
            f.writelines("\t\t} \n")
            f.writelines("\t} \n")
            
            if i == 0:    # The Front marker
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_MIDDLE_CAMERA " + "\n")
            if i == 1 or i == 2:    # The Front marker
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_MIDDLE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_LONG_CAMERA " + "\n")
            if i == 3:    # The Front marker
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_MIDDLE_CAMERA " + "\n")
            
            if i == 4:    # The leftFront marker
                f.writelines("\tobservers: LEFT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
            if i == 5:    # The leftRear marker
                f.writelines("\tobservers: LEFT_REAR_CAMERA " + "\n")
            if i == 6:    # The rightFront marker
                f.writelines("\tobservers: RIGHT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: FRONT_WIDE_CAMERA " + "\n")
            if i == 7:      # The rightRear marker
                f.writelines("\tobservers: RIGHT_REAR_CAMERA " + "\n")

            if i == 8:      # The leftMiddle marker
                f.writelines("\tobservers: LEFT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: LEFT_REAR_CAMERA " + "\n")
            if i == 9:      # The rightMiddle marker
                f.writelines("\tobservers: RIGHT_FRONT_CAMERA " + "\n")
                f.writelines("\tobservers: RIGHT_REAR_CAMERA " + "\n")

            f.writelines("\tused: true"+"\n")
            f.writelines(
                "\tdata:" + "\"rows: 5\\ncols: 9\\nsquare_size: 0.10\\ninner_only: true\\n\"" + "\n")
            f.writelines(
                "\troi { \n\t\tauto_roi: true \n\t\tscale: 2.0" + "\n")
            f.writelines("\t} \n")
            f.writelines("\tsolve_pose: true" + "\n")
            f.writelines("\tscale: 2.5" + "\n")
            f.writelines("\tuse_opencv: true" + "\n")
            f.writelines("} \n")
    f.close()