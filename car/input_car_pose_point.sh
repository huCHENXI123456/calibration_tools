#!/bin/bash
#1-input measure point
#2-change master calib config
#3-change slave calib config
L_P_X=0
L_P_Y=0
R_P_X=0
R_P_Y=0

CONFIG_PATH='/opt/data/deepway/cxk/output/linux-arm/ANP/conf/calibration/configs/dw_anp/calib_configs.prototxt'

function update_config_path() {
    read -p "Input config path:" CONFIG_PATH
    echo $CONFIG_PATH
}

function get_point(){
    read -p "Left Point X: " L_P_X
    read -p "Left Point Y: " L_P_Y
    read -p "Right Point X: " R_P_X
    read -p "Right Point Y: " R_P_Y
}

function change_point(){
    DATA='measure_point_l {\n\tx:'${L_P_X}'\n\ty:'${L_P_Y}'\n\tz:0\n}\nmeasure_point_r {\n\tx:'${R_P_X}'\n\ty:'${R_P_Y}'\n\tz:0\n}'
    sed -i '37,46d' $CONFIG_PATH
    echo -e $DATA >> $CONFIG_PATH
    #sed -i '$a '$(echo -e $DATA)'' configs/dw_anp/calib_configs.prototxt
}

function update_data() {
    DATA='measure_point_l {\\n\\tx:'${L_P_X}'\\n\\ty:'${L_P_Y}'\\n\\tz:0\\n}\\nmeasure_point_r {\\n\\tx:'${R_P_X}'\\n\\ty:'${R_P_Y}'\\n\\tz:0\\n}'
}

function change_master(){
    sshpass -p 123 ssh -o StrictHostKeyChecking=no root@172.16.1.112 "
                        sed -i '37,46d' ${CONFIG_PATH}; \
                        echo -e "${DATA}" >> ${CONFIG_PATH}; \
                        echo 'master change result:'
                        tail -10 ${CONFIG_PATH};"
}
function change_slave(){
    sshpass -p 123 ssh -o StrictHostKeyChecking=no root@172.16.1.32 "
                        sed -i '37,46d' ${CONFIG_PATH}; \
                        echo -e "${DATA}" >> ${CONFIG_PATH}; \
                        echo 'slave change result:'
                        tail -10 ${CONFIG_PATH};"
}

function running(){
    get_point
    update_data
    change_master
    change_slave
}

running
