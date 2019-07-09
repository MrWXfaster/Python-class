'''
  ref,  A mutable Tensor. Should be from a Variable node. May be uninitialized. 待赋值的变量   value,# value: A Tensor. Must have the same type as ref. The value to be assigned to the variable. 使用张量赋值
  validate_shape=None,
  use_locking=None,
  name=None
'''
'''
return A Tensor that will hold the new value of 'ref' after the assignment has completed. 返回ref。
https://www.tensorflow.org/api_docs/python/tf/assign
assign  指派
将 ref 赋值为 value，必须维度相同

tf.assign_add(
    ref,
    value,
    use_locking=None,
    name=None
)
ref = ref + value  相加操作，赋值给ref
return Same as "ref". Returned as a convenience for operations that
 want to use the new value after the variable has been updated.
'''

import tensorflow as tf

x = tf.Variable(tf.constant(0.0), dtype=tf.float32)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("value x: ", sess.run(x))
    y = tf.assign(x, 20)
    print("value y； ", sess.run(y))
    print("tensor y: ", y)
    z = tf.assign_add(y, 11)
    print("value z: ", sess.run(z))
