#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-10-5 上午10:35
# @Author  : WX1995
# @Site    : 
# @File    : Scale尺度.py
# @Software: PyCharm

import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("400x400")

l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()

def print_selection(v):
    l.config(text='you have selected' + v)

s = tk.Scale(window, label="trr me", from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()