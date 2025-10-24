import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('li.csv')
sns.barplot(data=df, x="Region", y="Sales", hue="Category")
plt.show()

