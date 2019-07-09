'''
tf.layer.conv2d.transpose(input,filter,kernel_size,strides,padding)
以上是比较关注的参数，

inputs: 输入的张量
filters: 输出卷积核的数量
kernel_size : 在卷积操作中卷积核的大小
strides: （不太理解，我直接理解成放大的倍数）
padding : ‘valid’ 或者 ‘same’。
'''
import tensorflow as tf
import numpy as np

a = np.array([[1,1],[2,2]], dtype=np.float32)
# [[1,1],
#  [2,2]]

# tf.layers.conv2d_transpose 要求输入是4维的
a = np.reshape(a, [1,2,2,1])

# 定义输入
x = tf.constant(a,dtype=tf.float32)
# 进行tf.layers.conv2d_transpose
upsample_x = tf.layers.conv2d_transpose(x, 1, 3, strides=2, padding='same', kernel_initializer=tf.ones_initializer())
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(upsample_x))
    # [[[[1],[1],[2],[1]],
    #   [[1],[1],[2],[1]],
    #   [[3],[3],[6],[3]],
    #   [[2],[2],[4],[2]]]]