import numpy as np
def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)
result = softmax([10,2,3,4,56])
print(result)
'''输入值太大会导致溢出'''
#改进 加一个常数使得输出均在0附近

def softmax_plus(x):
    shift_x = x - np.max(x)
    exp_x = np.exp(shift_x)
    return exp_x / np.sum(exp_x)
result1 = softmax_plus([10,20,30,20])
print(result1)