#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-10-5 上午11:30
# @Author  : WX1995
# @Site    : 
# @File    : Canvas.py
# @Software: PyCharm

import tkinter as tk

window= tk.Tk()
window.title()
window.geometry("1280x720")

canvas = tk.Canvas(window,bg="blue", height=400, width=400)
image_file = tk.PhotoImage(file="timg.gif")
image = canvas.create_image(0, 0, anchor="center", image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill = "red")
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30,start=0,extent=180)
rect=canvas.create_rectangle(100,30,100+20, 30+20)

canvas.pack()

def moveit():
    canvas.move(rect,0,2)

b = tk.Button(window, text="move", command=moveit).pack()

window.mainloop()