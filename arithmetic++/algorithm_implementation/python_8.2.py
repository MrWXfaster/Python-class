# 例8.2 枚举算法案例分析

# 例8-7 输出由1,2,3,4这四个数字组成的每位上的数字都不相同的所有三位数

#解析：标准库itertool提供了一个排列函数permutations（）可以用来返回从n个元素中任选i个元素组成
# 的所有排列，把这些排列转化为数字输出即可

from itertools import permutations

def demo(digits, num):
    for item in permutations(digits,num):
        print(int(''.join(map(str,item))),end=',')

demo((1,2,3,4),3)

# 例8-8 编写函数，接受一个正偶数为参数，输出两个素数，并且这两个素数之和等于原来正偶数。如果存在多
# 组符合条件的素数，则全部输出

# 解析： 首先编写一个函数IsPrime()来判断一个数是否为素数，然后再编写一个函数demo()来把给定数字n
# 拆分两个数字的和，调用IsPrime（）函数判断这两个数字是否都是素数，如果是则输出这两个数

def Isprime(p):
    if p ==2:              #2是素数，直接返回
        return True
    if p % 2 ==0:
        return False       #除2以外的其他偶数都不是素数，直接返回
    for i in range(3,int(p**0.5)+1,2): #判断从3到p的平方根之内有没有p的因数
        if p%i == 0:
            return False    #有因数，p不是素数
    return True             #没有因数，p是素数
def demo(n):                #主函数
    if isinstance(n,int) and n>0 and n%2==0:#isinstance是Python中的一个内建函数。是用来判断一个对象的变量类型
        for i in range(2,n//2+1):
            if Isprime(i) and Isprime(n-i):
                print('\n',i,'+','=',n )

demo(30)

# 例8-9 编写程序，输出所有的3位水仙花数
# 解析：所谓水仙花数是指1个n位十进制数，其各位数字的立方和恰好等于该数本身。
# 例如：153是水仙花数，因为153 = 1 + 5 + 3 的各立方和

for i in range(100,1000):#遍历所有的三位数
    bai,shi,ge = map(int,str(i))
    if ge**3+shi**3+bai**3 == i:
        print(i)

# 8-10 编写程序寻找指定数的黑洞数
# 解析：黑洞数是指：有这个数字每位上组成的最大数减去每位上组成的最小数，仍然是该数本身。例如：3位黑洞数495
# 954-459 = 459

def main(n):
    '''参数n表示数字的位数，例如n=3时返回495,n=4时返回6174'''
    # 带测试数范围的起点和结束值
    start = 10**(n-1)
    end = 10**n
    # 依次测试每个数
    for i in range(start,end):
        #由这几个数字组成的最大数和最小数
        big = ''.join(sorted(str(i),reverse=True))
        little = ''.join(reversed(big))
        big,little = map(int,(big,little))
        if big - little == i:
            print(i)

main(4)