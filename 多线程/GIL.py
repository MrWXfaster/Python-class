#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : XH
#   File name   : GIL.py
#   Author      : WrWx
#   Created date: 2019-07-22 16:44:45
#   Description :
#
#================================================================
import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)#代替return的作用

def multithreading(l):
    q = Queue()
    threads = []#多线程的列表，共添加了四个线程
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start() #开始线程
        threads.append(t) #将每个线程添加到列表当中
    [t.join() for t in threads] #将线程插入列表当中
    total = 0
    for _ in range(4):
        total += q.get()#执行了求和的任务
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)