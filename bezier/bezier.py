import matplotlib.pyplot as plt
import numpy as np


# 计算二次贝塞尔曲线
def quadratic_bezier(p0, p1, p2, t):
    """
    计算二次贝塞尔曲线上给定参数 t 的点

    Args:
        p0, p1, p2 (numpy.ndarray): 控制点的坐标
        t (float): 参数，取值范围 [0, 1]

    Returns:
        numpy.ndarray: 给定参数 t 时的点坐标
    """
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2


# 计算三次贝塞尔曲线
def cubic_bezier(p0, p1, p2, p3, t):
    """
    计算三次贝塞尔曲线上给定参数 t 的点

    Args:
        p0, p1, p2, p3 (numpy.ndarray): 控制点的坐标
        t (float): 参数，取值范围 [0, 1]

    Returns:
        numpy.ndarray: 给定参数 t 时的点坐标
    """
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3

def n_bezier(control_points, t):
    """
    计算 n 次贝塞尔曲线上给定参数 t 的点

    Args:
        control_points (list): 控制点的坐标列表，每个控制点是一个 numpy.ndarray
        t (float): 参数，取值范围 [0, 1]

    Returns:
        numpy.ndarray: 给定参数 t 时的点坐标
    """
    n = len(control_points) - 1
    if n == 1:
        return (1 - t) * control_points[0] + t * control_points[1]
    else:
        new_control_points = [n_bezier([control_points[i], control_points[i + 1]], t) for i in range(n)]
        return n_bezier(new_control_points, t)


# 二次贝塞尔曲线
p0 = np.array([0, 0])  # 起始点
p1 = np.array([2, 4])  # 控制点1
p2 = np.array([4, 0])  # 终止点

t_values = np.linspace(0, 1, 10)  # 参数t的取值范围
curve = np.array([quadratic_bezier(p0, p1, p2, t) for t in t_values])  # 计算二次贝塞尔曲线上的点

# 绘制二次贝塞尔曲线和控制线
plt.plot(curve[:, 0], curve[:, 1], label='Quadratic Bezier Curve')  # 绘制二次贝塞尔曲线
plt.plot([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], linestyle='--', marker='o', label='Control Line')  # 绘制控制线
plt.title('Quadratic Bezier Curve with Control Line')  # 设置图表标题
plt.legend()  # 显示图例
plt.show()  # 显示图表

# 三次贝塞尔曲线
p0 = np.array([0, 0])  # 起始点
p1 = np.array([1, 2])  # 控制点1
p2 = np.array([3, 2])  # 控制点2
p3 = np.array([4, 0])  # 终止点

t_values = np.linspace(0, 1, 100)  # 参数t的取值范围
curve = np.array([cubic_bezier(p0, p1, p2, p3, t) for t in t_values])  # 计算三次贝塞尔曲线上的点

# 绘制三次贝塞尔曲线和控制线
plt.plot(curve[:, 0], curve[:, 1], label='Cubic Bezier Curve')  # 绘制三次贝塞尔曲线
plt.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], linestyle='--', marker='o',
         label='Control Line')  # 绘制控制线
plt.title('Cubic Bezier Curve with Control Line')  # 设置图表标题
plt.legend()  # 显示图例
plt.show()  # 显示图表


# 控制点
control_points = [np.array([0, 0]), np.array([1, 2]), np.array([3, 2]), np.array([4, 0]), np.array([5, -1])]

t_values = np.linspace(0, 1, 100)  # 参数t的取值范围
curve = np.array([n_bezier(control_points, t) for t in t_values])  # 计算 n 次贝塞尔曲线上的点

# 绘制 n 次贝塞尔曲线和控制线
plt.plot(curve[:, 0], curve[:, 1], label='n-Bezier Curve')  # 绘制 n 次贝塞尔曲线
plt.plot([point[0] for point in control_points], [point[1] for point in control_points], linestyle='--', marker='o',
         label='Control Line')  # 绘制控制线
plt.title('n-Bezier Curve with Control Line')  # 设置图表标题
plt.legend()  # 显示图例
plt.show()  # 显示图表
