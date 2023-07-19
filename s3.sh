#!/bin/bash
LOG="/home/one/calib_data/1801/1801_5/ica/mlog/log-0/HAVP/lat_controller_log_2023-07-06_110555.csv"
python3 lat_plot.py $LOG
echo "----------- Done -------------"