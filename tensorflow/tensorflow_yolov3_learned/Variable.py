import tensorflow as tf

# 创建一个变量, 初始化为标量 0.
state = tf.Variable(0, name="counter")

# 创建一个 op, 其作用是使 state 增加 1

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
init_op = tf.initialize_all_variables()

# 启动图, 运行 op
with tf.Session() as sess:
  # 运行 'init' op
  sess.run(init_op)
  # 打印 'state' 的初始值
  print(sess.run(state))
  # 运行 op, 更新 'state', 并打印 'state'
  for _ in range(3):
    sess.run(update)
    print(sess.run(state))


state=tf.Variable(0,name='counter')
 # print(state.name) 
# 变量+常量=变量 
one=tf.constant(1) 
new_value=tf.add(state,one) 
#将state用new_value代替 
updata=tf.assign(state,new_value)
 #变量必须要激活
init=tf.global_variables_initializer() 
with tf.Session() as sess: 
   sess.run(init)
   for _ in range(3): 
     sess.run(updata) 
     print(sess.run(state))