import tensorflow as tf
 
matrix1 = tf.constant([[3,3]])#申明一个一行两列的矩阵
matrix2 = tf.constant([[2],
                        [2]])#申明一个两行一列的矩阵
product = tf.matmul( matrix1 , matrix2) #matrix multiply np.dot(m1,m2)



#method 1
# sess = tf.Session()#使用tf.Session()使用会话
# result = sess.run(product)#运行sess
# print(result)
# sess.close()#最后要关闭


# #method 2
# with tf.Session() as sess:#打开Session,给它一个命名，自动关闭sess
#     result2 = sess.run(product)
#     print(result2)

a = tf.constant(0.1, shape=[32])
sess = tf.Session()
result3 = sess.run(a)
print(result3)
sess.close()

