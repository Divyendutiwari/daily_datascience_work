import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv('Travel.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df['Gender'].value_counts())
df['Gender']=df['Gender'].replace('Fe Male','Female')
print(df['Gender'].value_counts())
df['MaritalStatus']=df['MaritalStatus'].replace('Single','Unmarried')
print(df['MaritalStatus'].value_counts())
print(df['TypeofContact'].value_counts())
#checking missing values
features_na=[feature for feature in df.columns if df[feature].isnull().sum()>=1]
print("Features with missing values:")
for feature in features_na:
    print(feature,np.round(df[feature].isnull().mean()*100,4),"% missing values")
print(df[features_na].select_dtypes(exclude=['object']).describe().columns)
df.Age.fillna(df.Age.median(),inplace=True)
df.TypeofContact.fillna(df.TypeofContact.mode()[0],inplace=True)
df.DurationOfPitch.fillna(df.DurationOfPitch.median(),inplace=True)
df.NumberOfFollowups.fillna(df.NumberOfFollowups.mode()[0],inplace=True)
df.PreferredPropertyStar.fillna(df.PreferredPropertyStar.mode()[0],inplace=True)
df.NumberOfTrips.fillna(0,inplace=True)
df.NumberOfChildrenVisiting.fillna(0,inplace=True)
df.MonthlyIncome.fillna(df.MonthlyIncome.median(),inplace=True)
print(df.isnull().sum())
df.drop(['CustomerID'],axis=1,inplace=True)
df['TotalVisits']=df['NumberOfPersonVisiting']+df['NumberOfChildrenVisiting']
df.drop(['NumberOfPersonVisiting','NumberOfChildrenVisiting'],axis=1,inplace=True)
#numeric features
numeric_features=[feature for feature in df.columns if df[feature].dtype!='O']
print("Numeric features:",numeric_features)
#categorical features
categorical_features=[feature for feature in df.columns if df[feature].dtype=='O']
print("Categorical features:",categorical_features)
#discrete features
discrete_features=[feature for feature in numeric_features if len(df[feature].unique())<25]
print("Discrete features:",discrete_features)
#pincode, 20 unique values is a discrete feature
#continuous features
continuous_features=[feature for feature in numeric_features if feature not in discrete_features]
print("Continuous features:",continuous_features)
#train test split
from sklearn.model_selection import train_test_split
X=df.drop('ProdTaken',axis=1)
y=df['ProdTaken']
print(y.value_counts())
#input
print(X.head())
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(x_train.shape)
print(x_test.shape)
#creation of column transformer with 3 types of transformers
cat_features=[feature for feature in x_train.columns if x_train[feature].dtype=='O']
num_features=[feature for feature in x_train.columns if x_train[feature].dtype!='O']
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
numeric_transformer=StandardScaler()
categorical_transformer=OneHotEncoder(drop='first')
preprocessor=ColumnTransformer(
    transformers=[
        ('num',numeric_transformer,num_features),
        ('cat',categorical_transformer,cat_features)
    ])
print(preprocessor)
x_train=preprocessor.fit_transform(x_train)
x_test=preprocessor.transform(x_test)
#machine learning model training/random forest classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,roc_auc_score,roc_curve,precision_score,recall_score,f1_score
models={ 'Decision Tree':DecisionTreeClassifier(random_state=42),
         'Random Forest':RandomForestClassifier(random_state=42),
         'Logistic Regression':LogisticRegression(random_state=42),
         'AdaBoost': AdaBoostClassifier(random_state=42),
         'Gradient Boosting': GradientBoostingClassifier(random_state=42)
    }
for model_name,model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    print(f"Model: {model_name}")
    print("Classification Report:")
    print(classification_report(y_test,y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test,y_pred))
    print("Accuracy Score:",accuracy_score(y_test,y_pred))
    print("Precision Score:",precision_score(y_test,y_pred))
    print("Recall Score:",recall_score(y_test,y_pred))
    print("F1 Score:",f1_score(y_test,y_pred))
for i in range(len(models)):
    model_name=list(models.keys())[i]
    model=list(models.values())[i]
    y_pred=model.predict(x_test)
    y_prob=model.predict_proba(x_test)[:,1]
    fpr,tpr,thresholds=roc_curve(y_test,y_prob)
    plt.figure(figsize=(8,6))
    plt.plot(fpr,tpr,label=f'{model_name} (AUC={roc_auc_score(y_test,y_prob):.2f})')
    plt.plot([0,1],[0,1],'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve - {model_name}')
    plt.show()
    plt.legend(loc='lower right')
    print(f"ROC AUC Score for {model_name}: {roc_auc_score(y_test,y_prob):.2f}")
    model_test_score=model.score(x_test,y_test)
    print(f"Test Score for {model_name}: {model_test_score:.2f}")
    model_train_score=model.score(x_train,y_train)
    print(f"Train Score for {model_name}: {model_train_score:.2f}")
    #hyperparameter tuning of gradient boosting
    
from sklearn.model_selection import GridSearchCV
param_grid={
    'n_estimators':[100,200],
    'learning_rate':[0.01,0.1],
    'max_depth':[3,5]
}
grid_search=GridSearchCV(estimator=GradientBoostingClassifier(random_state=42),param_grid=param_grid,cv=5,n_jobs=-1)
grid_search.fit(x_train,y_train)
print("Best Hyperparameters:",grid_search.best_params_)
print("accuracy score of best model:",grid_search.best_score_)
best_gb=grid_search.best_estimator_
y_pred=best_gb.predict(x_test)
#roc curve for best gradient boosting model
y_prob=best_gb.predict_proba(x_test)[:,1]
fpr,tpr,thresholds=roc_curve(y_test,y_prob)
plt.figure(figsize=(8,6))
plt.plot(fpr,tpr,label=f'Best Gradient Boosting (AUC={roc_auc_score(y_test,y_prob):.2f})')
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Best Gradient Boosting')
plt.legend(loc='lower right')
plt.show()
print("Classification Report for Best Gradient Boosting:")
print(classification_report(y_test,y_pred))
print("Confusion Matrix for Best Gradient Boosting:")
print(confusion_matrix(y_test,y_pred))
print("Accuracy Score for Best Gradient Boosting:",accuracy_score(y_test,y_pred))
