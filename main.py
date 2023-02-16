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

person = np.dtype([('name','S20'),('age','i1'),('gender','i1')])
print(person)
pp = np.array([('aa',18,1),('bb',33,0),('cc',31,1)],dtype=person)
print(pp['name'])
print(pp['age'])
print(pp['gender'])

a = np.array([[1,2,3,4],[5,6,7,8]])
a = a.reshape(4,2)
print(a)
a = np.arange(120)
print(a)
b = a.reshape(2,3,4,5)
print(b)
