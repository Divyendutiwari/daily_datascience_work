import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
k=os.getcwd()
print(k)
df=pd.read_excel('D:\\anaconda\\anaconda program\\EDA\\flight_price.xlsx')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
df['Date']=df['Date_of_Journey'].str.split('/').str[0]
df['Month']=df['Date_of_Journey'].str.split('/').str[1]
df['Year']=df['Date_of_Journey'].str.split('/').str[2]
print(df.head())
df['Date']=df['Date'].astype(int)
df['Month']=df['Month'].astype(int)
df['Year']=df['Year'].astype(int)
df.drop('Date_of_Journey',axis=1,inplace=True)
df['Arrival_Time']=df['Arrival_Time'].str.split(' ').str[0]
df['Arrival_Hour']=df['Arrival_Time'].str.split(':').str[0]
df['Arrival_Minute']=df['Arrival_Time'].str.split(':').str[1]
df['Arrival_Hour']=df['Arrival_Hour'].astype(int)
df['Arrival_Minute']=df['Arrival_Minute'].astype(int)
df.drop('Arrival_Time',axis=1,inplace=True)
df['Dep_Hour']=df['Dep_Time'].str.split(':').str[0]
df['Dep_Minute']=df['Dep_Time'].str.split(':').str[1]
df['Dep_Hour']=df['Dep_Hour'].astype(int)
df['Dep_Minute']=df['Dep_Minute'].astype(int)
df.drop('Dep_Time',axis=1,inplace=True)
print(df['Total_Stops'].unique())
df['Total_Stops']=df['Total_Stops'].replace('non-stop','0 stop')
df[df['Total_Stops'].isnull()]
k=df['Total_Stops'].mode()
df['Total_Stops']=df['Total_Stops'].fillna(k)
print(df['Total_Stops'].unique())
print(df['Total_Stops'].isnull())
df['Total_Stops']=df['Total_Stops'].map({'0 stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4,np.nan:1})
print(k)
df.drop('Route',axis=1,inplace=True)
df['duration_hours']=df['Duration'].str.split(' ').str[0].str.split('h').str[0]

df['duration_minutes']=df['Duration'].str.split(' ').str[1].str.split('m').str[0]

df['Airline'].unique()
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder=OneHotEncoder()
encoder.fit_transform(df[['Airline','Source','Destination']])