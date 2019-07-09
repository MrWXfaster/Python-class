import numpy as np
from sklearn.datasets import load_sample_image
from sklearn.cluster import KMeans, MiniBatchKMeans
from PIL import Image
import matplotlib.pyplot as plt

#读取原始图片数据，并转换为三维矩阵
path = './my_tensorflow_yolov3/data/images/test1.jpeg'
imOrigin = Image.open(path)
plt.imshow(imOrigin)
plt.show()
dataOrigin = np.array(imOrigin)
#生成二维数组
data = dataOrigin.reshape(-1,3)

#使用Kmeans算法把所有像素点化分为四类

kmeansPredicter = MiniBatchKMeans(n_clusters =12, batch_size=20000)
kmeansPredicter.fit(data)

#使用每个像素所属类的中心值替换该像素的颜色

temp = kmeansPredicter.predict(data)
dataNew = kmeansPredicter.cluster_centers_[temp]
dataNew.shape = dataOrigin.shape
plt.imshow(dataNew)
plt.imsave('result1.jpeg',dataNew)
plt.show()


