'''
深拷贝，包含对象里面的所有嵌入部分的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
'''
import numpy as np
list = [1, 2]
c = np.copy(list)
print(list,'\n',c)
list[0]=5
print(list,'\n',c)  # 拷贝了对象以及所有子对象，所以原始数据改变，子对象不变
x = np.floor(3.8)
print(x)

