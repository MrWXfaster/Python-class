text = "This is first test.\n this is next line.\n this is last line"

my_file = open('my_file.txt',"w")#w代表write
my_file.write(text)
my_file.close()
'''
创建文件，写入文件
'''