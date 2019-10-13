
a = True
while a:
    b=input('type something')
    if b == '1':
        a = False
    else:
        pass
print("finish run")

'''break'''
a = True
while a:
    b=input('type something')
    if b == '1':
        break
    else:
        pass
    print("still in while")
print("finish run")

'''continue'''

a = True
while a:
    b=input('type something')
    if b == '1':
        continue
    else:
        pass
    print("still in while")
print("finish run")

"""
input somesthing:3
still in while
input somesthing:1  # 没有"still in while"。直接进入下一次循环
input somesthing:4
still in while
input somesthing:
"""