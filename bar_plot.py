import matplotlib.pyplot as plt
categ=['a','s']
price=[3,4]
colo=['teal','red']

plt.pie(price, labels=categ, colors=colo, autopct="%1.1f%%", shadow=True)
plt.show()
