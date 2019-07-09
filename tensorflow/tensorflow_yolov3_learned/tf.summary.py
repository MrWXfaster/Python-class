'''
tf.summary()
通常情况下，我们在训练网络时添加summary都是通过如下方式：
'''
'''
tf.scalar_summary(tags, values)
# ...
summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter(logdir, graph=sess.graph)
summary_str = sess.run(summary_op)
summary_writer.add_summary(summary_str, global_step)
'''
#逐条代码分析
'''
 tf.summary.merge_all    
merge_all 可以将所有summary全部保存到磁盘，以便tensorboard显示。如果没有特殊要求，
一般用这一句就可一显示训练时的各种信息了。
格式：tf.summaries.merge_all(key='summaries')
'''


'''
tf.summary.FileWriter  
指定一个文件用来保存图。
格式：tf.summary.FileWritter(path,sess.graph)
可以调用其add_summary（）方法将训练过程数据保存在filewriter指定的文件中
'''
#eg
tf.summary.scalar('accuracy',acc)                   #生成准确率标量图
merge_summary = tf.summary.merge_all()
train_writer = tf.summary.FileWriter(dir,sess.graph)#定义一个写入summary的目标文件，dir为写入文件地址
# ......(交叉熵、优化器等定义)
for step in xrange(training_step):                  #训练循环
    train_summary = sess.run(merge_summary,feed_dict =  {...})#调用sess.run运行图，生成一步的训练过程数据
    train_writer.add_summary(train_summary,step)#调用train_writer的add_summary方法将训练过程以及训练步数保存
#此时开启tensorborad：
'''tensorboard --logdir=/summary_dir '''


'''
tf.summary.merge()   tf.summary.merge(inputs, collections=None, name=None)
一般选择要保存的信息还需要用到tf.get_collection()函数
'''
#方式一
#eg
tf.summary.scalar('accuracy',acc)                   #生成准确率标量图
merge_summary = tf.summary.merge([tf.get_collection(tf.GraphKeys.SUMMARIES,'accuracy'),...(其他要显示的信息)])
train_writer = tf.summary.FileWriter(dir,sess.graph)#定义一个写入summary的目标文件，dir为写入文件地址
# ......(交叉熵、优化器等定义)
for step in xrange(training_step):                  #训练循环
    train_summary = sess.run(merge_summary,feed_dict =  {...})#调用sess.run运行图，生成一步的训练过程数据
    train_writer.add_summary(train_summary,step)#调用train_writer的add_summary方法将训练过程以及训练步数保存
'''
使用tf.get_collection函数筛选图中summary信息中的accuracy信息，这里的
 tf.GraphKeys.SUMMARIES  是summary在collection中的标志。
'''

#方式二
acc_summary = tf.summary.scalar('accuracy',acc)                   #生成准确率标量图
merge_summary = tf.summary.merge([acc_summary ,...(其他要显示的信息)])  #这里的[]不可省