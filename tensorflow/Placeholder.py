#placeholder
import tensorflow as tf

# input1 = tf.placeholder(tf.float32)#给它一个值的位置，是float32形式
# input2 = tf.placeholder(tf.float32)#如果用placeholder,则在使用sess.run()时，要再给其输出一个值有点类似于函数
#
#
# output = tf.multiply(input1,input2)#两个浮点型矩阵相乘
# with tf.Session() as sess:
#    print(sess.run(output,feed_dict = {input1:[7.],input2:[2.]}))#feed_dict即为一个字典



output2 = tf.Variable(1.0)
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

update = tf.assign(output2,output)#把output传给了output2

init = tf.global_variables_initializer()


with tf.Session() as sess:
   sess.run(init)
   print(sess.run(update, feed_dict={input1: 7., input2: 2.}))
   print(sess.run(output,feed_dict = {input1:[2.],input2:[7.]}))
   print(sess.run(output2))