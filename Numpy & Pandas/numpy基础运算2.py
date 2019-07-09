import numpy as np

A = np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A))
print(np.average(A))

print(np.median(A))
print(np.cumsum(A))#累加的过程
print(np.diff(A))#每两个数中间的差
print(np.nonzero(A))#输出非零数的坐标
print(np.sort(A))
print(np.transpose(A))#转置
print(A.T)#转置
print((A.T).dot(A))

print(np.clip(A,5,9))#所有大于9的数变为9,小于5的变为5,中间的不变

print(np.mean(A,axis=0))
