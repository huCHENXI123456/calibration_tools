#

scp *.prototxt root@172.16.1.112:/opt/data/deepway/calibration/output/latest/ANP/conf/calibration/configs/wm_anp/stations
scp *.prototxt root@172.16.1.32:/opt/data/deepway/calibration/output/latest/ANP/conf/calibration/configs/wm_anp/stations



# computer compentation
.s1.sh

## generate stations
.s2.sh

## lane verify
.s3.sh



## Git
### push    
git add .
git commit -m "new lidar"
git push origin1 calibration

### pull
git pull origin1 calibration