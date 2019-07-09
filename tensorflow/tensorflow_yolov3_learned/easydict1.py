'''
在这个里面，和[]的作用是一样的
'''

from easydict import EasyDict as edict

temp = edict()
temp.train = edict()
temp.test = edict()
temp.train.val = 1.0
temp.test.val = 1.0
'''
调用
'''
temp.train
temp.test
temp.train.val
temp.test.val

'''
在深度学习中往往利用 easydict 建立一个全局的变量
'''
from easydict import EasyDict as edict
config = edict()#创建一个字典，key是Train,值是{}
config.TRAIN = edict()
config.TEST = edict()
# config.TRAIN = {} # 这个和上面的那句话是等价的，相当于创建一个字典的key

config.TRAIN.batch_size = 25# 然后在里面写值,表示Train里面的value也是一个字典
config.TRAIN.early_stopping_num = 10
config.TRAIN.lr = 0.0001
print(config)



