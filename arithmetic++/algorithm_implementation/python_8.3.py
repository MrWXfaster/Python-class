#8.3 递推算法案例分析
#例8-12 使用递推法计算阶乘
# 解析：根据阶乘的定义式编写代码

def fac(n):
    result = 1
    for i in range(1,n+1):
        # result*=i
        result = result*i
    return result

print(fac(6))

# 例8-13 使用递推法计算组合数
# 解析：

def Cni2(n,i):
    if not (isinstance(n,int) and isinstance(i,int) and n>=i):
        print('n和i必须是数字，并且n>=i')
        return 1

    result = 1
    Min,Max = sorted((i,n-i))
    for i in range(n,0,-1):
        if i>Max:
            result*=i
        elif i <=Min:
            result//=i
    return result
print(Cni2(6,2))
