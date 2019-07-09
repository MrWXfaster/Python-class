'''
使用类实现__iter__()和next()函数

另一个创建迭代器的方法是使用类，一个实现了__iter__()和next()方法的类可以作为迭代器使用。
next方法：返回迭代器的下一个元素
__iter__方法：返回迭代器对象本身
'''

#! /usr/bin/env python
#coding=utf-8

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

if __name__ == '__main__':
    for n in Fib():
        print(n)