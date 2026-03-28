import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
y=np.sqrt(10**2-x**2)
y=np.hstack([y,-y])
x=np.hstack([x,x])
x1=np.linspace(-5,5,100)
y1=np.sqrt(5**2-x1**2)
y1=np.hstack([y1,-y1])
x1=np.hstack([x1,-x1])
plt.scatter(x,y,color='blue',label='class1')
plt.scatter(x1,y1,color='red',label='class2')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Support Vector Kernel')
plt.legend()
print(np.vstack([x,y]).T)
import pandas as pd
df1=pd.DataFrame(np.vstack([x,y]).T,columns=['Feature 1','Feature 2'])
df1['Class']=0
df2=pd.DataFrame(np.vstack([x1,y1]).T,columns=['Feature 1','Feature 2'])
df2['Class']=1
df=pd.concat([df1,df2],ignore_index=True)
print(df.head())
x=df.iloc[:,:2]
y=df['Class']
print(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
df['x1_squared']=df['Feature 1']**2
df['x2_squared']=df['Feature 2']**2
df['x1_x2']=df['Feature 1']*df['Feature 2']
x=df[['Feature 1','Feature 2','x1_squared','x2_squared','x1_x2']]
y=df['Class']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
import plotly.express as px
fig = px.scatter_3d(df, x='Feature 1', y='Feature 2', z='x1_squared', color='Class')

