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
index = 0

dataVals=data.values

while index < size:
    index = loopIndex+1
    if(index >= size):
        break
    currentRowlist = dataVals[index]
    startTime = int(currentRowlist[0])
    startLon = currentRowlist[1]
    startLat = currentRowlist[2]
    loopIndex = index + 1
    if (index == 0):
        fwriter.writerow([startTime,startLon, startLat])

    while loopIndex < size:
        nextRowlist = dataVals[loopIndex]
        loopIndex += 1
        endTime = int(nextRowlist[0])
        endLon = nextRowlist[1]
        endLat = nextRowlist[2]

        # 计算距离
        dx = endLon - startLon
        dy = endLat - startLat
        distance = cmath.sqrt(dx * dx + dy * dy).real * 100000.0
        if (distance >= 3.0):
            fwriter.writerow([endTime, endLon, endLat])
            break
        else:
            continue

    index += 1

