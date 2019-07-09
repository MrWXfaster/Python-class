import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize


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
#直线拟合
def f_1(x, A, B):
    return A * x + B

# 三次曲线方程
def f_3(x, A, B, C, D):
    return A * x * x * x + B * x * x + C * x + D
def plot_feasible_region():
    x,y = np.arange(0,1.920,0.001),np.arange(0,1.440,0.001)
    X_H1, Y_H1 = [], []
    X_H2, Y_H2 = [], []
    for x_key in x:
        for y_key in y:
            ky = int(Formula(x_key,y_key))
            if ky ==120:
                '''拟合点'''
                x1,y1 = x_key*1.0,y_key*1.0
                X_H1.append(y1),Y_H1.append(x1)
            elif ky ==240:
                x2, y2 = x_key * 1.0, y_key * 1.0
                X_H2.append(y2), Y_H2.append(x2)
    # 绘制散点
    # plt.scatter(X_H1[:], Y_H1[:], 1, "red")
    # plt.figure(num=None, figsize=None, dpi=300,  edgecolor=None, frameon=True)
    # 直线拟合与绘制数据准备
    X0, Y0 = [], []
    X0.append([X_H1[0], X_H2[0]]), X0.append([X_H1[-1], X_H2[-1]]), Y0.append([Y_H1[0], Y_H2[0]]), Y0.append([Y_H1[-1], Y_H2[-1]])
    print(X0,Y0)
    # 三次曲线拟合与绘制
    A3, B3, C3, D3 = optimize.curve_fit(f_3, X_H1, Y_H1)[0]
    x3 = np.arange(X0[0][0], X0[1][0], 0.001)
    y3 = A3 * x3 * x3 * x3 + B3 * x3 * x3 + C3 * x3 + D3

    # 三次曲线拟合与绘制
    A3, B3, C3, D3 = optimize.curve_fit(f_3, X_H2, Y_H2)[0]
    x4 = np.arange(X0[0][1], X0[1][1], 0.001)
    y4 = A3 * x4 * x4 * x4 + B3 * x4 * x4 + C3 * x4 + D3
    axes = plt.subplot(facecolor='black')
    plt.xlim(0, 1.920)
    plt.xticks(())
    plt.ylim(1.440, 0)
    plt.yticks(())
    for i in range(len(X0)):  # 要连接的两个点的坐标
        axes.plot(X0[i], Y0[i], color='white')
        # plt.scatter(X0[i],Y0[i],color="r")
    axes.plot(x3, y3, 'white')
    axes.plot(x4, y4, 'white')
    # plt.plot(x3, y3, color='red',linewidth =2)
    # plt.plot(x4, y4, color='red', linewidth=2)
    plt.savefig('Image', dpi=300)
    plt.show()

if __name__=="__main__":
    plot_feasible_region()




