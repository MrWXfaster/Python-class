import numpy as np

A = np.arange(3,15).reshape((3,4))
print(A)
print(A[1][1])#索引出第一行，第一列的值
print(A[2,1])
print(A[2,:])#‘:’ 代表这一列所有的值   #这一行的所有列
print(A[:,2])#这一列的所有行
print(A[1,1:3])#表示第一行的从1到2的值

for row in A:#迭代出每一行
    print(row)

for column in A.T:#迭代出每一列
    print(column)

print(A.flatten())#返回了一个被改变的array
for item in A.flat:#一个迭代器
    print(item)