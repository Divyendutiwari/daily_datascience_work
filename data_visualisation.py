import pandas as pd
import matplotlib.pyplot as plt 
df=pd.read_csv('kli.csv')
print(df)
sales=df.groupby('Product Name')['Price'].sum()
print(sales)
sales.plot(kind='pie',shadow=True)
plt.show()