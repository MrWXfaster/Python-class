'''
tf.cast(
    x,
    dtype,
    name=None）
将x的数据格式转化成dtype数据类型.例如，原来x的数据格式是bool，
那么将其转化成float以后，就能够将其转化成0和1的序列。反之也可以
'''

import sys
import tensorflow as tf
print(sys.version)

a = tf.Variable([1.0,1.3,2.1,3.41,4.51])
b = tf.cast(a>3,dtype=tf.bool)
c = tf.cast(a>3,dtype=tf.int8)
e = tf.cast(a<2,dtype=tf.float32)
d = tf.cast(a,dtype=tf.int8)

sess = tf.Session()
sess.run(tf.initialize_all_variables())
print(sess.run(b))
print(sess.run(c))
print(sess.run(e))
print(sess.run(d))