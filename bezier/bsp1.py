import numpy as np
from scipy.interpolate import splprep, splev
import matplotlib.pyplot as plt

def bspline_smooth(x, y, num_points=100, degree=3):
    """
    使用B-样条曲线平滑给定的线段数组

    参数：
    x, y: 线段数组的x和y坐标
    num_points: 生成B-样条曲线的点数
    degree: B-样条的次数

    返回：
    smoothed_x, smoothed_y: 平滑后的曲线坐标
    """
    tck, u = splprep([x, y], k=degree, s=0)
    u_new = np.linspace(u.min(), u.max(), num_points)
    smoothed_coords = splev(u_new, tck)

    return smoothed_coords[0], smoothed_coords[1]

# 示例
# 输入线段
x_segments = np.array([1, 2, 3, 4, 5])
y_segments = np.array([1, 3, 1, 4, 2])

# 使用B-样条曲线平滑线段
smoothed_x, smoothed_y = bspline_smooth(x_segments, y_segments)

# 绘制原始线段和平滑后的B-样条曲线
plt.plot(x_segments, y_segments, 'o-', label='origin')
plt.plot(smoothed_x, smoothed_y, 'r-', label='smooth')
plt.legend()
plt.show()
