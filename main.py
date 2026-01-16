import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\\anaconda program\\Algerian_forest_dataset\\forest_data.csv')
print(df.info())
#data cleaning
df=df.dropna().reset_index()
print(df.head())
print(df.isnull().sum())
df.loc[:122,"region"]=0
df.loc[122:,"region"]=1
d=df


print(d.head())
print(d.tail())
d.drop(122).reset_index(inplace=True,drop=True)
print(d.columns)
#space fixing in the columns
d.columns=d.columns.str.strip()
print(d.info())
d.reset_index(inplace=True,drop=True)
print(d.columns)
#change required columns to integer type
objects=[features for features in d.columns if d[features].dtype=='0']
for i in objects:
    if i!='classes': 
        d[i]=d[i].astype('float')
for i in objects:
    if i=='Classes': 
        d[i]=d[i].astype('string')
d.describe()
d.head()
d.to_csv('D:\\anaconda program\\Algerian_forest_dataset\\cleaned_forest_data.csv',index=False)
df_copy=d.drop(['day','month','year'],axis=1)
print(df_copy.head())
print(df_copy.columns)
print(df_copy['Classes'].value_counts())
#df_copy['Classes']=df_copy['Classes'].replace({'fire':1,'not fire':0})
#dont use this cause of the spaces that are found in the parameteric values
df_copy['Classes']=np.where(df_copy['Classes'].str.contains('not fire'),0,1)
print(df_copy['Classes'].value_counts())
sns.histplot(data=df_copy,x='Classes',y='FFMC',hue='region',multiple='dodge')
plt.show()
df_copy['Classes'].value_counts(normalize=True)*100
classlabels=["fire","not fire"]
plt.figure(figsize=(6,6))
plt.pie(df_copy['Classes'].value_counts(normalize=True)*100,labels=classlabels,autopct='%1.1f%%')
plt.title('Distribution of Fire and Not Fire Cases')
plt.show()
sns.boxplot(df['FWI'])
plt.title('Boxplot of FWI')
plt.show()
dftemp=df.loc[df['region']==1]
plt.subplots(figsize=(12,8))
plt.show()
sns.set_style('darkgrid')
sns.countplot(x='month',hue='Classes',data=dftemp)
plt.ylabel('no. of fires',weight='bold',size=12)
plt.xlabel('month',weight='bold',size=12)
plt.title('Forest Fires in Region 1',weight='bold',size=16)
plt.show()
print(df_copy.head())
print(df_copy['Classes'].value_counts())
x=df.drop('FWI',axis=1)
y=df['FWI']
print(x.head())
print(y.head())
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
plt.figure(figsize=(10,6))
corr=x_train.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
def correlation(dataset,threshold):
    col_corr=set()
    corr_matrix=dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i,j])>threshold:
                colname=corr_matrix.columns[i]
                col_corr.add(colname)
    return col_corr
corr_features=correlation(x_train,0.8)
x_train.drop(corr_features,axis=1,inplace=True)
x_test.drop(corr_features,axis=1,inplace=True)
print(x_train.shape,x_test.shape)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
plt.subplots(figsize=(12,8))
# Model Building
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
linreg=LinearRegression()
linreg.fit(x_train_scaled,y_train)
y_pred=linreg.predict(x_test_scaled)
mse=mean_squared_error(y_test,y_pred)
print("Mean Squared Error:",mse)
print("Root Mean Squared Error:",np.sqrt(mse))
#similarly we could do the other types of the regression models like ridge,lasso,elasticnet etc.
from sklearn.linear_model import LassoCV
lassocv=LassoCV()
lassocv.fit(x_train_scaled,y_train)
lassocv.predict(x_test_scaled)
lassocv.alpha_
plt.scatter(y_test,y_pred)
plt.xlabel('Actual FWI')
plt.ylabel('Predicted FWI')
plt.title('Actual vs Predicted FWI')
plt.show()
#just like that we could do other cross validation techniques also