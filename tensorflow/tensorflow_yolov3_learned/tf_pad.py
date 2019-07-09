'''
tf.pad(input, paddings,mode='CONSTANT', name=None)
input : 代表输入张量
padding ： 代表加的边界
mode : "CONSTANT" 是填充0,
       "REFLECT"是映射填充，上下（1维）填充顺序和paddings是相反的，左右（零维）顺序补齐
       "SYMMETRIC"是对称填充，上下（1维）填充顺序是和paddings相同的，左右（零维）对称补齐
name ： 代表此操作的名字
'''
'''
padding它必须是 [N, 2] 形式，N代表张量的阶， 2代表必须是2列，比如
padding = [ [1,1], [2,2] ]   或者
padding = [ [1,1], [2,2], [3,3] ]
具体根据需要设定，但列必须为2，不然报错
首先，假定 一个3x1的一个张量input = [[1],[2],[3]] ， padding = [[1,1], [2,2]]
'''
import tensorflow as tf
input = [[1],[2],[3]]
padding = [[1,2],
           [1,2]]
with tf.Session() as sess:
    print(sess.run(tf.pad(input,padding)))

input = [[1], [2], [3]]
padding = [[3,1],
           [2,5]]
with tf.Session() as sess:
    print(sess.run(tf.pad(input,padding)))
    
'''
padding中[3,1]表示在输入矩阵上面补3行0,下面补1行0
         [2,5]表示在上面的基础上的矩阵左边补2列0,右边补3列0
'''
