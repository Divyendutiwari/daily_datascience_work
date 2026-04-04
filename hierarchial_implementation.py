import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#iris dataset
from sklearn.datasets import load_iris
iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head())
#standardization
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaled_data=scaler.fit_transform(df)
print(scaled_data[:5])
#PCA
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
pca_data=pca.fit_transform(scaled_data)
print(pca_data[:5])
#pca plot
plt.figure(figsize=(8,6))
sns.scatterplot(x=pca_data[:,0], y=pca_data[:,1], hue=iris.target, palette='Set1')
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Species')
plt.show()
#agglomerative clustering
#constructing dendrogram
import scipy.cluster.hierarchy as sch
plt.figure(figsize=(10,7))
dendrogram=sch.dendrogram(sch.linkage(pca_data, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Euclidean distances')
plt.show()
#fitting hierarchical clustering
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
y_hc=hc.fit_predict(pca_data)
print(y_hc)
#visualizing clusters
plt.figure(figsize=(8,6))
sns.scatterplot(x=pca_data[:,0], y=pca_data[:,1], hue=y_hc, palette='Set2')
plt.title('Hierarchical Clustering of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Cluster')
plt.show()