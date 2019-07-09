import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()#窗口
ax = Axes3D(fig)#在窗口上加了一个3D的轴

'''X,Y value'''
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)#把X,Y放置的到底面上去
R = np.sqrt(X**2 + Y**2)#计算X,Y的值，为高度值

#height value
Z = np.sin(R)
'''设置整个3D图的表面，颜色为rainbow,rstride代表在x轴上化分多少网格，cstride表示为在y轴上把颜色分为多少半'''

ax.plot_surface(X,Y,Z,rstride=20,cstride=2,cmap="rainbow")
#将这个三维图压缩到zdir="z"轴上，偏移-2,即offset为-2,cmap为颜色的类型，这次定义为rainbow
ax.contourf(X,Y,Z,zdir="x",offset=-4,cmap='rainbow')
'''将z轴限定在-2到2之间'''
ax.set_zlim(-2,2)


plt.show()