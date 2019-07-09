import numpy as np

a = np.array([2,23,4],dtype = np.int)#int默认64位
print(a)
'''[ 2 23  4],无逗号分割，这是和列表的区别'''
print(a.dtype)
b = np.zeros((3,4))
c  = np.ones((3,4),dtype = np.int16)
d = np.empty((3,4))
e = np.arange(10,20,2)
a = np.arange(12).reshape((3,4))

print(a,b,c,d,e)

f = np.linspace(0,10,6)#生成等长序列
print(f)

g = f.reshape((2,3))
print(g)