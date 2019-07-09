import matplotlib.pyplot as plt
import numpy as np
'''产生50数据点，-1～1,'''
x = np.linspace(-1,1,50)
# y = 2*x + 1
y = x**2
'''1,将x,y,plot出来 2,显示出来'''
plt.plot(x,y)
plt.show()