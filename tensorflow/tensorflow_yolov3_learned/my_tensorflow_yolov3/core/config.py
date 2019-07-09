from easydict import EasyDict as edict

__C                         =edict()
cfg                         =edict()
##YOLO options
__C.YOLO                    =edict()
#set the class name
__C.YOLO.CLASSES            ="./data/classes/coco.names"
__C.YOLO.ANCHORS            =""
__C.YOLO.MOVING_AVG_DECAY   =0.9995
__C.YOLO.STRIDES            =[8,16,32]
__C.YOLO.ANCHORS_PER_SCALE  =3
__C.YOLO.IOU_LOSS_THRESH    =0.5
__C.YOLO.UPSAMPLE_METHOD    =""
__C.YOLO.ORIGINAL_WEIGHTE   =""
__C.YOLO.DEMO_WEIGHT        =""

#train options
__C.TRAIN                   =edict()
__C.TRAIN.ANNOT_PATH        =""
__C.TRAIN.BATCH_SIZE        =2
__C.TRAIN.INPUT_SIZE        =[320,352,384,416,448,480,512,544,578,608]
__C.TRAIN.DATA_AUG          =True
__C.TRAIN.LEARN_RATE_INIT   =1e-4
__C.TRAIN.LEARN_RATE_END    =1e-6
__C.TRAIN.WAMUP_EPOCHS      =5
__C.TRAIN.EPOCHS            =50

# TEST options
__C.TEST                        = edict()

__C.TEST.ANNOT_PATH             = "./data/dataset/voc_test.txt"
__C.TEST.BATCH_SIZE             = 2
__C.TEST.INPUT_SIZE             = 544
__C.TEST.DATA_AUG               = False
__C.TEST.WRITE_IMAGE            = True
__C.TEST.WRITE_IMAGE_PATH       = "./data/detection/"
__C.TEST.WRITE_IMAGE_SHOW_LABEL = False
__C.TEST.WEIGHT_FILE            = "./checkpoint/yolov3_test_loss=9.2099.ckpt-5"
__C.TEST.SHOW_LABEL             = False
__C.TEST.SCORE_THRESHOLD        = 0.3
__C.TEST.IOU_THRESHOLD          = 0.5

# print(__C)




