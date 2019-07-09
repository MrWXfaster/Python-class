'''
Tqdm 是一个快速，可扩展的Python进度条，可以在 Python 长循环中添加一个进度提示信息，
用户只需要封装任意的迭代器 tqdm(iterator)。
'''
from tqdm import tqdm
#方式一
for i in tqdm(range(1000)):
    pass

for char in tqdm(['a','b','c','d']):
    #do something
    pass

#方式二
'''trange(i) 是 tqdm(range(i)) 的简单写法'''
from tqdm import trange
for i in trange(1000):
    pass
trainset = [1,2,3,43,4,5,5]
pbar = tqdm(trainset)