import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt


def bezier_smooth(points, num_points=100):
    # 将点数组转换为NumPy数组
    points = np.array(points)

    # 获取点数组的长度
    n = len(points)

    if n < 2:
        raise ValueError("至少需要两个点来进行平滑")

    # 将点数组拆分为X和Y坐标
    x = points[:, 0]
    y = points[:, 1]

    # 使用make_interp_spline函数创建插值器
    t = np.arange(0, 1.1, 0.1)
    spl = make_interp_spline(np.linspace(0, 6, n), np.column_stack((x, y)), k=3)

    # 在指定数量的点上进行插值
    smoothed_points = spl(t)

    return smoothed_points


# 示例用法
if __name__ == "__main__":
    # 原始线段数组
    original_points = np.array([
        [0, 0],
        [1, 1],
        [2, 0],
        [3, 1],
        [4, 0]
    ])

    # 对线段数组进行贝塞尔平滑
    smoothed_points = bezier_smooth(original_points)

    # 绘制结果
    plt.figure(figsize=(8, 6))
    plt.plot(original_points[:, 0], original_points[:, 1], 'ro-', label='原始线段')
    plt.plot(smoothed_points[:, 0], smoothed_points[:, 1], 'g-', label='贝塞尔平滑')
    plt.title('线段数组贝塞尔平滑')
    plt.legend()
    plt.show()
