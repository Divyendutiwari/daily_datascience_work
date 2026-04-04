import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
import pandas as pd
import seaborn as sns
x, y = make_blobs(n_samples=1000, centers=3, n_features=2, random_state=0)
print(x.shape)
plt.figure(figsize=(10, 6))
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()
#standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
#train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3,init="k-means++", random_state=0)
kmeans.fit(x_train_scaled)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.figure(figsize=(10, 6))
plt.scatter(x_train_scaled[:, 0], x_train_scaled[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200)
plt.show()
#elbow method
wcss=[]
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(x_train_scaled)
    wcss.append(kmeans.inertia_)
print(wcss)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
y_pred = kmeans.predict(x_test_scaled)
print(y_pred)
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
#knee locator
from kneed import KneeLocator
knee = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
print(knee.knee)
#silhouette score
from sklearn.metrics import silhouette_score
silhouette_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(x_train_scaled)
    score = silhouette_score(x_train_scaled, kmeans.labels_)
    silhouette_scores.append(score)
plt.plot(range(2, 11), silhouette_scores)
plt.title('Silhouette Score')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.show()
