APPLE = 100
a = None
def fun():
    global a
    a = 20

    print(a)
    return a + 100

print(APPLE)
print('a past=',a)
print(fun())
print('a now=', a)
'''
全局变量是在函数之外的
局部变量是在函数之内的
想要把全局变量定义到里面，需要在函数中定义global a,调用函数之后会将局部变量转化为全局变量
'''