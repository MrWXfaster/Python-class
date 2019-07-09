
def read_class_name(class_file_name):
    '''loads class name from a file'''
    names ={}
    with open(class_file_name,"r") as data:
        for ID,name in enumerate(data):
            names[ID] = name.strip("\n")#strip 同时去掉左右两边的空格
        return names
class_file_name = "/home/asus/PycharmProjects/Report_tensorflow_2019.05.15/venv/my_tensorflow_yolov3/data/classes/coco.names"
print(read_class_name(class_file_name))
