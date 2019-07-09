'''
一 tf.global_variables_initializer()
tf.global_variables_initializer()添加节点用于初始化所有的变量(GraphKeys.VARIABLES)。
返回一个初始化所有全局变量的操作（Op）。在你构建完整个模型并在会话中加载模型后，运行这个节点。
能够将所有的变量一步到位的初始化，非常的方便。通过feed_dict, 你也可以将指定的列表传递给它，
只初始化列表中的变量。
‘’‘


’‘’
二 tf.local_variables_initializer()
tf.local_variables_initializer()返回一个初始化所有局部变量的操作（Op）。初始化局部变量（GraphKeys.LOCAL_VARIABLE）。
GraphKeys.LOCAL_VARIABLE中的变量指的是被添加入图中，但是未被储存的变量。
‘’‘
