import pandas as pd
import os
k=os.getcwd()
print(k)
df=pd.read_csv('D:\\anaconda program\\PandasLibrary\\test.csv')
print(df.isnull().any(axis=1))
print(df.isnull().any(axis=0))
k=df.fillna(0,inplace=True)
print(k)#temproarily changed....notin the parent dataframe
s=df['Age'].fillna(df['Age'].mean())
print(s)
df['filled']=s
print(df)
#renaming columns
k=df.rename(columns={'Age':'Dick'})
print(k)
#changing datatype
s=df['Age_new']=df['Age'].astype(int)
print(s)