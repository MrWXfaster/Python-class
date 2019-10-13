#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-9-16 下午7:47
# @Author  : WX1995
# @Site    : 
# @File    : Menu.py
# @Software: PyCharm

from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qlabel的学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("xxx")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())