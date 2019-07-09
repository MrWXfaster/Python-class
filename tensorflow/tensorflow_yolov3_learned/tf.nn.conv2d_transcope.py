'''
反卷积就是反向卷积
conv2d_transpose(value, filter, output_shape, strides, padding="SAME",
                data_format="NHWC", name=None)

除去name参数用以指定该操作的name，与方法有关的一共六个参数：
第一个参数value：指需要做反卷积的输入图像，它要求是一个Tensor
第二个参数filter：卷积核，它要求是一个Tensor，具有[filter_height, filter_width, out_channels, in_channels]这样的shape，
                具体含义是[卷积核的高度，卷积核的宽度，卷积核个数，图像通道数]
第三个参数output_shape：反卷积操作输出的shape，细心的同学会发现卷积操作是没有这个参数的，
                        那这个参数在这里有什么用呢？下面会解释这个问题
第四个参数strides：反卷积时在图像每一维的步长，这是一个一维的向量，长度4
第五个参数padding：string类型的量，只能是"SAME","VALID"其中之一，这个值决定了不同的卷积方式
第六个参数data_format：string类型的量，'NHWC'和'NCHW'其中之一，这是tensorflow新版本中新加的参数，
                    它说明了value参数的数据格式。'NHWC'指tensorflow标准的数据格式
                    [batch, height, width, in_channels]，'NCHW'指Theano的数据格式,
                    [batch, in_channels，height, width]，当然默认值是'NHWC'

'''
import tensorflow as tf
x1 = tf.constant(1.0, shape=[1,3,3,1])
kernel = tf.constant(1.0, shape=[3,3,3,1])

x2 = tf.constant(1.0, shape=[1,6,6,3])
x3 = tf.constant(1.0, shape=[1,5,5,3])

y2 = tf.nn.conv2d(x3,kernel,padding="SAME",strides=[1,2,2,1],name="conv0")

with tf.Session() as sess:
    sess.run(y2)
    print(y2)
'''
又一个很重要的部分！tf.nn.conv2d中的filter参数，是[filter_height, filter_width, in_channels, out_channels]的形式，
而tf.nn.conv2d_transpose中的filter参数，是[filter_height, filter_width, out_channels，in_channels]的形式，
注意in_channels和out_channels反过来了！因为两者互为反向，所以输入输出要调换位置
'''
y3 = tf.nn.conv2d_transpose(y2,kernel,output_shape=[1,5,5,3],strides=[1,2,2,1],padding="SAME",name="de_conv0")
y4 = tf.nn.conv2d(x2, kernel, strides=[1,2,2,1], padding="SAME",name="conv1")
print(y3,"\n",y4)
