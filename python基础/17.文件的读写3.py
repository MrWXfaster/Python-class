file = open('my_file.txt',"r")
content = file.readline()#逐行读取
all = file.read()#
print(all)
second_read_line = file.readline()
all_read_line = file.readlines()#一下读取所有行

print(all,content,second_read_line,all_read_line)

