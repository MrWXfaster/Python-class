
'''
- 控制依赖
with tf.control_dependencies([train_step, variables_averages_op]):
    train_op = tf.no_op(name='train') #train_op does nothin
'''
'''
该函数的参数是一个包含Op或者tensor的列表，列表里的操作的执行顺序先于context里面定义的Op和tensor；
该函数返回一个上下文管理器
'''

#https://blog.csdn.net/PKU_Jade/article/details/73498753 