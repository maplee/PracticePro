import cmath
import struct
import sys

import csv

import pandas

# infile = sys.argv[1]
#
# outfile = sys.argv[2]
infile = '/Users/matt/Desktop/track/self.csv'
outfile = '/Users/matt/Desktop/track/fly.csv'
# with open(infile, "r", newline='') as incsv, open(outfile, "w", newline='') as outcsv:
data = pandas.read_csv(infile, header=None)
fwriter = csv.writer(open(outfile, "w"))
size = len(data)
loopIndex = 0


def hexToDouble(hexString):  # 16进制转double
    return struct.unpack('>d', bytes.fromhex(hexString))[0]
dataVals=data.values
for index in range(size):

    if index < loopIndex:
        continue
    currentRowlist = dataVals[index]
    startTime = int(currentRowlist[0])
    startLon = currentRowlist[1]
    startLat = currentRowlist[2]
    if (index == 0):
        fwriter.writerow([startTime,startLon, startLat])

    # print(data)
    # for tindex, nextRowlist in enumerate(dataVals[index+1:],start=index+1):
    for tindex in range(size):
        if tindex <= index:
            continue
        loopIndex = tindex
        nextRowlist = dataVals[tindex]
        # print(nextRowlist)
        endTime = int(nextRowlist[0])
        endLon = nextRowlist[1]
        endLat = nextRowlist[2]

        # 计算距离
        dx = endLon - startLon
        dy = endLat - startLat
        distance = cmath.sqrt(dx*dx+dy*dy).real*100000.0
        if (distance >= 3.0):
            fwriter.writerow([endTime,endLon, endLat])
            break
        else:
            continue

