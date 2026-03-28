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
from sklearn.model_selection import RandomizedSearchCV
model = LogisticRegression()
from sklearn.model_selection import StratifiedKFold
cv=StratifiedKFold()
randomcv=RandomizedSearchCV.__init__(estimator=model,param_distributions=,cv=cv,n_jobs=-1)
print(randomcv.best_index_)
print(randomcv.best_score_)