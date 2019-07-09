import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    #the height function
    return (1 - x/2 + x**5 + y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
'''X,Y的网格'''
X,Y  =np.meshgrid(x,y)

#use plt.contourf to filling contours
#X,Y and value for (X,Y) point
'''contourf(x,y z),alpha表示透明度，cmap =每个点的颜色
第一个8是填充八个颜色，第二个八是八条等高线图
'''

plt.contourf(X,Y,f(X,Y),8,alpha = 0.75,cmap=plt.cm.hot)

#use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,color="black",linewidth=5)

#adding label
plt.clabel(C,inline=False,fontsize=10)


plt.xticks(())
plt.yticks(())
plt.show()