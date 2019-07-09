
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
x0 = 1
y0 = 2*x0 + 1
'''展示该点,s代表点的大小'''
plt.scatter(x0,y0,s=50,color='b')
'''展示一条直线，即将两个点连接起来,k--表示黑色的虚线，lw为线宽'''
plt.plot([x0,x0],[0,y0],'k--',lw=2.5)

#method 1
#############
'''xytext表示基于某个点的位置；xy表示基于的点的坐标，textcoods表示基于这个点，fontsize代表字体的大小，arrowprops代表箭头的形状，以及弧度
arrowstyle代表最后的箭头的形状，connectionstyle表示为连接的弧度以及长度的一些参数'''
plt.annotate(r"$2x+1=%s$"%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords = "offset points",
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))

#method 2
#############
'''3.7 3代表开始的坐标，fontdict:表示字体的一些属性，像尺寸和颜色'''
plt.text(-3.7,3,r"$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$",
         fontdict={'size':16,'color':'red'})
plt.show()