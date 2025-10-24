import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y1=[3,5,6,6,6,7]
y2=[5,6,7,3,4,2]
plt.subplot(1,2,1)
plt.plot(x,y1,color='green')
plt.subplot(1,2,2)
plt.plot(x,y2,color='green')

plt.show()