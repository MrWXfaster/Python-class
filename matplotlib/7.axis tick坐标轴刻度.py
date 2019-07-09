
import matplotlib.pyplot as plt
import numpy as np

'''改变坐标轴的位置'''
x = np.linspace(-3,3,50)
y1 = 2*x + 1



plt.figure(num=1,figsize=(8,5))#默认第二张图片
plt.plot(x,y1,)

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

'''本次课改变的东西'''

for label in ax.get_xticklabels() + ax.get_yticklables():
    label.set_fontsize(12)
    '''0.7'''
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))


plt.show()