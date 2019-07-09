#可视化tensorflow1
import tensorflow as tf
import numpy as np


#添加或者定义一个层
def add_layer(inputs,in_size,out_size,activation_function = None):#（输入值，输入的数量，输出的数量，激励函数）
  with tf.name_scope("layer"):#大的框架
    with tf.name_scope("weights"):#定义权重
      Weights = tf.Variable(tf.random_normal([in_size, out_size]),name="W")#定义权重，定义随机变量，变量矩阵 in_size行，out_size列;
    with tf.name_scope("biases"):
      biases = tf.Variable(tf.zeros([1,out_size]) + 0.1 )#列表
    with tf.name_scope("Wx_plus_b"):
      Wx_plus_b = tf.add(tf.matmul(inputs,Weights),biases)
    if activation_function is None:#看是否是一个线性算法
       outputs = Wx_plus_b
    else:
       outputs = activation_function(Wx_plus_b)
    return outputs

#data for training
x_data = np.linspace(-1,1,300)[:,np.newaxis]#有300行，300个例子
noise = np.random.normal(0,0.05,x_data.shape)#方差0.05,格式和X_data一样
y_data = np.square(x_data)  - 0.5 + noise
#data holder  define placeholder for inputs to network

with tf.name_scope("inputs"):#申明输入包括了下面的东西
  xs = tf.placeholder(tf.float32,[None,1],name = "x_input")
  ys = tf.placeholder(tf.float32,[None,1],name = "y_input")
#隐藏层

l1 = add_layer(xs,1,10,activation_function  = tf.nn.relu)#X_data时输入值，1，输入层，输出层
#输出层

prediction = add_layer(l1,10,1,activation_function = None)
#损失函数

with tf.name_scope("loss"):
  loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
#训练
with tf.name_scope("train"):
  train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)#
#初始化变量Important step

#init = tf.initialize_all_variables()
sess = tf.Session()
writer= tf.summary.FileWriter("logs/",sess.graph)#graph是整个框架very important 有坑
sess.run(tf.global_variables_initializer())#globel
