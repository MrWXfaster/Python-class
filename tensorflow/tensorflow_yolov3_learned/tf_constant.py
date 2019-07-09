import tensorflow as tf
'''
tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const',
    verify_shape=False
)
'''

'''
可以看到第一个值value是必须的，可以是一个数值，也可以是一个列表。
如果是数值：
为查看结果必须创建一个会话，并用取值函数eval()来查看创建的tensor的值：
'''
tensor = tf.constant(1)
with tf.Session() as sess:
    print("结果是:",tensor.eval())
'''
如果value为列表
'''
tensor = tf.constant([1,2])
with tf.Session() as sess:
    print('结果是:',tensor.eval())
'''
后面四个参数可写可不写，第二个参数表示数据类型，一般可以是tf.float32, tf.float64等：
'''
tensor = tf.constant([1,2],dtype=tf.float32)
with tf.Session() as sess:
    print("结果是:",tensor.eval())

'''
第三个参数表示张量的“形状”，即维数以及每一维的大小。如果指定了第三个参数，
当第一个参数value是数字时，张量的所有元素都会用该数字填充：
可以看到是一个二维张量，第一维大小为2， 第二维大小为3，全用数字-1填充。

而当第一个参数value是一个列表时，
注意列表的长度必须小于等于第三个参数shape的大小（即各维大小的乘积）.

而如果列表大小小于shape大小，则会用列表的最后一项元素填充剩余的张量元素：
'''
tensor = tf.constant(1,shape=[2,3])
with tf.Session() as sess:
    print('result:',tensor.eval())

tensor = tf.constant([2,1],shape=[4,4])
with tf.Session() as sess:
    print("result:",tensor.eval())

'''
第四个参数name可以是任何内容，主要是字符串就行。
'''
tensor=tf.constant([1, 2])
print(tensor)
tensor=tf.constant([1, 2],name='wx')
print(tensor)

'''
第五个参数verify_shape默认为False，如果修改为True的话表示检查value的形状与shape是否相符，如果不符会报错。
'''
tensor = tf.constant([[1,2,3],
                      [4,5,6]],shape=[2,3],verify_shape=True)
print(tensor)


tensor = tf.constant([[0,0],[2,3],[2,3],[0,0]],shape=[4,2], verify_shape=True)
print(tensor)