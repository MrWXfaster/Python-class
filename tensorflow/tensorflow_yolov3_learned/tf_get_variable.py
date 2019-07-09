'''
获取一个已经存在的变量或者创建一个新的变量
tf.get_variable(name, shape = None, dtype = tf.float32,
                initializer = None, trainable = True, collection = None)

name ： 新变量或现有变量的名称.
shape : 新变量或现有变量的形状.
dtype：新变量或现有变量的类型.default = tf.float32
initializer : 如果创建了则用它来初始化变量.
trainable : 如果为True，则会默认将变量添加到图形集合GraphKeys.TRAINABLE_VARIABLES中。
            此集合用于优化器Optimizer类优化的的默认变量列表【可为optimizer指定其他的变量集合】，可
            就是要训练的变量列表。
collection: 要将变量添加到的图表集合列表个图graph集合列表的关键字。新变量将添加到这个集合中。
            默认为[GraphKeys.GLOBAL_VARIABLES]。也可自己指定其他的集合列表；.
'''

'''
变量初始化的方式
tf.constant_initializer：常量初始化函数
tf.random_normal_initializer：正态分布
tf.truncated_normal_initializer：截取的正态分布
tf.random_uniform_initializer：均匀分布
tf.zeros_initializer：全部是0
tf.ones_initializer：全是1
tf.uniform_unit_scaling_initializer：满足均匀分布，但不影响输出数量级的随机值
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

a1 = tf.get_variable(name='a1',shape = [2,3], dtype=tf.float32,initializer=tf.random_normal_initializer(mean=0,stddev=1))
a2 = tf.get_variable(name='a2',shape = [1], dtype=tf.float32,initializer=tf.constant_initializer(1))
a3 = tf.get_variable(name='a3',shape = [2,3],dtype=tf.float32,initializer=tf.ones_initializer())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run([a1,a2,a3])
    print(result[0],"\n",result[1],"\n",result[2])
    print(sess.run(a1))
    print(sess.run(a2))
    print(sess.run(a3))


