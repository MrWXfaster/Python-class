import cv2
import random
import colorsys
import numpy as np
import tensorflow as tf
from config import cfg

def read_class_name(class_file_name):
    '''
    loads class name from a file
    :param class_file_name: 获取coco.names/voc.names.txt文件
    :return: 字典{}
    '''

    names = {}
    with open(class_file_name,"r") as data:
        for ID, name in enumerate(data):
            names[ID] = name.strip('\n')
        return names

def get_anchors(anchors_path):
    '''
    loads the anchors
    :param anchors_path: 获取anchor_box.txt文件
    :return: 一个shape[3,3,2]的矩阵
    '''

    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = np.array(anchors.split(','),dtype=np.float32)
    print(anchors)
    return anchors.reshape(3,3,2)

def image_preporcess(image, target_size, gt_boxes = None):
    '''
    :param image: 原始图片
    :param target_size: 目标图片大小例如416×416等
    :param gt_boxes: 不知道
    :return: 0-1之间[]矩阵
    '''
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    '''将背景的颜色进行转化'''

    ih, iw   = target_size#将目标尺寸的长h,和宽w分别取出来
    h,  w, _ = image.shape#'''得到原图片的高h,宽w,和维度3取出来'''

    scale  = min(iw/w, ih/h)#取出两个之中小的一个数
    nw, nh = int(scale * w),int(scale * h)#整形得到nw, nh
    image_resized = cv2.resize(image, (nw, nh))#将图片resize为nw, nh

    image_paded = np.full(shape=[ih, iw, 3], fill_value = 128.0)#形成一个shape = ih×iw*3的矩阵，key全为128
    dw, dh = (iw -nw) // 2, (ih -nh) // 2  #得到dw, dh
    image_paded[dh:nh+dh, dw:nw+dw, :] = image_resized #?这个不是很懂
    image_paded = image_paded / 255.  #

    if gt_boxes is None:
        return image_paded
    else:
        gt_boxes[:, [0,2]] = gt_boxes[:, [0, 2]] * scale + dw
        gt_boxes[:, [1,3]] = gt_boxes[:, [1, 3]] * scale + dh
        return image_paded, gt_boxes


def draw_bbox(image, bboxs, classes=read_class_names(cft.YOLO.CLASSES), show_label=True):
    '''
    bboxes :[x_min, y_min, x_max, y_max, cls_id] format coordinates;设置坐标格式
    :param image:
    :param bboxs:
    :param classes:
    :param show_label:
    :return:
    '''
    num_classes = len(classes)#获取长度
    image_h, image_w, _ = image.shape#获取图片的长宽和高以及维度
    hsv_tuples = [(1.0 * x / num_classes, 1., 1.) for x in range(num_classes)]#产生一个list,[(0.0,1.0,1.0),...]
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), colors))

    random.seed(0)
    random.shuffle(colors)#将一个可变序列中的元素打乱
    random.seed(None)

    for i, bbox in enumerate(bboxes):
        coor = np.array(bboxs[:4], dtype=np.int32)
        fontScale = 0.5
        score = bbox[4]
        class_ind = int(bboxs[5])
        bbox_color = colors[class_ind]
        bbox_thick = int(0.6 * (image_h + image_w) / 600)
        c1, c2 = (coor[0], coorr[1]), (coor[2], coor[3])
        cv2.rectangle(image, c1, c2, bbox_color, bbox_thick)

        if show_label:
            bbox_mess = "%s: %.2f" % (classes[class_ind], score)
            t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness = bbox_thick//2)[0]
            cv2.rectangle(image, c1,(c1[0] + t_size[0], c1[1] - t_size[1] -3), bbox_color, -1)
            cv2.putText(image, bbox_mess, (c1[0],c1[1]-2), cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale, (0, 0, 0), bbox_thick//2, lineType=cv2.LINE_AA)

    return image

def bboxs_iou(boxes1, boxes2):

    boxes1 = np.array(boxes1)
    boxes2 = np.array(boxes2)

    boxes1_area = (boxes1[..., 2] - boxes1[..., 0]) * (boxes1[..., 3] - boxes1[..., 1])
    boxes2_area = (boxes2[..., 2] - boxes2[..., 0]) * (boxes2[..., 3] - boxes2[..., 1])

    left_up = np.maximum(boxes1[..., :2], boxes2[..., :2])
    right_down = np.minimum(boxes1[..., 2:], boxes2[..., 2:])

    inter_section = np.maximum(right_down - left_up, 0.0)
    inter_area    = inter_section([..., 0] * inter_section[..., 1])
    union_area    = boxes1_area + boxes2_area - inter_area
    ious          = np.maximum(1.0 * inter_area / union_area, np.finfo(np.float32).eps)

    return ious



