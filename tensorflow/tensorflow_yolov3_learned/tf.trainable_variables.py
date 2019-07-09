'''
tf.trainable_variables返回的是需要训练的变量列表

tf.all_variables返回的是所有变量的列表
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

v = tf.Variable(tf.constant(0.0, shape=[1],dtype=tf.float32),name = 'v')
v1 = tf.Variable(tf.constant(5, shape=[1], dtype=tf.float32), name = 'v1')

global_step = tf.Variable(tf.constant(5, shape=[1],dtype=tf.float32),name= 'global_step',trainable =False)

for ele1 in tf.trainable_variables():
    print(ele1.name)
for ele in tf.global_variables():
    print(ele.name)
'''
tf.all_variables已经不使用，
代替为tf.global_variables
'''