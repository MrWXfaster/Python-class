import tensorflow as tf
# sess = tf.Session()
# merged_summary_op = tf.summary.merge_all()
# summary_writer = tf.summary.FileWriter('/tmp/mnist_logs', sess.graph)
# total_step = 0
# while training:
#   total_step += 1
#   session.run(training_op)
#   if total_step % 100 == 0:
#     summary_str = session.run(merged_summary_op)
#     summary_writer.add_summary(summary_str, total_step)

# Create a variable with a random value.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
# Create another variable with the same value as 'weights'.
w2 = tf.Variable(weights.initialized_value(), name="w2")
# Create another variable with twice the value of 'weights'
w_twice = tf.Variable(weights.initialized_value() * 0.2, name="w_twice")

