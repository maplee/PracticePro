import cmath
import struct
import sys

import csv
import random

import pandas

outfile = '/Users/matt/Desktop/input/input_param.txt'

size = 720

f = open(outfile, 'w')

index = 1

strTemp = ""
while index <= size:
    m = random.randint(10,100)+random.randint(0,100)/100
    strTemp += "{}:{},".format(index/2.0, m)
    index += 1

f.write(strTemp)
f.close()