import matplotlib.pyplot as plt
'''第二种方法plot出小格子的办法'''
import matplotlib.gridspec as gridspec

#method 1: subplot 2 grid

plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)#3,3代表了把figure划分为多少个格子
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)#colspan 代表跨了横2格
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)#rowspan代表跨了竖2格子
ax4 = plt.subplot2grid((3,3),(2,0))
ax5 = plt.subplot2grid((3,3),(2,1),)
#method2: gridspec
'''索引的方法'''
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])

#method3: easy to define structure

f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])


plt.tight_layout()
plt.show()

