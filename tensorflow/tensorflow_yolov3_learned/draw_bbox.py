import cv2
import random
import colorsys
import numpy as np
import tensorflow as tf
import colorsys
# hsv_tuples = [(1.0 * x / 80, 1., 1.) for x in range(80)]
# print(hsv_tuples)
# colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
# print(colors)
# colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), colors))
# print(colors)
# random.seed(0)
# random.shuffle(colors)
# print(colors)
# random.seed(None)

# g = lambda x, y: x * y
# print(g(3,4))

# def draw_bbox(image, bboxes, classes=read_class_names(cfg.YOLO.CLASSES), show_label=True):
#     """
#     bboxes: [x_min, y_min, x_max, y_max, cls_id] format coordinates.
#
#     """
#
#     num_classes = len(classes)
#     image_h, image_w, _ = image.shape
#     hsv_tuples = [(1.0 * x / num_classes, 1., 1.) for x in range(num_classes)]
#     colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
#     colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), colors))
#
#     random.seed(0)
#     random.shuffle(colors)
#     random.seed(None)
#
#     for i, bbox in enumerate(bboxes):
#         coor = np.array(bbox[:4], dtype=np.int32)
#         fontScale = 0.5
#         score = bbox[4]
#         class_ind = int(bbox[5])
#         bbox_color = colors[class_ind]
#         bbox_thick = int(0.6 * (image_h + image_w) / 600)
#         c1, c2 = (coor[0], coor[1]), (coor[2], coor[3])
#         cv2.rectangle(image, c1, c2, bbox_color, bbox_thick)
#
#         if show_label:
#             bbox_mess = '%s: %.2f' % (classes[class_ind], score)
#             t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick//2)[0]
#             cv2.rectangle(image, c1, (c1[0] + t_size[0], c1[1] - t_size[1] - 3), bbox_color, -1)  # filled
#
#             cv2.putText(image, bbox_mess, (c1[0], c1[1]-2), cv2.FONT_HERSHEY_SIMPLEX,
#                         fontScale, (0, 0, 0), bbox_thick//2, lineType=cv2.LINE_AA)
#
#     return image
# bboxes = [7, 90, 122, 567, 0]
# for i, bbox in enumerate(bboxes):
#     print(i,bbox)
#     coor = np.array(bbox[:4], dtype=np.int32)
#     print(coor)
#     fontScale = 0.5
#     score = bbox[4]
#     class_ind = int(bbox[5])
#     bbox_color = colors[class_ind]
#     bbox_thick = int(0.6 * (image_h + image_w) / 600)
#     c1, c2 = (coor[0], coor[1]), (coor[2], coor[3])
#     cv2.rectangle(image, c1, c2, bbox_color, bbox_thick)
i = 1.655
print("%.2f"%(i))

arr=np.array([[1],[2]])
list = []
tuple = (1,2,3,4,5,6,7,7,8,9)
for i in range(10):
    list.append(i)
# a = np.array(1)
# print(arr,a)
# b = np.array[..., 2]

c = list[ : 3]
d = [..., 3]
print(c)