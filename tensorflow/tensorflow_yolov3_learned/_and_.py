#1、单斜杠（/）表示除法，且不管除数和被除数是不是整数，最后结果都是float类型。

a = 3/1
print(a)

b = 3.2/2
print(b,type(b))

#2、双斜杠（//）表示地板除，即先做除法（/），然后向下取整（floor）。
# 至少有一方是float型时，结果为float型；两个数都是int型时，结果为int型。

c = 3//2
print(c,type(c))

d = 3.2//2
print(d,type(d))

#另外，地板除 floor(x) 表示不大于x的最大整数，因此不是取整数部分，如 x 为负数时：
import math
e = math.floor(1.6)
print(e,type(e))

f  = math.floor(-1.6)
print(f,type(f))


