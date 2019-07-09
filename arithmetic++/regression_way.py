import numpy as np
import math
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt

def Formula(r1, r2):
    T = 1.85*10**(-4)
    n = 7
    E = 1.67*10**11
    Molecule = r1**3*T*E                              #分子
    down1 = 3*math.pi*((r1 + r2)**3)/8                #分母部分1
    down2 = 4 + 6*((r1 + r2)**2) + 3*math.pi*(r1+r2)   #分母部分2
    Demominator = 4*n*(down1 +down2)
    ky = Molecule/Demominator
    return ky

def add_layer(inputs, in_size, out_size, activation_function=True):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs


def plot_test():
    sess = tf.Session()
    P_Z = np.ones((1000, 1000, 3))
    x = tf.tile(tf.range(1000, dtype=tf.int32)[:, tf.newaxis], [1, 1000])
    y = tf.tile(tf.range(1000, dtype=tf.int32)[tf.newaxis, :], [1000, 1])
    x, y = x / 1000, y / 1000
    xy_grid = tf.concat([x[:, :, tf.newaxis], y[:, :, tf.newaxis]], axis=-1)
    xy_grid = tf.cast(xy_grid, tf.float32)
    xy_grid = sess.run(xy_grid)
    X_H1, Y_H1 = [], []
    X_H2, Y_H2 = [], []
    plt.figure()
    for i in xy_grid:  # 先取列
        for list in i:  # 再取行
            Variables = np.array(list)
            x, y = Variables[0], Variables[1]
            ky = int(Formula(x, y))
            if ky == 120:
                '''拟合点'''
                x1, y1 = x * 1000, y * 1000
                X_H1.append(y1), Y_H1.append(x1)
            elif ky == 240:
                x2, y2 = x * 1000, y * 1000
                X_H2.append(y2), Y_H2.append(x2)
    X_H,Y_H = np.array(X_H1 + X_H2),np.array(Y_H1 + Y_H2)
    # data for training
    x_data = X_H[:, np.newaxis]
    y_data = Y_H[:, np.newaxis]
    # data holder
    xs = tf.placeholder(tf.float32, [None, 1])
    ys = tf.placeholder(tf.float32, [None, 1])
    # networks
    l_1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
    prediction = add_layer(l_1, 10, 1, activation_function=None)
    # loss
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    # train method
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
    # initialization
    init = tf.initialize_all_variables()
    # Session
    sess = tf.Session()
    sess.run(init)
    # visulization
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x_data, y_data)
    plt.ion()
    plt.show()

    for i in range(10000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 500 == 0:
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value = sess.run(prediction, feed_dict={xs: x_data})
            lines = ax.plot(x_data, prediction_value, 'r-', lw=1)

            plt.pause(0.8)

    # plt.xlim(0, 1000)
    # plt.ylim(0, 1000)
    # plt.plot(x3, y3, color='red', linewidth=1.0)
    # plt.plot(x4, y4, color='red', linewidth=1.0)
    # plt.savefig('Figure5', dpi=300)
    # plt.show()


if __name__ == '__main__':
    curve1 = plot_test()

    
