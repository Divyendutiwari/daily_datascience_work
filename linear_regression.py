import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(os.getcwd())
print(os.listdir())
df=pd.read_csv('D:\\anaconda program\\machine_learning\\height-weight.csv')
print(df.head())
plt.scatter(df['Weight'],df['Height'])
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Height vs Weight')
print(df.corr())
import seaborn as sns
sns.pairplot(df)
x=df[['Weight']]
type(x)
np.array(x)
print(np.array(x).shape)
y=df['Height']
np.array(y)
print(np.array(y).shape)
x_series=df['Weight']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train.shape)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
from sklearn.linear_model import LinearRegression
regression_model=LinearRegression(n_jobs=-1)
regression_model.fit(x_train_scaled,y_train)
regression_model.intercept_
regression_model.coef_
plt.scatter(x_train_scaled,y_train)
plt.plot(x_train_scaled,regression_model.predict(x_train_scaled),color='red')
y_pred=regression_model.predict(x_test_scaled)
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)
print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}, R2 Score: {score}')
import statsmodels.api as sm
model=sm.OLS(y_train,x_train).fit()
predictions=model.predict(x_test)
print(predictions)
print(model.summary())
k=regression_model.predict(scaler.transform([[72]]))
print(k)