#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : XH
#   File name   : lock_
#   Author      : WrWx
#   Created date: 2019-07-21 16:21:45
#   Description :
#
#================================================================
import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        print("job1",A)
    lock.release()#锁住一个线程，当一个线程结束后再执行后一个线程

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 10
        print("job2", A)
    lock.release()


if __name__ =="__main__":
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
