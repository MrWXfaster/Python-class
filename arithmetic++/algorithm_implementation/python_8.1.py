# 例子8-1根据定义计算组合数
# 解析：组合数公式
import math
import numpy as np
def Cnil(n,i):
    return int(math.factorial(n)/math.factorial(i)/math.factorial(n-i))
print(Cnil(10,2))


#例8-2编写程序，计算一元二次方程的根

def root(a,b,c,highmiddle=True):
    #首先保证接收的参数a,b,c都是数字，并且a不等于0
    #由于计算机表示实数存在精度问题，故不能使用==0来判断实数是否为0
    # 函数的最后一个参数highmiddle为True表示高中,False表示初中
    if not isinstance(a,(int,float,complex))or abs(a)<1e-6:
        print('error')
        return
    if not isinstance(b,(int,float,complex)):
        print('error')
        return
    if not isinstance(c,(int,float,complex)):
        print('error')
        return
    #delta<0时无解
    d =b**2 - 4*a*c
    # 根据一元二次方程求根公式进行计算
    #当d<0时，在实数域内无解，d**0.5会得到复数
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)

    if isinstance(x1,complex):
        if highmiddle:
            #高中阶段需要考虑复数根，实部和虚部都保留3位小数
            x1 = np.round(x1.real,3) + np.round(x1.imag,3)*1j
            x2 = np.round(x2.real,3) + np.round(x2.imag,3)*1j
        else:
            #初中阶段只考虑实数根
            return "no answer"

    #如果是实数根，保留三位小数
    return(np.round(x1,3),np.round(x2,3))
r = root(1,2,4)
if isinstance(r,tuple):
    print("x1={0[0]}\nx2={0[1]}".format(r))

# 例 8-3 并联电路的电阻计算

def compute(lst):
    r = sum(map(lambda x:1/x,lst))
    return np.round(1/r,3)

print(compute([50,30,20]))

# 例子8-4 根据公式计算圆的面积

from math import pi as pi

def circleArea(r):
    if isinstance(r,(int,float)):    #确保接收的参数为数值
        return pi*r*r
    else:
        return "半径必须是数字"
r = 4
s = circleArea(r)
print("园半径为 %d 面积为 %d"%(r, s))

# 例子8-5 已知三角两个边长和夹角角度，计算第三边长
# 解析：根据余弦定理来编写程序，其中余弦可以使用标准库math提供函数cos()来计算，不过cos()函数接受的参数
# 是弧度而不是角度，所有需要先对参数进行一些转化。

from math import cos,pi

def thirdLength(a,b,C):
    C = C/180*pi
    return(a**2+b**2-2*a*b*cos(C))**0.5

print("已知三角形三边中，a=3,b=4,C(cos) = 90度，则另一边c=%d"%(thirdLength(3,4,90)))