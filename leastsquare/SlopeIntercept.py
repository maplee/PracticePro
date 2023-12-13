import numpy as np

# 观测数据
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 3, 3.5, 5])

# 计算最小二乘法斜率和截距
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xx = np.sum(x * x)
sum_xy = np.sum(x * y)

# 计算斜率 (m) 和截距 (c)
# m = (n(∑xy)−(∑x)(∑y))/(n(∑xx)−(∑x)(∑x))
# c = (∑y−m(∑x))/n

m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
c = (sum_y - m * sum_x) / n

# 输出结果
print(f"斜率 (m): {m}")
print(f"截距 (c): {c}")
