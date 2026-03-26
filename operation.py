import pandas as pd      
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\\anaconda\\anaconda program\\Algerian_forest_dataset\\cleaned_forest_data.csv')
print(df.head())
print(df.info())
print(df.columns)
df.drop(['day', 'month', 'year'], axis=1, inplace=True)
print(df.head())
df['Classes']=df['Classes'].map({'not fire':0, 'fire':1})
print(df.head())
print(df['Classes'].value_counts())
x=df.drop('FWI', axis=1)
y=df['FWI']
x.head()
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
plt.figure(figsize=(10,5))
corr=x_train.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
def correlation(dataset, threshold):
    col_corr=set()
    corr_matrix=dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i,j]) > threshold:
                colname=corr_matrix.columns[i]
                col_corr.add(colname)
    return col_corr
correlation(x_train, 0.8)
x_train.drop(correlation(x_train, 0.8), axis=1, inplace=True)
x_test.drop(correlation(x_test, 0.8), axis=1, inplace=True)
print(x_train.head())
print(x_test.head())
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
plt.subplots(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=x_train)
plt.title('Boxplot of x_train before scaling')
plt.subplot(1,2,2)
sns.boxplot(data=x_train_scaled)
plt.title('Boxplot of x_train after scaling')
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
linreg=LinearRegression()
linreg.fit(x_train_scaled, y_train)
y_pred=linreg.predict(x_test_scaled)
mse=mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
#lasso regression
from sklearn.linear_model import Lasso
lasso=Lasso(alpha=0.1)
lasso.fit(x_train_scaled, y_train)
y_pred_lasso=lasso.predict(x_test_scaled)
mse_lasso=mean_squared_error(y_test, y_pred_lasso)
r2_lasso=r2_score(y_test, y_pred_lasso)
print(f'Lasso Mean Squared Error: {mse_lasso}')
print(f'Lasso R-squared: {r2_lasso}')
plt.scatter(y_test, y_pred, color='blue', label='Linear Regression')
plt.scatter(y_test, y_pred_lasso, color='red', label='Lasso Regression')
plt.xlabel('Actual FWI')
plt.ylabel('Predicted FWI')
plt.title('Comparison of Linear and Lasso Regression')
#cross validation
from sklearn.model_selection import cross_val_score
lasso_cv_scores=cross_val_score(lasso, x_train_scaled, y_train, cv=5, scoring='neg_mean_squared_error')
lasso_cv_mse=-lasso_cv_scores
print(f'Lasso Cross-Validated MSE: {lasso_cv_mse.mean()}')
print(f'Lasso Cross-Validated R-squared: {cross_val_score(lasso, x_train_scaled, y_train, cv=5, scoring="r2").mean()}')
