'''
tf.image.resize_nearest_neighbor(
    images,
    size,
    align_corners=False,
    name=None
)
使用最近邻插值调整images为size.

参数：

    images：一个Tensor,必须是下列类型之一：int8,uint8,int16,uint16,int32,int64,half,float32,float64.4-D与形状[batch, height, width, channels].
    size：2个元素(new_height, new_width)的1维int32张量,表示图像的新大小.
    align_corners：可选的bool,默认为False,如果为True,则输入和输出张量的4个角像素的中心对齐,并保留角落像素处的值.
    name：操作的名称(可选).

返回：

该函数与images具有相同类型的Tensor.
'''
'''
function:在使用TensorFlow进行图片的放大缩小时，有三种方式：
1、tf.image.resize_nearest_neighbor（）:临界点插值
2、tf.image.resize_bilinear(）：双线性插值
3、tf.image.resize_bicubic(）：双立方插值算法
'''
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

image_raw_data = tf.gfile.GFile('./CNN_V3/Image/Fashion/ankle boot.jpg','rb').read() # 加载原始图像

with tf.Session() as sess:
    img_data = tf.image.decode_jpeg(image_raw_data)
# '''
# 一张RGB图像可以看成一个三维的矩阵，矩阵中的每一个数表示了图像上不同位置，不同颜色的亮度。
# 然而图像在存储时并不是直接记录这些矩阵中的数字，而是记录经过压缩编码之后的结果。
# 所以要将一张图象还原成一个三维矩阵。需要解码的过程。
# '''
    plt.imshow(img_data.eval())
    plt.show()
    resized = tf.image.resize_images(img_data,[300,300],method = 0)
    ''' 第一个参数为原始图像，第二个参数为图像大小，第三个参数给出了指定的算法'''
    resized = np.asarray(resized.eval(),dtype='uint8')
    plt.imshow(resized)
    plt.show()

    croped = tf.image.resize_image_with_crop_or_pad(img_data,200,200)# 目标图像大小<原始图像的大小，则截取原始图像的居中部分
    padded = tf.image.resize_image_with_crop_or_pad(img_data,200,800)#目标图像大小>原始图像的大小，则会在原始图像的四周填充全为0背景
    plt.imshow(croped.eval())
    plt.show()
    plt.imshow(padded.eval())
    plt.show()
    
    central_cropped = tf.image.central_crop(img_data,0.5)# 按照比例裁剪图像，第二个参数为调整比例，比例取值[0,1]
    plt.imshow(central_cropped.eval())
    plt.show()

    
  