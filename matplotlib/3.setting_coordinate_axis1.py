import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2


plt.figure(num=1)#默认第二张图片
plt.plot(x,y1,color="red",linewidth=1.0,linestyle='--')
plt.plot(x,y2)
plt.xlim((-1,2))
plt.ylim((-2,3))

new_ticks = np.linspace(-1,2,5)
print(new_ticks)

'''对x的刻度重新进行排布使用new_ticks'''
plt.xticks(new_ticks)
'''对y轴 刻度与标签改为相应位置的标识，并且转化为优美的文字，\表示转字符，同时也能转数学符号如alpha，
$表示转化为数学形式的字体，r为正则表达的一种形式，显示中文在最后加上fontproperties="FangSong,就可以显示仿宋字体"'''
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])

''''对x，y轴描述;'''
plt.xlabel("I am x")
plt.ylabel("I am y")

plt.show()