'''
tf.device()

指定tensorflow 运行的GPU或CPU设备
'''
#设置GPU

'''
使用 tf.device('/gpu:1') 指定Session在第二块GPU上运行：
ConfigProto() 中参数 log_device_placement=True  会打印出执行操作所用的设备，以上输出：
'''
#
import tensorflow as tf

with tf.device('/gpu:0'):
    v1 = tf.constant(1, name ='v1')
    v2 = tf.constant(2, name ='v2')
    sumV12 = v1 + v2

with tf.Session() as sess:
    result0= sess.run(sumV12)
    print(result0)

#设置CPU

'''
使用tf.device('/cpu:0')
tensorflow中不同的GPU使用/gpu:0和/gpu:1区分，而CPU不区分设备号，统一使用 /cpu:0
'''

with tf.device('/cpu:0'):
    v3 = tf.constant(1,name='v3')
    v4 = tf.constant(2, name='v4')
    SumV1 = v3+v4
with tf.Session() as sess:
    result1 = sess.run(SumV1)
    print(result1)
