'''
tf.reduce_max函数的作用：计算张量的各个维度上的元素的最大值。例子:
'''
import tensorflow as tf

max_value = tf.reduce_max([1, 3, 2], axis = 0)
with tf.Session() as sess:
    max_value = sess.run(max_value)
    print(max_value)

'''
2、tf.sequence_mask的作用是构建序列长度的mask标志 。 例子：
'''
import tensorflow as tf
mask = tf.sequence_mask([1, 3, 2], 5)
with tf.Session() as sess:
    mask = sess.run(mask)
    print(mask)

'''
3、两个函数结合使用：

  # 根据目标序列长度，选出其中最大值，然后使用该值构建序列长度的mask标志，代码：
'''
import tensorflow as tf
max_value = tf.reduce_max([1, 3, 2])
mask = tf.sequence_mask([1, 3, 2], max_value)
with tf.Session() as sess:
    mask = sess.run(mask)
    print(mask)
'''
tf.argmax(values,axis):返回values在axis维度最大值的索引

tf. reduce_max(values,axis):返回values在axis维度的最大值

结果维度为values的维度-1，且shape为去掉axis之后的values的shape,顺序不变。
'''
import tensorflow as tf

d = [[[1, 200], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]] # d.shape = (2,3,2) 三维
idx = tf.argmax(d, axis=0)
val = tf.reduce_max(d, axis=0)

with tf.Session() as sess:
    print(idx.eval())  # shape = (3,2) 二维
    print(val.eval())

idx = tf.argmax(d, axis=-1)
val = tf.reduce_max(d, axis=-1)

with tf.Session() as sess:
    print(idx.eval())  # shape = (2,2)
    print(val.eval())