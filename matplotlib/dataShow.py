import numpy as np
npa = np.array
f = open(r"/Users/matt/Desktop/data.txt")
import matplotlib
matplotlib.use('qt5agg')
from matplotlib import pylab as plt

for line in f.readlines():
    data = line.strip('\n\r\t ').split(',')
    if data[-1] == '':
        data = data[:-1]
    p = npa([float(each) for each in data[1:]])
    l = len(p)
    if l % 2 == 0:
        ps = p.reshape((l // 2, 2))
    else:
        ps = p[:-1].reshape((l // 2, 2))
    plt.plot(ps[:, 0], ps[:, 1], '*-')
plt.show()
