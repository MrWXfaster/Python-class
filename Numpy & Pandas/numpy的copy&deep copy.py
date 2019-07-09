import numpy as np

a = np.arange(4)

b = a
c = a
d = b

a[0] = 11
print(a)
print(b is a)
print(d)
'''改变其中任意值均会改变其他的值'''
b = a.copy() #deep copy把值赋给了b,但没有相关联
a[3]=44
print(a)
print(np.array(b))
'''只改变了a,b不会发生改变'''