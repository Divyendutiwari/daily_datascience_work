import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\\anaconda\\anaconda program\\Algerian_forest_dataset\\forest_data.csv')
df.head()
df.info()
df[df.isnull().sum(axis=1) > 0]
df.loc[:123,"Region"]=0
df.loc[124:246,"Region"]=1
dp=df
dp.head()
print(dp["Region"].value_counts())
dp["Region"]=dp["Region"].astype(int)
print(dp.head())
print(dp.isnull().sum())
dp=dp.dropna().reset_index(drop=True)
print(dp.isnull().sum())
print(dp.columns)
dp.columns=dp.columns.str.strip()
print(dp.info())
dp[['day', 'month', 'year', 'Temperature', 'RH']]=dp[['day','month', 'year', 'Temperature', 'RH']].astype(int)
objects=[feature for feature in dp.columns if dp[feature].dtype == '0']
print(objects)
for i in objects:
    if i != 'Classes':
        dp[i]=dp[i].astype(float)
print(dp.describe())
dp.to_csv('D:\\anaconda\\anaconda program\\Algerian_forest_dataset\\cleaned_forest_data.csv', index=False)
dp_copy=dp.drop(['day', 'month', 'year'], axis=1)
print(dp_copy.head())
dp_copy['Classes']=dp_copy['Classes'].map({'not fire':0, 'fire':1})
print(dp_copy.head())
print(dp_copy['Classes'].value_counts())
percentage=dp_copy['Classes'].value_counts(normalize=True)*100
classlables=['fire', 'not fire']
plt.figure(figsize=(10,5))
plt.pie(percentage,labels=classlables, autopct='%1.1f%%')
plt.title('Distribution of fire and not fire classes')
dp_copy.corr()
sns.heatmap(dp_copy.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
sns.pairplot(dp_copy, hue='Classes')
dp['classes']=np.where(dp['Classes'].str.contains('not fire'), 'not fire', 'fire')
dftemp=dp.loc[dp['Region']==1]
plt.subplots(figsize=(10,5))
sns.set_style('whitegrid')
sns.countplot(x='month', hue='classes', data=dftemp, palette='Set1')
plt.title('Distribution of fire and not fire classes by month in Region 1')
plt.xlabel('Month')
plt.ylabel('Count')
dftemp2=dp.loc[dp['Region']==0]
plt.subplots(figsize=(10,5))
sns.set_style('whitegrid')
sns.countplot(x='month', hue='classes', data=dftemp2, palette='Set1')
plt.title('Distribution of fire and not fire classes by month in Region 0')
plt.xlabel('Month')
plt.ylabel('Count')



