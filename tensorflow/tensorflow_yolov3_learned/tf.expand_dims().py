'''
tf.expand_dims(
    input,
    axis=None,
    name=None,
    dim=None
)
 他所实现的功能是给定一个input，在axis轴处给input增加一个为1的维度。
'''
import tensorflow as tf

# 't2' is a tensor of shape [2, 3, 5]
t2  = tf.zeros((2,3,5))
expand = tf.shape(tf.expand_dims(t2, 0))  # [1, 2, 3, 5]
'''
因为axis=0所以矩阵的维度变成1*2*3*5。

同理如果axis=2，矩阵就会变为2*3*1*5。

0其实代表的第一维度，那么1代表第二维度，2代表第三位度。以此类推。

-1代表最后的一维的度
'''
print(expand)