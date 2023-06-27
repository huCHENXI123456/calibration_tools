#coding:UTF-8
import time
 
timeStamp = 1682491534
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

######################################
dt = "2023-03-14 16:03:03"

#转换成时间数组
timeArray1 = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp1 = time.mktime(timeArray1)

print( timestamp1)