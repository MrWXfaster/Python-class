import tensorflow as tf

x = tf.placeholder('float',shape = [None,784])
label = tf.placeholder("float",shape = [None,10])

w_fc1 = tf.Variable(tf.truncated_normal([784,1024],stddev = 0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape = [1024]))
h_fc1 = tf.matmul(x,w_fc1) + b_fc1

w_fc2 = tf.Variable(tf.truncated_normal([1024,10],stddev = 0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape = [10]))
y = tf.nn.softmax(tf.matmul(h_fc1,w_fc2) + b_fc2)

cross_entroy = -tf.reduce_sum(label * tf.log(y))


#方式二，使用tf.nn.softmax_cross_entropy_with_logits
import tensorflow as tf

x = tf.placeholder('float', shape = [None,784])
label = tf.placeholder("float", shape = [None,10])

w_fc1 = tf.Variable(tf.truncated_normal([784,1024],stddev = 0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape = [1024]))
h_fc1 = tf.matmul(x, w_fc1) + b_fc1

w_fc2 = tf.Variable(tf.truncated_normal([1024,10],stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape = [10]))
y = tf.matmul(h_fc1, w_fc2) + b_fc2

cross_entroy = -tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits_v2(labels=label,logits=y))

