#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-9-17 下午7:29
# @Author  : WX1995
# @Site    : 
# @File    : 继承结构图.py
# @Software: PyCharm

from PyQt5.Qt import *

#print(QObject.__subclasses__())
#print(QWidget.__subclasses__())
#print(QAbstractButton.__subclasses__())

def getSubClasses(cls):
    for subcls in cls.__subclasses__():
        print(subcls)
        if len(cls.__subclasses__()) > 0:
            getSubClasses(subcls)

getSubClasses(QObject)