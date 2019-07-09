
# 加载库
import cv2
import numpy as np
from matplotlib import pyplot as plt


def image_preporcess(image, target_size, gt_boxes = None):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    '''将背景的颜色进行转化'''

    ih, iw   = target_size#可以得到列表中的两个数
    h,  w, _ = image.shape

    scale  = min(iw/w, ih/h)
    nw, nh = int(scale * w),int(scale * h)
    image_resized = cv2.resize(image, (nw, nh))

    image_paded = np.full(shape=[ih, iw, 3], fill_value = 128.0)
    dw, dh = (iw -nw) // 2, (ih -nh) // 2
    image_paded[dh:nh+dh, dw:nw+dw, :] = image_resized
    image_paded = image_paded / 255.

    if gt_boxes is None:
        return image_paded
    else:
        gt_boxes[:, [0,2]] = gt_boxes[:, [0, 2]] * scale + dw
        gt_boxes[:, [1,3]] = gt_boxes[:, [1, 3]] * scale + dh
        return image_paded, gt_boxes
# 将图像加载为灰度
path = '/home/asus/PycharmProjects/Report_tensorflow_2019.05.15/venv/my_tensorflow_yolov3/data/images/levio.jpeg'
image1 = cv2.imread(path)
image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB).astype(np.float32)
target_size = [416,416]
b = image_preporcess(image,target_size)

print(b[402])

# 展示图像
plt.imshow(image1, cmap='gray')
plt.show()

plt.imshow(image)
plt.show()
