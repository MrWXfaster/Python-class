import matplotlib.pyplot as plt

plt.figure()

'''
plt.subplot(2,2)把一张figure分为2行2列的格子，最后一个1代表是第一个plot
plt.plot(x,y)代表plot出x,y的坐标范围
'''
plt.subplot(2,1,1)#第二个1代表这个plot代表1行
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,3])
#
plt.subplot(2,3,6)
plt.plot([0,1],[0,4])
plt.show()