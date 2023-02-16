import cmath
import sys

import csv

import pandas


# infile = sys.argv[1]
#
# outfile = sys.argv[2]
infile = '/Users/matt/StudioProjects/map_jni/app/src/main/assets/othercar/track_other_shun.csv'
outfile = '/Users/matt/StudioProjects/map_jni/app/src/main/assets/othercar/track_other_shun_3.csv'
# with open(infile, "r", newline='') as incsv, open(outfile, "w", newline='') as outcsv:
data = pandas.read_csv(infile)
fwriter = csv.writer(open(outfile, "w"))
size = len(data)

for index in range(size):
    currentRowlist = data.values[index]
    if (index + 1 < size):
        nextRowlist = data.values[index + 1]

        startTime = currentRowlist[0]
        startID = int(currentRowlist[1])
        startLon = currentRowlist[2]
        startLat = currentRowlist[3]
        startAlt = currentRowlist[4]
        startAngle = currentRowlist[5]
        startType = int(currentRowlist[6])
        startDuration = currentRowlist[7]

        endTime = int(nextRowlist[0])
        endID = int(nextRowlist[1])
        endLon = nextRowlist[2]
        endLat = nextRowlist[3]
        endAlt = nextRowlist[4]
        endAngle = nextRowlist[5]
        endType = int(nextRowlist[6])
        endDuration = int(nextRowlist[7])

        # 根据速度计算时间
        speed = 60.0/3.6
        dx = endLon - startLon
        dy = endLat - startLat
        distance = cmath.sqrt(dx*dx+dy*dy)*100000
        duration = int((distance/speed*1000).real)
        fwriter.writerow([endTime, endID, endLon, endLat, endAlt, endAngle, endType, duration, endDuration])

        # 计算原始速度
        # dx = endLon - startLon
        # dy = endLat - startLat
        # distance = cmath.sqrt(dx*dx+dy*dy)*100000
        # speed = (distance/(endDuration*0.001)*3.6).real
        # fwriter.writerow([endTime, endID, endLon, endLat, endAlt, endAngle, endType, endDuration,speed])


        # addCount = int((endTime - startTime) / 20)
        # if (addCount > 1):
        #     pDuration = int((endTime - startTime) / addCount)
        #     pLon = (endLon - startLon) / addCount
        #     pLat = (endLat - startLat) / addCount
        #     pAngle = (endAngle - startAngle) / addCount
        #
        #     for pi in range(addCount):
        #         time = int(startTime + pi * pDuration)
        #         lon = startLon + pi * pLon
        #         lat = startLat + pi * pLat
        #         angle = startAngle + pi * pAngle
        #         duration = int(pDuration)
        #         fwriter.writerow([time, startID, lon, lat, startAlt, angle, startType, pDuration])

    else:
        fwriter.writerow(currentRowlist)