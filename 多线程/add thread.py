#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : XH
#   File name   : add_thread.py
#   Author      : WrWx
#   Created date: 2019-07-22 16:45:45
#   Description :
#
#================================================================
import threading

def thread_job():
    print("This is an added Thread, number is %s"%threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job) #在添加一个线程
    added_thread.start()#开始添加的线程




if __name__ =="__main__":
    main()