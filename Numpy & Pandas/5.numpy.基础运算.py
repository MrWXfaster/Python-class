import numpy as np
a = np.array([[10,20],
             [30,40]])
b = np.array(4)
f = np.arange(4).reshape((2,2))

c  = a*f#逐个相乘
c_dot = np.dot(a,f)#矩阵相乘
c_dot1 = a.dot(f)
print(c,c_dot,c_dot1)

print(a,b)
c = a**b
print(c)

d = 10*np.sin(a)
e = 10*np.cos(a)

print(d,e)

print(f)
print(f<3)

h = np.random.random((2,4))
print(h)
print(np.sum(h,axis=1))
print(np.min(h,axis=0))
print(np.max(h,axis=1))




arr = [1,2,3,4,5,6]
#求均值
arr_mean = np.mean(arr)
#求方差
arr_var = np.var(arr)
#求标准差
arr_std = np.std(arr,ddof=1)
print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)