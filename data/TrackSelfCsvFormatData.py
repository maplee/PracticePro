import cmath
import sys

import csv

import pandas

# infile = sys.argv[1]
#
# outfile = sys.argv[2]
infile = '/Users/matt/StudioProjects/map_sdk/appmodule/src/main/assets/track/track_heng_20221009.csv'
outfile = '/Users/matt/StudioProjects/map_sdk/appmodule/src/main/assets/track/track_heng_20221009_2.csv'
# with open(infile, "r", newline='') as incsv, open(outfile, "w", newline='') as outcsv:
data = pandas.read_csv(infile)
fwriter = csv.writer(open(outfile, "w"))
size = len(data)


for index in range(size):
    currentRowlist = data.values[index]
    if (index + 1 < size):
        nextRowlist = data.values[index + 1]

        startTime = int(currentRowlist[0])
        startLon = currentRowlist[1]
        startLat = currentRowlist[2]
        startAlt = currentRowlist[3]
        startAngle = currentRowlist[4]
        startGpsTime = int(currentRowlist[8])

        endTime = int(nextRowlist[0])

        endGpsTime = int(nextRowlist[8])

        if(startTime == endTime or startGpsTime == endGpsTime):
            continue
        else:
            fwriter.writerow([startTime, startLon, startLat, startAlt, startAngle, startAngle, 0, 0,startGpsTime])

        # 计算原始速度
        # duration = endTime - startTime
        # durationGps = endGpsTime - startGpsTime
        # dx = endLon - startLon
        # dy = endLat - startLat
        # distance = cmath.sqrt(dx*dx+dy*dy)*100000
        # speed = (distance/(duration*0.001)*3.6).real
        # speedGps = (distance/(durationGps*0.001)*3.6).real
        # fwriter.writerow([endTime,endGpsTime, endLon, endLat, endAlt, endAngle,speed,speedGps])

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
        #         fwriter.writerow([time, lon, lat, startAlt, angle, 0, 0,0,0])

    else:
        fwriter.writerow(currentRowlist)
