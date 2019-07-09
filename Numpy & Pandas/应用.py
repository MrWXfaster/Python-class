'''
为什么使用numpy & pandas

1,运算速度快：numpy和pandas都是采用C语言编写的，pandas又是基于numpy,是numpy的升级版。
2,消耗资源少：采用的是矩阵算法，会比python自带的字典或者列表快好多
'''

import m1

m1.printdata('I am Wx')

import numpy as np
list1 = np.random.random((6,416,416,3))
list2 = np.ones((6,416,416,3))
add = list2 - list1
list3 = np.ones((50,3))
add_ = np.sum(list3)
add_1 = add_.astype(np.float32)
print(add_1.dtype)
