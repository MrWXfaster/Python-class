'''
关于tf.GraphKeys.UPDATE_OPS，这是一个tensorflow的计算图中内置的一个集合，
其中会保存一些需要在训练操作之前完成的操作，并配合tf.control_dependencies函数使用。
关于在batch_norm中，即为更新mean和variance的操作。通过下面一个例子可以看到
tf.layers.batch_normalization中是如何实现的。
'''
import tensorflow as tf

is_training = tf.placeholder(dtype=tf.bool)
input = tf.ones([1,2,2,3])
output = tf.layers.batch_normalization(input, training = is_training)

update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
print(update_ops)
#with tf.control_dependencies(update_ops):
#train_op = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.save(sess, 'batch_norm_layer/Model')
'''
可以看到输出的即为两个batch_normalization中更新mean和variance的操作，需要保证它们在train_op前完成。
这两个操作是在tensorflow的内部实现中自动被加入tf.GraphKeys.UPDATE_OPS这个集合的，
在tf.contrib.layers.batch_norm的参数中可以看到有一项updates_collections的默认值
即为tf.GraphKeys.UPDATE_OPS，而在tf.layers.batch_normalization中则是直接将两个更新操作放入了上述集合。
'''


