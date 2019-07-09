import numpy as np
import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

# 获取数据集，并采用采用one_hot热编码
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

with tf.name_scope('input'):
    x_input = tf.placeholder(tf.float32, [None, 784],name='x_input')
    y_actual = tf.placeholder(tf.float32, shape=[None, 10],name = 'y_input')
    keep_prob = tf.placeholder("float",name='keep_prob')

# 初始化权重参数
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1,name='weight_variable')
    return tf.Variable(initial)

# 初始化偏执参数
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape,name='bias_variable')
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# input -> conv -> pool -> conv -> pool -> fc -> dropout -> softmax
def network(x):
    with tf.name_scope('reshape'):
        x_image = tf.reshape(x, [-1, 28, 28, 1],name='reshape')
        tf.summary.image('input', x_image, 5)   #显示图片
    with tf.name_scope('h_conv1'):
        W_conv1 = weight_variable([5, 5, 1, 32])
        tf.summary.histogram('layer1_weights',W_conv1)
        b_conv1 = bias_variable([32])
        tf.summary.histogram('layer1_bias', b_conv1)
        h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1,name='h_conv1')  # conv1
    with tf.name_scope('h_pool1'):
        h_pool1 = max_pool(h_conv1)  # max_pool1
    with tf.name_scope('h_conv2'):
        W_conv2 = weight_variable([5, 5, 32, 64])
        tf.summary.histogram('layer2_weights', W_conv2)
        b_conv2 = bias_variable([64])
        tf.summary.histogram('layer2_bias', b_conv2)
        h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2,name='h_conv2')  # conv2
    with tf.name_scope('h_pool2'):
        h_pool2 = max_pool(h_conv2)  # max_pool2
    with tf.name_scope('fc1'):
        W_fc1 = weight_variable([7 * 7 * 64, 1024])
        tf.summary.histogram('function1_weights', W_fc1)
        b_fc1 = bias_variable([1024])
        tf.summary.histogram('function1_bias', b_fc1)
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64],name='h_poo2_flat')
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1,name='fc1')  # fc1

    with tf.name_scope('dropout'):
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)  # dropout
        tf.summary.histogram('dropout', h_fc1_drop)
    with tf.name_scope('fc2'):
        W_fc2 = weight_variable([1024, 10])
        tf.summary.histogram('function2_weights', W_fc2)
        b_fc2 = bias_variable([10])
        tf.summary.histogram('function2_bias', b_fc2)  ##采用直方图形式
    with tf.name_scope('y_predicts'):
        y_predicts = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2,name='y_predicts')
        tf.summary.histogram('y_predicts', y_predicts)
    return y_predicts

y_predict = network(x_input)



with tf.name_scope('cross_entropy'):
    cross_entropy = -tf.reduce_sum(y_actual * tf.log(y_predict),name='cross_entropy')
    tf.summary.scalar('cross_entropy',cross_entropy)
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(1e-3).minimize(cross_entropy)
with tf.name_scope('accuracy'):
    correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y_actual, 1),name='correct_prediction')
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"),name='accuracy')
    tf.summary.scalar('accuracy', accuracy)

# saver = tf.train.Saver()
sess =tf.Session()

# summaries合并
merged = tf.summary.merge_all()
# 写到指定的磁盘路径中,保存Tensorboard,到指定文件

writer = tf.summary.FileWriter("log/", sess.graph)

# 运行初始化所有变量

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

for i in range(201):  # iteration 20000 steps = (epochs * train_size) / batch_size ,epochs=21
    batch = mnist.train.next_batch(64)  # batch_size=64
    if i % 10 == 0:
        train_acc = accuracy.eval(feed_dict={x_input: batch[0], y_actual: batch[1], keep_prob: 1.0})
        result = sess.run(merged,feed_dict={x_input: batch[0], y_actual: batch[1], keep_prob: 0.5})
        writer.add_summary(result,i)  #将所有的数据加载在图中
        print('step', i, 'training accuracy', train_acc)
        train_step.run(feed_dict={x_input: batch[0], y_actual: batch[1], keep_prob: 0.5})
# saver.save(sess, "my_net/model_save.ckpt")  # save model
# test accuracy in mnist.test dataset
test_acc = accuracy.eval(feed_dict={x_input: mnist.test.images, y_actual: mnist.test.labels, keep_prob: 1.0})
print("test accuracy", test_acc)
writer.close()