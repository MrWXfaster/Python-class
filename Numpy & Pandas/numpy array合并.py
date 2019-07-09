import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B))#上下合并
D = np.hstack((A,B))#左右合并

print(C)#上下合并
print(D)
print(A.shape, D.shape)

print(A.T.shape)#不可以把序列转化为矩阵

print(A[np.newaxis, :].shape)#在 行 上加了个维度
print(A[:, np.newaxis].shape)#在 列 上加了个维度

A1 = np.array([1,1,1])[:,np.newaxis]
B1 = np.array([2,2,2])[:,np.newaxis]

C1 = np.vstack((A,B))
D1 = np.hstack((A,B))

print(A1,B1,C1,D1)

F = np.concatenate((A1,B1,B1,A1),axis=0)#0代表在上下这个方向合并#也就是列方向合并#把每一个array再上下这个方向合并
G = np.concatenate((A1,B1,B1,A1),axis=1)#在行方向合并
print(F, G)