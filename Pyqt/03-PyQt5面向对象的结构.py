#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-9-16 下午7:30
# @Author  : WX1995
# @Site    : 
# @File    : 03-PyQt5面向对象的结构.py
# @Software: PyCharm


# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys
from Menu import *


#1.创建一个应用程序对象,获取参数
app = QApplication(sys.argv)

#2. 控件的操作
#2.1 创建控件
window =Window()

# #2.2 设置控件
# window.setWindowTitle("")
# window.resize(500,500)
#
#
#2.3 展示控件
window.show()
#
#3.应用程序的执行，进入到消息循环
sys.exit(app.exec())
