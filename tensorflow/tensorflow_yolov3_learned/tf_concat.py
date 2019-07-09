import tensorflow as tf
'''
tensorflow中用来拼接张量的函数tf.concat()，用法:
tf.concat([tensor1, tensor2, tensor3,...], axis)

axis=0     代表在第0个维度拼接

axis=1     代表在第1个维度拼接 
对于一个二维矩阵，第0个维度代表最外层方括号所框下的子集，第1个维度代表内部方括号所框下的子集。维度越高，括号越小
注意：tf.concat()拼接的张量只会改变一个维度，其他维度是保存不变的。

对于axis等于负数的情况

axis=-1    表示倒数第一个维度
对于三维矩阵拼接来说，axis=-1等价于axis=2。
同理，axis=-2代表倒数第二个维度，对于三维矩阵拼接来说，axis=-2等价于axis=1。
'''
#eg1

t1 = [[1, 2, 3], [4, 5, 6]]
t2 = [[7, 8, 9], [10, 11, 12]]
a = tf.concat([t1, t2], 0)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
b = tf.concat([t1, t2], 1)  # [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]]

# tensor t3 with shape [2, 3]
# tensor t4 with shape [2, 3]
# tf.shape(tf.concat([t3, t4], 0))  # [4, 3]
# tf.shape(tf.concat([t3, t4], 1))  # [2, 6]
print(a,b)
