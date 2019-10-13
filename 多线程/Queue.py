#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : XH
#   File name   : Queue.py
#   Author      : WrWx
#   Created date: 2019-07-22 16:44:45
#   Description :
#
#================================================================
import threading
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for threads in threads:
        threads.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__=="__main__":
    multithreading()