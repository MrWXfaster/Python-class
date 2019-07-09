# 1、cap = cv2.VideoCapture(0)
#
# VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
# 如cap = cv2.VideoCapture(“../test.avi”)
#
# 2、ret,frame = cap.read()
#
# cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。
# 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
#
# 3、cv2.waitKey(1)，waitKey（）方法本身表示等待键盘输入，
#
# 参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
#
# 参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停,；
#
# 参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿。
#
# c得到的是键盘输入的ASCII码，esc键对应的ASCII码是27，即当按esc键是if条件句成立
#
# 4、调用release()释放摄像头，调用destroyAllWindows()关闭所有图像窗口。
# cv2.imshow()
#
#     cv2.imShow()函数可以在窗口中显示图像。该窗口和图像的原始大小自适应（自动调整到原始尺寸）。


# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# import numpy as np
# import cv2
#
# # Create a black image
# img=np.zeros((512,512,3), np.uint8)
#
# # Draw a diagonal blue line with thickness of 5 px
# cv2.line(img,(0,0),(511,511),(0,0,255),1)#前面两个坐标为构成线的两个点，最后一个（RGB）光学三原色,最后一个为线段的宽度
# #cv2.line(img,(0,256),(511,256),(0,255,0),1)
# cv2.line(img,(0,511),(511,0),(255,0,0),1)
# #510-384=126 ; 128-0=128
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# img = [11,22,23,45.4]
# a = max(img)
# print(a)
# b = img.index(max(img))
# print(b)


# cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)画出矩行
#
# 参数解释
#
# 第一个参数：img是原图
#
# 第二个参数：（x，y）是矩阵的左上点坐标
#
# 第三个参数：（x+w，y+h）是矩阵的右下点坐标
#
# 第四个参数：（0,255,0）是画线对应的rgb颜色
#
# # 第五个参数：2是所画的线的宽度


# cv2.resize(src,dsize,dst=None,fx=None,fy=None,interpolation=None)
#
# scr:原图
#
# dsize：输出图像尺寸
#
# fx:沿水平轴的比例因子
#
# fy:沿垂直轴的比例因子
#
# interpolation：插值方法