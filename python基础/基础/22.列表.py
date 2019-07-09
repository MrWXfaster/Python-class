a = [1,2,3,4,51,1]
b= [1,2,3,45,6,7]
c = a+b
print(c)

a.append(0)#把0加到列表的最后一个
a.insert(4,0)
print(a)
a.remove(1)#剪掉第一个出现的数值
print(a)
print(a[-1])#-1是列表中的最后一位值
print(b.index(45))#s索引出出现45的位置
a.sort()#从小到大排序
print(a)