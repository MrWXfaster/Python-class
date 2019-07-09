'''
tf.control_dependencies(control_inputs)
该函数的参数是一个包含Op或者tensor的列表，列表里的操作的执行顺序先于context里面定义的Op和tensor；
该函数返回一个上下文管理器
'''
'''
首先我们先介绍tf.control_dependencies，
该函数保证其辖域中的操作必须要在该函数所传递的参数中的操作完成后再进行。请看下面一个例子。
'''
import tensorflow as tf
a1 = tf.Variable(1)
b1 = tf.Variable(2)
update_op = tf.assign(a1,10)
add = tf.add(a1, b1)

a_2 = tf.Variable(1)
b_2 = tf.Variable(2)
update_op = tf.assign(a_2, 10)

with tf.control_dependencies([update_op]):
    add_with_dependencies = tf.add(a_2, b_2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    ans_1, ans_2 = sess.run([add, add_with_dependencies])
    print('Add:', ans_1)
    print('Add_with_dependency:',ans_2)
'''
可以看到两组加法进行的对比，正常的计算图在计算add时是不会经过update_op操作的，因此在加法时a的值为1，
但是采用tf.control_dependencies函数，可以控制在进行add前先完成update_op的操作，因此在加法时a的
值为10，因此最后两种加法的结果不同。

'''

