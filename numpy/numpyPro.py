# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


a = np.array([1, 2, 3])
print(a)
a = np.array([[1, 2], [3, 4]])
print(a)
a = np.array([[1, 2, '1'], [3, 4, '1']])
print(a)

dt = np.dtype('i8')
print(dt)
dt = np.dtype('>i8')
print(dt)
dtSex = np.dtype([('sex', np.int8)])
print(dt)
dt = np.dtype([('age', np.int64)])
print(dt)
a = np.array([10, 20, 30], dtype=dt)
b = np.array([0, 1, 2], dtype=dtSex)
print(a)
print(a['age'])
print(b['sex'])

person = np.dtype([('name', 'S20'), ('age', 'i1'), ('gender', 'i1')])
print(person)
pp = np.array([('aa', 18, 1), ('bb', 33, 0), ('cc', 31, 1)], dtype=person)
print(pp['name'])
print(pp['age'])
print(pp['gender'])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
a = a.reshape(4, 2)
print(a)
a = np.arange(120)
print(a)
b = a.reshape(2, 3, 4, 5)
print(b)

x = [1, 2, 3]
a = np.asarray(x)
print(a)
a = np.asarray(x, dtype=float)
print(a)
x = (1, 2, 3)
a = np.asarray(x)
print(a)
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x, dtype=object)
print(a)

s = 'Hello World'
a = np.frombuffer(np.asarray(s), dtype='S1')
print(a)

list = range(5)
it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=float)
print(x)

x = np.linspace(10, 20, 5)
print(x)

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('我们的数组是：')
print(a)
# 这会返回第二列元素的数组：
print('第二列的元素是：')
print(a[..., 1])
print('\n')
# 现在我们从第二行切片所有元素：
print('第二行的元素是：')
print(a[1, ...])
print('\n')
# 现在我们从第二列向后切片所有元素：
print('第二列及其剩余元素是：')
print(a[..., 1:])
