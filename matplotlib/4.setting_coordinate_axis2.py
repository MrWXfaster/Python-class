
import matplotlib.pyplot as plt
import numpy as np

'''改变坐标轴的位置'''
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
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

#gca = get current axis

ax = plt.gca()
'''ax.spines表示为设置脊梁，即四个边框'''
ax.spines["right"].set_color('none')
ax.spines["top"].set_color('none')
'''设置底侧的边框为x轴，左边的边框为y轴'''
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
'''固定x：把x轴设置在y轴为-1的位置上'''
ax.spines['bottom'].set_position(('data',0))#outward, axes#百分之多少的位置
'''固定y：把y轴设置在x轴为-1的位置上'''
ax.spines['left'].set_position(("data",0))
plt.show()