'''
tf.Graph() 函数非常重要，注意提现在两个方面
1. 它可以通过tensorboard用图形化界面展示出来流程结构
2. 它可以整合一段代码为一个整体存在于一个图中

声明情况大体有三种
'''
'''
1. tensor:通过张量本身直接出graph
'''
# -*- coding: utf-8 -*-
import tensorflow as tf
c = tf.constant(4.0)
sess= tf.Session()
sess.run(tf.global_variables_initializer())

c_out = sess.run(c)

print(c_out)
print(c.graph == tf.get_default_graph())
print(c.graph)
print(tf.get_default_graph())
'''
2.通过声明一个默认的，然后定义张量内容，在后面可以调用或保存
'''
# -*- coding: utf-8 -*-
import tensorflow as tf

g = tf.Graph()
with g.as_default():
    c = tf.constant(4.0)

sess = tf.Session(graph=g)
c_out = sess.run(c)
print(c_out)
print(g)
print(tf.get_default_graph())
'''
3.通过多个声明，在后面通过变量名来分别调用
'''
# -*- coding: utf-8 -*-
import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    c1 = tf.constant(4.0)

g2 = tf.Graph()
with g2.as_default():
    c2 = tf.constant(20.0)

with tf.Session(graph=g1) as sess1:
    print(sess1.run(c1))
with tf.Session(graph=g2) as sess2:
    print(sess2.run(c2))
'''
对graph的操作大体有三种
'''

'''
1.保存
'''
g1 = tf.Graph()
with g1.as_default():
    # 需要加上名称，在读取pb文件的时候，是通过name和下标来取得对应的tensor的
    c1 = tf.constant(4.0,name='c1')
g2 = tf.Graph()
with g2.as_default():
    c2 = tf.constant(20.0, name='c2')
with tf.Session(graph=g1) as sess1:
    print(sess1.run(c1))
with tf.Session(graph=g2) as sess2:
    print(sess2.run(c2))

# g1的图定义，包含pb的path, pb文件名，是否是文本默认False
tf.train.write_graph(g1.as_graph_def(),'.','graph.pb',False)
'''
2.从pb文件中调用
'''
#load graph
with tf.gfile.FastGFile("./graph.pb",'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
sess = tf.Session()
c1_tensor = sess.graph.get_tensor_by_name("c1:0")
c1 = sess.run(c1_tensor)
print(c1)
'''
穿插调用
'''
# -*- coding: utf-8 -*-
g1 = tf.Graph()
with g1.as_default():
    # 声明的变量有名称是一个好的习惯，方便以后使用
    c1 = tf.constant(4.0, name="c1")

g2 = tf.Graph()
with g2.as_default():
    c2 = tf.constant(20.0, name="c2")

with tf.Session(graph=g2) as sess1:
    # 通过名称和下标来得到相应的值
    c1_list = tf.import_graph_def(g1.as_graph_def(), return_elements=["c1:0"], name='')
    print(sess1.run(c1_list[0] + c2))

g2 = tf.Graph()
with g2.as_default():
    c2 = tf.constant(20.0, name='c2')
with tf.Session(graph=g2) as sess1:
    # 通过名称和下标来得到相应的值
    with tf.gfile.FastGFile('./graph.pb','rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def,name = '')
    sess = tf.Session()
    c1_tensor = sess.graph.get_tensor_by_name('c1:0')
    c1 = sess.run(c1_tensor)
    print(sess1.run(c2)+c1)