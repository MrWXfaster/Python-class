def get_anchors(anchors_path):
    '''loads the anchors'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = np.array(anchors.split(','),dtype=np.float32)
    print(anchors)
    return anchors.reshape(3,3,2)#变换为三维矩阵，如有-1则代表，我不知道可以分成多少行，但是我的需要是分成3列
                                 #第一个3代表：分为3列，后面3×2代表：分为3行2列的矩阵，顺序为从上到下，从左往右
anchors_path = "/home/asus/PycharmProjects/Report_tensorflow_2019.05.15/venv/my_tensorflow_yolov3/data/anchors/coco_anchors.txt"
a  = get_anchors(anchors_path)
print(a)