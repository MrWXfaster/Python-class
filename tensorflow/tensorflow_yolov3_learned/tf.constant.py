import tensorflow as tf


# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
with tf.name_scope("matrix"):
    matrix1 = tf.constant([[3., 3.]],name="matrix1")
#
# 创建另外一个常量 op, 产生一个 2x1 矩阵.
with tf.name_scope("matrix1"):
    matrix2 = tf.constant([[2.],[2.]],name="matrix2")

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
with tf.name_scope("product"):
    product = tf.matmul(matrix1, matrix2,name="result")
    # print(product)

# # method 1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()
# method2

constant (
    value ,
    dtype = None ,
    shape = None ,
    name = 'Const' ,
    verify_shape = False
)
'''
创建一个常数张量. 
生成的张量由 dtype 类型的值填充,如参数值和 (可选) 形状所指定 (请参见下面的示例).
参数值可以是常量值,或者是 dtype 类型的值的列表.如果值是一个列表, 则列表的长度必须小于或等于
形状参数所隐含的元素数 (如果指定).如果列表长度小于由形状指定的元素数, 则列表中的最后一个元素将用于填充剩余的项.
参数形状是可选的.如果存在,它指定生成的张量的维度.如果不存在, 则使用值的形状.
如果未指定参数 dtype, 则从值类型推断类型.'''
'''
例如：

```python ＃常数一维张量使用 list. tensor = tf.constant([1,2,3,4,5,6,7])=> [1 2 3 4 5 6 7] 的值填充

＃常数二维张量用标量值 -1.tensor= tf.constant(-1.0,shape = [2,3])=> [[-1.-1.-1.] [-1.-1.-1.]] 填充```