import tensorflow as tf
import numpy as np

with tf.name_scope("input"):#没有出现
# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
    x_data = np.float32(np.random.rand(2, 100)) # 随机输入
    y_data = np.dot([0.100, 0.200], x_data) + 0.300
with tf.name_scope('parameter'):
# 构造一个线性模型
    b = tf.Variable(tf.zeros([1]),name="bias")
    W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0),name='weight')
    y = tf.matmul(W, x_data) + b
with tf.name_scope("loss"):
# 最小化方差
    loss = tf.reduce_mean(tf.square(y - y_data),name='loss')
    tf.summary.scalar("loss", loss)
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)


# 初始化变量
# init = tf.initialize_all_variables()
init = tf.global_variables_initializer()


# 启动图 (graph)
sess = tf.Session()
sess.run(init)
# 合并所有的summary
merged = tf.summary.merge_all()
# 保存Tensorboard文件
writer = tf.summary.FileWriter("log/", sess.graph)
#保存权重文件
saver = tf.train.Saver(max_to_keep=1)
sess.run(train)
# 拟合平面
for step in range(0, 201):
    if step % 10 == 0:
        w = sess.run(W)
        B = sess.run(b)
        print (step, w, B)
    saver.save(sess, "my_net/model.ckpt")
sess.close()

# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]

