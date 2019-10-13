class Calculator:
    name = "Good calculator"#定义类的属性
    price = 18
    def add(self,x,y):#self代表在类里面默认的一个参数 #定义类的函数功能
        print(self.name)
        result = x+y
        print(result)

    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
calcul = Calculator()
print(calcul.name)
print(calcul.price)
print(calcul.add(10,20))