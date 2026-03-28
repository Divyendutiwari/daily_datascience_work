import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
x, y = make_classification(n_samples=1000,n_classes=2, random_state=42)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
dummy_prob=[0 for _ in range(len(y_test))]
print("Dummy AUC:", roc_auc_score(y_test, dummy_prob))
print(dummy_prob)
model = LogisticRegression()
model.fit(x_train, y_train)
y_prob = model.predict_proba(x_test)[:, 1]
dumm_model_auc = roc_auc_score(y_test, dummy_prob)
model_auc = roc_auc_score(y_test, y_prob)
print("Dummy Model AUC:", dumm_model_auc)
print("Logistic Regression Model AUC:", model_auc)
fig=plt.figure(figsize=(8, 6))
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label='Logistic Regression Model')
plt.plot([0, 1], [0, 1], 'k--', label='Random Guessing')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

