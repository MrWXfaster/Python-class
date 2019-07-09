import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_xlabel("x")
ax1.set_xlabel("y")
ax1.set_xlabel("title")

left,bottom,width,height = 0.3,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b')
ax2.set_xlabel("x")
ax2.set_xlabel("y")
ax2.set_xlabel("title inside 1")

plt.axes([.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,'g')#设置y为逆的顺序，即从后往前
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')


plt.show()