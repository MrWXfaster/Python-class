import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import math


# 直线方程函数
def f_1(x, A, B):
    return A * x + B


# 二次曲线方程
def f_2(x, A, B, C):
    return A * x * x + B * x + C


# 三次曲线方程
def f_3(x, A, B, C, D):
    return A * x * x * x + B * x * x + C * x + D


def plot_test():
    plt.figure()

    # 拟合点
    x0 = [1, 2, 3, 4, 5]
    y0 = [1, 3, 8, 18, 36]

    # 绘制散点
    plt.scatter(x0[:], y0[:], 25, "red")

    # 直线拟合与绘制
    A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
    x1 = np.arange(0, 6, 0.01)
    y1 = A1 * x1 + B1
    plt.plot(x1, y1, "blue")

    # 二次曲线拟合与绘制
    A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]
    x2 = np.arange(0, 6, 0.01)
    y2 = A2 * x2 * x2 + B2 * x2 + C2
    plt.plot(x2, y2, "green")

    # 三次曲线拟合与绘制
    A3, B3, C3, D3 = optimize.curve_fit(f_3, x0, y0)[0]
    x3 = np.arange(0, 6, 0.01)
    y3 = A3 * x3 * x3 * x3 + B3 * x3 * x3 + C3 * x3 + D3
    plt.plot(x3, y3, "purple")

    plt.title("test")
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

    return

# if __name__ == '__main__':
#     curve_fitting = plot_test()

import matplotlib.pyplot as plt

x = [[1, 3], [2, 5]] # 要连接的两个点的坐标
y = [[4, 7], [6, 3]]

for i in range(len(x)):

    plt.plot(x[i], y[i], color='r')
    plt.scatter(x[i], y[i], color='b')
# plt.show()

# import tensorflow as tf
# x = tf.tile(tf.range(1920, dtype=tf.int32)[:, tf.newaxis], [1, 1920])
# y = tf.tile(tf.range(1440, dtype=tf.int32)[tf.newaxis, :], [1440, 1])
# x1,y1= x[:,:, tf.newaxis],y[:,:, tf.newaxis]
# xy_grid = tf.concat([x[:, :, tf.newaxis], y[:, :, tf.newaxis]], axis=-1)
# sess = tf.Session()
# print(sess.run([x1,y1,xy_grid]))

# import cv2
#
# src =cv2.imread('/home/asus/PycharmProjects/arithmetic/venv/Figure5.png')
#
# cv2.namedWindow('input_image')
# cv2.imshow('input_image', src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(math.log(2))
print(math.fabs(-300))
print(round(100.98,0))
print(np.arange(1,10, 0.1))
N = 10
print(np.random.rand(N))