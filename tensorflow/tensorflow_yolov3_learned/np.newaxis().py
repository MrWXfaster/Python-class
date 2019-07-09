'''
np.newaxis的一点理解

np.arange(0, 10)
这句话 生成的是一个一维的数组，如下：
[0 1 2 3 4 5 6 7 8 9]

输出其shape：(10,)
那么我如何才能将其转化为shape=(1,10)呢

可以用两种方法：
'''
#1.使用shape
import numpy as np
y=np.arange(1, 11)
y.shape=(10,1)
print(y)
'''
[[ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]]
'''

#2.使用np.newaxis

print(np.arange(0, 10)[:, np.newaxis])

'''
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
'''
#eg1
line = ['path','56,77,447,310,13']
# line1 = ['path','56,77,447,310,13','163,9,376,252,14']
strides = np.array([8,16,32])
bbox_xywh = [ 251.5,193.5,391,233]
strides = np.array([8,16,32])
print(strides)
bboxes = np.array([list(map(int, box.split(','))) for box in line[1:]])
bboxes = np.copy(bboxes)
for bbox in bboxes:
    bbox_coor = bbox[ :4]#[ 56  77 447 310]
    bbox_class_ind = bbox[4]

    onehot = np.zeros(20,dtype=np.float)
    onehot[bbox_class_ind] = 1
    uniform_distribution = np.full(20,1.0/20)
    deta = 0.01
    smooth_onehot = onehot * (1 - deta) + deta * uniform_distribution
    bbox_xywh = np.concatenate([(bbox_coor[2:] + bbox_coor[:2]) * 0.5, bbox_coor[2:] - bbox_coor[:2]], axis=0)
    print(bbox_xywh)
    bbox_xywh_scaled = 1.0 * bbox_xywh[np.newaxis, :] / strides[:, np.newaxis]
    print(bbox_xywh_scaled)

list = strides[:, np.newaxis]
print(list)
list1 =1*bbox_xywh[np.newaxis, :]
print(list1)
bbox_xywh_scaled = list1 / list
print(bbox_xywh_scaled)
