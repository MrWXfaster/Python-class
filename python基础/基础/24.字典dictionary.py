a_list=[1,2,3,5,4,5,4]
d = {'apple':1, "pear":2,"orange":3}
d2 ={1:"a",2:"b"}

print(d['apple'])
print(a_list[0])
del d['pear']#删除字典里的元素
print(d)
d["b"] = 20#随便加到任意位置;没有顺序
print(d)
'''内容里面可以是一个列表'''

d = {"apple":[1,2,3],"pear":{1:3,3:"a"},'orange':2}
print(d['pear'][3])