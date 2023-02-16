import matplotlib.pyplot as plt

import numpy as np

data = np.arange(10)
# data.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(data)
# plt.plot(data)
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
# plt.plot(np.random.randn(30).cumsum(), 'k--')
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
# plt.plot(np.random.randn(100).cumsum(), 'k--')
ax3 = fig.add_subplot(2, 2, 4)
plt.plot(np.random.randn(50).cumsum(), 'k--')

# fig = plt.figure()
# ax1 = fig.add_subplot(3, 1, 1)
# plt.plot(np.random.randn(30).cumsum(), 'k--')
# ax2 = fig.add_subplot(3, 1, 2)
# plt.plot(np.random.randn(100).cumsum(), 'k--')
# ax3 = fig.add_subplot(3, 1, 3)
# plt.plot(np.random.randn(50).cumsum(), 'k--')

plt.show()
