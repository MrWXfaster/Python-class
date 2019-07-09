import tensorflow as tf
state=tf.Variable(0,name='counter')#定义一个变量,计数类型
 # print(state.name)
# 变量+常量=变量
one=tf.constant(1) #定义一个常量
new_value=tf.add(state,one)
#将state用new_value代替
updata=tf.assign(state,new_value)
 #变量必须要激活
init=tf.global_variables_initializer() #必须激活
with tf.Session() as sess:
   sess.run(init)#激活
   for _ in range(3):#作用是让这个更新三次
     sess.run(updata)
     print(sess.run(state))
#rang()即为生成一个列表·[0,1,2]
for i in range(3):
    print(i)
