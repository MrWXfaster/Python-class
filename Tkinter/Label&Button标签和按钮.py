#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-10-4 下午5:53
# @Author  : WX1995
# @Site    : 
# @File    : Label&Button标签和按钮.py
# @Software: PyCharm
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("640x480")

var = tk.StringVar()
l = tk.Label(window,textvariable=var, bg = "green", font=("Arial",12), width=15,
             height=2)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text="hit me", width=15,
              height=2, command=hit_me)      #点击一下可以运行hit_me函数
b.pack()
window.mainloop()