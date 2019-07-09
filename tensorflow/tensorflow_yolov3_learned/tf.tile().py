import tensorflow as tf
anchor_per_scale = 3
output_size = 52
batch_size = 52
y = tf.tile(tf.range(output_size, dtype=tf.int32)[:, tf.newaxis], [1, output_size])
x = tf.tile(tf.range(output_size, dtype=tf.int32)[tf.newaxis, :], [output_size, 1])
x1 = x[:, :, tf.newaxis]
y1 = y[:, :, tf.newaxis]
xy_grid = tf.concat([x[:, :, tf.newaxis], y[:, :, tf.newaxis]], axis=-1)
xy1 = xy_grid[tf.newaxis, :, :, tf.newaxis, :]
xy_grid = tf.tile(xy_grid[tf.newaxis, :, :, tf.newaxis, :], [batch_size, 1, 1, anchor_per_scale, 1])
# xy_grid = tf.cast(xy_grid,dtype = tf.float32)
# conv_raw_dxdy  = xy_grid[:, :, :, :,0:2]
# pred_xy = (tf.sigmoid(conv_raw_dxdy) + xy_grid) * stride
sess= tf.Session()
#y,x,x1,y1,
result = sess.run([xy1,xy_grid])

print(result)
'''
[array([[ 0,  0,  0, ...,  0,  0,  0],
       [ 1,  1,  1, ...,  1,  1,  1],
       [ 2,  2,  2, ...,  2,  2,  2],
       ..., 
       [49, 49, 49, ..., 49, 49, 49],
       [50, 50, 50, ..., 50, 50, 50],
       [51, 51, 51, ..., 51, 51, 51]], dtype=int32), array([[ 0,  1,  2, ..., 49, 50, 51],
       [ 0,  1,  2, ..., 49, 50, 51],
       [ 0,  1,  2, ..., 49, 50, 51],
       ..., 
       [ 0,  1,  2, ..., 49, 50, 51],
       [ 0,  1,  2, ..., 49, 50, 51],
       [ 0,  1,  2, ..., 49, 50, 51]], dtype=int32)]
'''
# x = tf.range(output_size)#52行
# z = x[:, tf.newaxis]#52列
# w= tf.tile(z,[1,output_size])
# print(x,z,w)
'''
tensorflow中的tile()函数是用来对张量(Tensor)进行扩展的，
其特点是对当前张量内的数据进行一定规则的复制。最终的输出张量维度不变。
tf.tile(
    input,
    multiples,
    name=None
)
'''
'''tf.tile()应用于需要张量扩展的场景，具体说来就是：
如果现有一个形状如[width, height]的张量，需要得到一个基于原张量的，
形状如[batch_size,width,height]的张量，其中每一个batch的内容都和原张量一模一样。tf.tile使用方法如： 
'''
'''可见，multi重复了raw的0 axes两次，1和2 axes不变'''
import tensorflow as tf

raw = tf.Variable(tf.random_normal(shape=(2, 3, 2)))
multi = tf.tile(raw, multiples=[1, 2, 2])

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(raw.eval())
    print('-----------------------------')
    print(sess.run(multi))

i= int(0/3)
print(i)
import numpy as np
strides1 = [8, 16, 32]
stides = np.array(strides1)
result = stides[:,np.newaxis]
print(np.shape(stides),'\n',np.shape(result))