import numpy as np

# 构造系数矩阵 A 和常数向量 b
A = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([7, 8, 9])

# 求解最小二乘问题
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

# x 是最小二乘解，residuals 是残差平方和，rank 是 A 的秩，s 是 A 的奇异值
print("最小二乘解:", x)
print("残差平方和:", residuals)
print("A 的秩:", rank)
print("A 的奇异值:", s)
