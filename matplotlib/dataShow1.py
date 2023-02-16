import numpy as np
npa = np.array
# f = open(r"/Users/matt/Desktop/data.txt")
import matplotlib
# matplotlib.use('qt5agg')
from matplotlib import pylab as plt
#
# for line in f.readlines():
#     data = line.strip('\n\r\t ').split(',')
#     if data[-1] == '':
#         data = data[:-1]
#     p = npa([float(each) for each in data[1:]])
#     l = len(p)
#     if l % 2 == 0:
#         ps = p.reshape((l // 2, 2))
#     else:
#         ps = p[:-1].reshape((l // 2, 2))
#     plt.plot(ps[:, 0], ps[:, 1], '*-')

data = np.loadtxt('/Users/matt/Desktop/data.txt', delimiter=',')




from mpl_toolkits.mplot3d import Axes3D
#
x = data[:, 1]
y = data[:, 2]
z = data[:, 3]



# plt.plot(x, y, 'ro')
# for i, (xi, yi) in enumerate(zip(x, y)):
#     plt.text(xi, yi, str(i))
fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)

# x = (x - np.mean(x)) / (x.max() - x.min())
# y = (y - np.mean(y)) / (y.max() - y.min())*20
# z = (z - np.mean(z)) / (z.max() - z.min())
ax.plot(x, y, z, color="deeppink")

ax.set(xlabel="X", ylabel="Y", zlabel="Z")

# ax.set_yticks([-1, 0, 1])
# ax.set_yticklabels(['min', 0, 'max'])
for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
    ax.text(xi, yi, zi, str(i))
ax.set_zticks([-1, 0, 1])

# plt.axis("equal")
# print(x[1:] - x[:-1])
# print(y[1:] - y[:-1])
# diff_x = x[1:] - x[:-1]
# diff_y = y[1:] - y[:-1]
# indx, = np.where(diff_x > 0.1)
# for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
#     ax.text(xi, yi, zi, str(i))
#     if i in (indx):
plt.show()


