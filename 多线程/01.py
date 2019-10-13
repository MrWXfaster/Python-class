#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : XH
#   File name   : config.py
#   Author      : WrWx
#   Created date: 2019-07-22 16:43:45
#   Description :
#
#================================================================
'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

import time

def loop1():
    #ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    time.sleep(4)
    print("End loop 2 at:", time.ctime())

def loop2():
    #ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def loop3():
    #ctime 得到当前时间
    print('Start at :', time.ctime())
    loop1()
    loop2()
    print("All done at:", time.ctime())

if __name__=="__main__":
    loop3()
