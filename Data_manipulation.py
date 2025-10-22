import pandas as pd
import os
k=os.getcwd()
print(k)
df=pd.read_csv('D:\\anaconda program\\PandasLibrary\\test.csv')
df['salary']=[4,5,6,7,8]
print(df)
k=df.drop('salary',axis=1)#temproary deformation
print(k)
#now permanent deformation
df.drop('salary',axis=1,inplace=True)
print(df)
#adding to the age of the employees
df['Age']+=1
print(df)
print(df.describe())
