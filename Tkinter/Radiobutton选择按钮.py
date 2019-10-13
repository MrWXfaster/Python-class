#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-10-5 上午10:19
# @Author  : WX1995
# @Site    : 
# @File    : Radiobutton选择按钮.py
# @Software: PyCharm

import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("400x400")

var = tk.StringVar()
l = tk.Label(window,bg="yellow",width=20,text="empty")
l.pack()

def print_selection():
    l.config(text="you have selected" + var.get())


r1 = tk.Radiobutton(window, text="Option A",
                    variable=var, value="A",
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text="Option B",
                    variable=var, value="B",
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text="Option C",
                    variable=var, value="C",
                    command=print_selection)
r3.pack()

window.mainloop()
