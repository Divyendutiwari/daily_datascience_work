import pandas as pd
import os
k=os.getcwd()
print(k)
df=pd.read_csv('D:\\anaconda program\\PandasLibrary\\test.csv')
group=df.groupby('Age')['EmployeeID'].mean()
print(group)