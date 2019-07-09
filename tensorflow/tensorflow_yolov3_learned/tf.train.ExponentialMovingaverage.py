# 定义变量一级滑动平均类
import tensorflow as tf
# 定义一个32位浮点变量,初始值为0.0, 这个代码就是在不断更新w1参数,优化 w1,滑动平均做了一个w1的影子
w1 = tf.Variable(0, dtype=tf.float32)
# 定义num_updates(NN 的迭代次数)初始值为0, global_step不可被优化(训练) 这个额参数不训练
global_step = tf.Variable(0, trainable=False)
# 设置衰减率0.99 当前轮数global_step
MOVING_AVERAGE_DECAY = 0.99
ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
# ema.apply后面的括号是更新列表,每次运行sess.run(ema_op)时,对更新列表中的元素求滑动平均值,
# 在实际应用中会使用tf.trainable_variable()自动将所有待训练的参数汇总为列表
# ema_op=ema.apply([w1])
ema_op = ema.apply(tf.trainable_variables())

# 查看不同迭代中变量的取值变化
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    # ema_op=ema.apply([w1])获取w1 的滑动平均值,
    print(sess.run([w1, ema.average(w1)]))  # 打印当前参数w1和w1 的滑动平均值 (0,0)
    sess.run(tf.assign(w1, 1))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))  # (1,0.9)
    # 跟新step w1的值,模拟出100轮迭代后,参数w1 变为10
    sess.run(tf.assign(global_step, 100))
    sess.run(tf.assign(w1, 10))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))  # (10,1.644)

    # 每次sess.run会更新一次w1的滑动平均值
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

