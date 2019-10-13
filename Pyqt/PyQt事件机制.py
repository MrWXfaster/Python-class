#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-9-19 下午7:28
# @Author  : WX1995
# @Site    : 
# @File    : PyQt事件机制.py
# @Software: PyCharm

import sys
from PyQt5.Qt import *

class App(QApplication):

    def notify(self,receiver,evt):
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver,evt)

        return super().notify(receiver,evt)

class Btn(QPushButton):
    def enevt(self,evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().enevt(evt)

    def mousePressEvent(self, *args, **kwargs):
        print("鼠标被按下........")


app = App(sys.argv)

window = QWidget()

btn = QPushButton(window)
btn.setText("按钮")
btn.move(100,100)

def cao():
    print("xxxxx")
btn.pressed.connect(cao)
window.show()

sys.exit(app.exec_())