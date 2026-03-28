import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
x, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
pd.DataFrame(x).head()
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
penalty_values = ['l1', 'l2', 'elasticnet', 'none']
c_values = [0.01, 0.1, 1, 10, 100]
solver_values = ['liblinear', 'saga']
dict_values = {'penalty': penalty_values, 'C': c_values, 'solver': solver_values}
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
cv=StratifiedKFold()
grid_search = GridSearchCV(estimator=model, param_grid=dict_values, cv=cv, n_jobs=-1)
grid_search.fit(x_train, y_train)
print("Best Hyperparameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
best_model = grid_search.best_estimator_
y_pred = best_model.predict(x_test)
print(accuracy_score(y_pred,y_test))
print(confusion_matrix(y_pred,y_test))