import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

T = np.arctan2(Y,X) # for color value
'''alpha代表透明度为50%，s代表大小，c代表颜色'''
# plt.scatter(X,Y,s=75,c=T,alpha=0.5)
plt.scatter(np.arange(5),np.arange(5))

# plt.xlim(-1.5,1.5)
# plt.ylim(-1.5,1.5)
'''隐藏x,y'''
plt.xticks(())
plt.yticks(())

plt.show()
