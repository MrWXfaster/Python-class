#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-10-5 上午9:37
# @Author  : WX1995
# @Site    : 
# @File    : Entry&Text输入，文本框.py
# @Software: PyCharm

import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("640x480")
e = tk.Entry(window,show="***")
e.pack()


def insert_point():
    var = e.get()
    t.insert("insert", var)

def insert_end():
    var = e.get()
    t.insert("end",var)

b1 = tk.Button(window, text="insert point",width=15,
              height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end",width=15,
              height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()  #让界面完全显示出来