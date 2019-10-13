#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-10-9 下午1:02
# @Author  : WX1995
# @Site    : 
# @File    : pythonlove.py
# @Software: PyCharm

import time

[(time.sleep(0.0009), print("\033[91m"+i,end="", flush=True)) for i in ('\n'.join([''.join([(" I love U"[(x-y)%9]if((x*0.05)**2 + (y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15, -15,-1)]))]