#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : XH
#   File name   : jion.py
#   Author      : WrWx
#   Created date: 2019-07-22 16:45:45
#   Description :
#
#================================================================
import threading
import time

def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

def main():
    added_thread = threading.Thread(target=thread_job,name="T1")
    thread2 = threading.Thread(target=T2_job,name="T2")
    added_thread.start()
    thread2.start()
    thread2.join()#将线程添加到主列表中并且执行完后再返回
    added_thread.join()
    print("all done\n")





if __name__ =="__main__":
    main()