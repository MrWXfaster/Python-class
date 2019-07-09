#tuple list 元祖与列表

a_tuple = (1,2,3,4,5,6)
another_tuple = 1,2,34,566,

a_list = [1,2,344,567,898,]
for content in a_list:
    print(content)

for content in a_tuple:
    print(content)

for index in range(len(a_tuple)):
    print('index',index,"number in list",a_tuple[index])