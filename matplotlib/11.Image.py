import matplotlib.pyplot as plt
import numpy as np

#image data
a = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)

'''
for the value of "interpolation",check this:
http://matplotlib.org/examples/image_contours_and_fields/interpolation_method.html
'''
'''interpolation表示为网格的类型，origin表示为像素点的顺序lower or upper'''

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
'''添加颜色柱,shrink压缩了0.9'''
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()