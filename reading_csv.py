import pandas as pd
import os
k=os.getcwd()
print(k)
df=pd.read_csv('D:\\anaconda program\\PandasLibrary\\test.csv')
print(df.head(5))
print(df.tail(2))
#accessing the data
print(df['Name'])#in form of the columns
print(df.loc[1])
print(df.iloc[0][1])
print(df.at[1,'Name'])
print(df.iat[2,2])
