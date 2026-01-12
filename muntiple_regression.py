import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('D:\\anaconda program\\machine_learning\\economic_index.csv')
print(df.head())
df.drop(columns=["Unnamed: 0","year","month"],axis=1,inplace=True)
print(df.head())
print(df.isnull().sum())
import seaborn as sns
sns.pairplot(df)
plt.show()
df.corr()
plt.scatter(df['interest_rate'],df['unemployment_rate'])
plt.xlabel('interest_rate')
plt.ylabel('unemployment_rate')
plt.show()
x=df[['interest_rate','unemployment_rate']]
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
sns.regplot(x='interest_rate',y='index_price',data=df)
plt.show()
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
from sklearn.linear_model import LinearRegression
regression=LinearRegression(n_jobs=-1)
regression.fit(x_train,y_train)
from sklearn.model_selection import cross_val_score
validation_score=cross_val_score(regression,x_train,y_train,cv=5)
np.mean(validation_score)
y_pred=regression.predict(x_test)
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mse)
print("Mean Absolute Error:",mae)
print("Mean Squared Error:",mse)
print("Root Mean Squared Error:",rmse)
r2=r2_score(y_test,y_pred)
print("R2 Score:",r2)