
__author_ = "大魔王W"

import numpy as np
import time
import cv2

def biliner_interpolation(input_image, out_image):

    ori_h ,ori_w, ori_dim = input_image.shape
    out_h, out_w  = out_image[1], out_image[0]
    if ori_h == out_h and ori_w == out_w:
        return np.copy(input_image)
    pre_image = np.zeros((out_h,out_w,3), dtype=np.uint8)
    scale_x , scale_y = float(ori_w) / out_w, float(ori_h) / out_h
    for i in range(3):
        for out_y in range(out_h):
            for out_x in range(out_w):
                '''
                通过对输出的尺度,来反向求每个输出点在原图片中的位置.+0.5意义在于构造一个输出图片的点,
                最后减去0.5是找出原始图片中对应的点.相当于是将坐标移动了0.5,原始图片与输出图片集合中心重合.
                '''
                ori_x = (out_x + 0.5) * scale_x - 0.5
                ori_y = (out_y + 0.5) * scale_y + 0.5

                '''
                得到四个在原图中的像素点位置
                '''
                ori_x0 = int(np.floor(ori_x))#取到左上方的点
                ori_x1 = min(ori_x0 + 1, ori_x0 -1)#取往下走一个单位,不可以超过原始图片的的尺度
                ori_y0 = int(np.floor(ori_y))
                ori_y1 = min(ori_y0 + 1, ori_y0 -1)

                '''
                双线性插值
                '''
                temp0 = (ori_x1 - ori_x) * input_image[ori_y0,ori_x0,i]  + (ori_x - ori_x0) * input_image[ori_y0,ori_x1,i]
                temp1 = (ori_x1 - ori_x) * input_image[ori_y1, ori_x0, i] + (ori_x - ori_x0) * input_image[ori_y1, ori_x1, i]
                pre_image[out_y,out_x, i] = int((ori_y1 - ori_y) * temp0 + (ori_y - ori_y0) * temp1)

    return pre_image

if __name__ == "__main__":
    input_image_path = "/home/asus/桌面/person_rd.jpg"
    input_image = cv2.imread(input_image_path)
    cv2.imshow('input_image',input_image)
    start = time.time()
    pre_image = biliner_interpolation(input_image,(450,350))
    print("cost %f time "%(time.time() - start ))
    cv2.imshow("pre_image",pre_image)
    cv2.waitKey(0)
