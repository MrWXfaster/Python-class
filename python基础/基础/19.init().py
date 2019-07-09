class Calculator:

    def __init__(self,name,price,height,width,weight):#定义类的特有属性，调用时必须传入固有参数，默认参数，可以更改
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight#前几个是属性
        self.add(1,3)#这个是功能，会直接执行
    def add(self,x,y):#self代表在类里面默认的一个参数  #定义类的函数功能
        # print(self.name)
        result = x+y
        print(result)

    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
# c = Calculator()
# print(c)#报错，必须输入5类的属性参数
d = Calculator("Bad calculator",12,30,15,19,)
print(d.height)
print(d.weight)

