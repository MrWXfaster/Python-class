# -*-coding: utf-8 -*-
__author__ = "WX"
'''
导入需要的包
'''
from PyQt5.Qt import *
import sys
'''
创建一个应用程序
'''
app = QApplication(sys.argv)
'''
控件操作： 创建控件 设置控件 添加子控件 其它
其中创建控件包括尺寸，位置，样式， 
'''
window = QWidget()
window.setWindowTitle("社会我顺哥，人狠话不多")
window.resize(500,500)
window.move(400,200)

label = QLabel(window)
label.setText("Hello Wx")
label.move(200,200)

window.show()

'''
开始执行应用程序，并进入消息循环
'''
sys.exit(app.exec_())