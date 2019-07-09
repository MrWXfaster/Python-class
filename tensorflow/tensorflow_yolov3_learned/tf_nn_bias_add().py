
'''
tf.nn.bias_add(value,bias,name=None)
解释：这个函数就是将偏差项bias添加value,上面
这个操作可以看成tf.add()操作的一个特例，其中bias必须是一维的，
'''

'''
eg1
'''
import tensorflow as tf

a = tf.constant([[1,2],
                 [1,4],
                 [4,6]],dtype=tf.float32)
b = tf.constant([1,2],dtype=tf.float32)
c = tf.constant(1,dtype = tf.float32)

with tf.Session() as sess:
    print("bias_add")
    print(sess.run(tf.nn.bias_add(a,b)))
    # print(sess.run(tf.nn.bias_add(a,c))) #报错

'''
对比tf.add(x,y,name = None)
通俗解释：
这个情况比较多，最常见的是，一个叫x的矩阵和一个叫y的数相加，
就是y分别与x的每个数相加，得到的结果和x大小相同。
'''

import tensorflow as tf

x = tf.constant([[1,2],
                 [1,2]])
y = tf.constant([[1,2],
                 [1,1]])
z = tf.add(x,y)

x1 = tf.constant(1)
y1 = tf.constant(2)
z1 = tf.add(x1, y1)

x2 = tf.constant(2)
y2 = tf.constant([1, 2])
z2 = tf.add(x2, y2)

x3 = tf.constant([[1, 2],
                  [3, 4]])
y3 = tf.constant([[1, 1]])
z3 = tf.add(x3, y3)

with tf.Session() as sess:
    z_result, z1_result, z2_result, z3_result = sess.run([z, z1, z2, z3])
    print('z =\n%s' % (z_result))
    print('z1 =%s' % (z1_result))
    print('z2 =%s' % (z2_result))
    print('z3 =%s' % (z3_result))