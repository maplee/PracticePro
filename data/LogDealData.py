import cmath
import sys

import csv

import pandas

input_file = '/Users/matt/Desktop/20230518/11.txt'
output_file = '/Users/matt/Desktop/20230518/11_oo.txt'
# 打开输入文件和输出文件
flag = 0
with open(input_file, 'r', encoding='utf-8', errors='ignore') as file_in, open(output_file, 'w') as file_out:
    # 逐行读取输入文件
    for line in file_in:
        if (line.startswith("05-18 15:29:04.682 I/AMapViewWrapper(22907): Roam--op-onRoamStatus")):
            # 写入输出文件
            flag = 1

        if (flag == 1):
            file_out.write(line)