'''
用法：zeros(shape, dtype=float, order='C')
返回：返回来一个给定形状和类型的用0填充的数组；
参数：shape:形状
dtype:数据类型，可选参数，默认numpy.float64
dtype类型：t ,位域,如t4代表4位
b,布尔值，true or false
i,整数,如i8(64位）
u,无符号整数，u8(64位）
f,浮点数，f8（64位）
c,浮点负数，
o,对象，
s,a，字符串，s24
u,unicode,u24
order:可选参数，c代表与c语言类似，行优先；F代表列优先
'''

#ex1

import numpy as np

list1 = np.zeros((1,2))
# print(list1)
#output
'''[[ 0.  0.]]'''

list2 = np.zeros((2,2))
# print(list2)
#output
'''
  [[ 0.  0.]
   [ 0.  0.]]
'''
list3 = np.zeros((2,4,4,3))
# print(list3)
#output
'''
  [[[ 0.  0.  0.] 
   [ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]]

  [[ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]]

  [[ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]]

  [[ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]
   [ 0.  0.  0.]]]]
'''
list = np.zeros((150,4))
# print(list)
# list1 = np.zeros((3,4))
# print(list1)
# bboxes_count= np.zeros((3,))
# print(bboxes_count)
# bboxes_count[1] +=1
# print(bboxes_count)
# iou =[[ 0.0913252 ,  0.32417744,  0.53319869]]
# print(np.array(iou).reshape(-1))
# best_anchor_ind = np.argmax(np.array(iou).reshape(-1), axis=-1)
# print(best_anchor_ind)

max_bbox_per_scale = 150
anchor_per_scale = 3
bbox_xywh = np.array([ 251.5, 193.5, 391,   233. ])
strides = np.array([8, 16, 32])
bbox_xywh_scaled = 1.0 * bbox_xywh[np.newaxis, :] / strides[:, np.newaxis]

# bbox_count =np.zeros((3,))
# bbox_xywh = [ 251.5,193.5,  391, 233]
#
# bboxes_xywh = [np.zeros((max_bbox_per_scale, 4)) for _ in range(3)]
# bbox_ind = int(bbox_count[i] % max_bbox_per_scale)  # 0
# bboxes_xywh[i][bbox_ind, :4] = bbox_xywh  #
iou = [[ 0.0913252 ,  0.32417744,  0.53319869]]

best_anchor_ind = np.argmax(np.array(iou).reshape(-1), axis=-1)#最好的框的索引：reshpe(-1)作用是减少一个维度  返回：2即最好的框是第三个框；
best_detect = int(best_anchor_ind / anchor_per_scale) # 2 / 3 #最好的探测
best_anchor = int(best_anchor_ind % anchor_per_scale) # 0
xind, yind = np.floor(bbox_xywh_scaled[best_detect, 0:2]).astype(np.int32)
print(xind,yind)