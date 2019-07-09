# import tensorflow as tf
# import numpy as np
#
#
# #create data
# x_data = np.random.rand(100).astype(np.float32)#创建100个随机数，类型是float32
# y_data = x_data*0.1+0.3
#
#
# """ structure """
#
#
# Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))#random_uniform（[1]）代表是一维张量
# biases=tf.Variable(tf.zeros([1]))
#
#
# y=Weights*x_data+biases
#
#
# Loss=tf.reduce_mean(tf.square(y-y_data))
# optimizer=tf.train.GradientDescentOptimizer(0.5)
# train=optimizer.minimize(Loss)
#
#
# init = tf.global_variables_initializer()#把这个模型运动起来，即初始化所有之前定义的Variable,
#
# """ end   """
#
#
# sess = tf.Session()
# sess.run(init)   #activate the structure
#
#
# for step in range(2002):
#   sess.run(train)#运行train
#   if step % 10 ==0:
#      print(step,sess.run(Weights),sess.run(biases))

import tensorflow as tf
import numpy as np

### creat data

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.3 +  0.1

### structure start

Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

### structure end

sess = tf.Session()
sess.run(init)

for step in range(2002):
    sess.run(train)
    if step %10  == 0:
        print(step,sess.run(Weights),sess.run(biases))
