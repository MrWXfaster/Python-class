import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize
T = 1.85*10**(-4)
n = 12
E = 1.67*10**11
F = 0.325
G = 0.85*10**(-3)
d = 2*F/G


def Formula(r1, r2):
    Molecule = r1**3*T*E                              #分子
    down1 = 3*math.pi*((r1 + r2)**3)/8                #分母部分1
    down2 = 4 + 6*((r1 + r2)**2) + 3*math.pi*(r1+r2)   #分母部分2
    Demominator = 4*n*(down1 +down2)
    ky = Molecule/Demominator
    return ky
def Formula1(r1,r2):
    Molecule = 2*n*(16*F+12*F*math.pi*(r1+r2)+24*F*((r1+r2)**2)+3/2*math.pi*F*((r1+r2)**3))
    Demoinator = E*r1**3*T
    ky1 = Molecule/Demoinator
    return ky1


def Formula2(r1,r2):
    c_m = math.fabs(r2/(2*r1+r2))
    c_m = 1 if c_m ==0 else c_m
    c = -(r1/(math.log(c_m)))
    b_up = E*c*T*(2*c*r1-r1*r2-r1**2)
    b_down = d + E*T*(2*c*r1-r1*r2-r1**2)
    b = b_up/b_down
    a = c - r2/2
    Molecule = E*a*(b-c)
    Demoinator = b*(c-a)
    ky2 =Molecule / Demoinator
    return ky2


#直线拟合
def f_1(x, A, B):
    return A * x + B

# 三次曲线方程
def f_3(x, A, B, C, D):
    return A * x * x * x + B * x * x + C * x + D
def plot_feasible_region():
    x,y = np.arange(0.001,0.64,0.001),np.arange(0.001,0.68,0.001)
    X_H1, Y_H1 = [], []
    X_H2, Y_H2 = [], []
    X_H3, Y_H3 = [], []
    X_H4, Y_H4 = [], []
    X_H5, Y_H5 = [], []
    X_H6, Y_H6 = [], []
    for x_key in x:
        for y_key in y:
            ky = int(Formula(x_key,y_key))
            ky1 = round(Formula1(x_key,y_key))
            ky2 = round(Formula2(x_key,y_key)/(10**6),0)
            if ky ==300:
                '''拟合点'''
                x1,y1 = x_key*1.0,y_key*1.0
                X_H1.append(y1),Y_H1.append(x1)
            elif ky ==350:
                x2, y2 = x_key * 1.0, y_key * 1.0
                X_H2.append(y2), Y_H2.append(x2)
            elif ky>=300 and ky <=350:
                x6, y6 = x_key*1.0, y_key * 1.0
                X_H6.append(y6),Y_H6.append(x6)

            elif ky1 >= 0.001:
                x21,y21 = x_key*1.0,y_key*1.0
                X_H3.append(y21),Y_H3.append(x21)
            elif ky2 == 336:
                x31, y31 = x_key * 1.0, y_key * 1.0
                X_H4.append(y31), Y_H4.append(x31)
            elif ky2 >=336:
                x41, y41 = x_key * 1.0, y_key * 1.0
                X_H5.append(y41), Y_H5.append(x41)
    # 直线拟合与绘制数据准备
    X0, Y0 = [], []
    X0.append([X_H1[0], X_H2[0]]), X0.append([X_H1[-1], X_H2[-1]]), Y0.append([Y_H1[0], Y_H2[0]]), Y0.append([Y_H1[-1], Y_H2[-1]])
    print(X0,Y0)
    # 三次曲线拟合与绘制ky ==300
    A3, B3, C3, D3 = optimize.curve_fit(f_3, X_H1, Y_H1)[0]
    x3 = np.arange(X0[0][0], X0[1][0], 0.001)
    y3 = A3 * x3 * x3 * x3 + B3 * x3 * x3 + C3 * x3 + D3

    # 三次曲线拟合与绘制ky ==350
    A4, B4, C4, D4 = optimize.curve_fit(f_3, X_H2, Y_H2)[0]
    x4 = np.arange(X0[0][1], X0[1][1], 0.001)
    y4 = A4 * x4 * x4 * x4 + B4 * x4 * x4 + C4 * x4 + D4

    # # 三次曲线拟合与绘制ky1 ==0.001
    # A5, B5, C5, D5 = optimize.curve_fit(f_3, X_H3, Y_H3)[0]
    # x5 = np.arange(X0[0][2], X0[1][2], 0.001)
    # y5 = A5 * x5 * x5 * x5 + B5 * x5 * x5 + C5 * x5 + D5
    #
    # 三次曲线拟合与绘制ky2 ==0.001
    A6, B6, C6, D6 = optimize.curve_fit(f_3, X_H4, Y_H4)[0]
    x6 = np.arange(X_H4[-1], X_H4[0], 0.001)
    y6 = A6 * x6 * x6 * x6 + B6 * x6 * x6 + C6 * x6 + D6
    axes = plt.subplot(facecolor='black')
    ax = plt.gca()
    '''ax.spines表示为设置脊梁，即四个边框'''
    ax.spines["right"].set_color('black')
    ax.spines["top"].set_color('black')
    ax.spines["left"].set_color('black')
    ax.spines["bottom"].set_color('black')
    plt.xlim(0, 0.64)
    plt.xticks(())
    plt.ylim(0.48, 0)
    plt.yticks(())
    # for i in range(len(X0)):  # 要连接的两个点的坐标
    #     axes.plot(X0[i], Y0[i], color='white')
        # plt.scatter(X0[i],Y0[i],color="r")
    # axes.plot(x3, y3, 'white')
    # axes.plot(x4, y4, 'white')
    # axes.plot(x5, y5, 'white')
    #axes.plot(x6, y6, 'white')
    plt.scatter(X_H5, Y_H5)
    plt.scatter(X_H3, Y_H3)
    plt.scatter(X_H6, Y_H6)
    # plt.plot(x3, y3, color='red',linewidth =2)
    # plt.plot(x4, y4, color='red', linewidth=2)
    plt.savefig('Image', dpi=300)
    plt.show()

if __name__=="__main__":
    plot_feasible_region()





