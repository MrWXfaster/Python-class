import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()#相当于默认第一个图片
plt.plot(x,y1)#一个图片上画东西

plt.figure(num =3,figsize=(8,5))#默认第二张图片
plt.plot(x,y1,color="red",linewidth=1.0,linestyle='--')
plt.plot(x,y2)

plt.show()


'''
)figure语法说明

figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)

    num:图像编号或名称，数字为编号 ，字符串为名称
    figsize:指定figure的宽和高，单位为英寸；
    dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张 
    facecolor:背景颜色
    edgecolor:边框颜色
    frameon:是否显示边框

'''