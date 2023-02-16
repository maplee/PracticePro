import cmath
import struct
import sys

import csv

import pandas

# infile = sys.argv[1]
#
# outfile = sys.argv[2]
infile = '/Users/matt/Desktop/track/fly_result_s.csv'
outfile = '/Users/matt/Desktop/track/fly_str.txt'
# with open(infile, "r", newline='') as incsv, open(outfile, "w", newline='') as outcsv:
data = pandas.read_csv(infile, header=None)
# fwriter = csv.writer(open(outfile, "w"))
size = len(data)

f = open(outfile, 'w')

index = 0

dataVals=data.values
strTemp = ""
while index < size:

    currentRowlist = dataVals[index]
    startLon = currentRowlist[0]
    startLat = currentRowlist[1]
    strTemp += "{},{},".format(startLon, startLat)
    index += 1

f.write(strTemp)
f.close()