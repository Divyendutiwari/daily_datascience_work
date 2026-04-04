import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer
# Load the breast cancer dataset
data = load_breast_cancer()
print(data.keys())
df=pd.DataFrame(data.data, columns=data.feature_names)
print(df.head())
print(df.columns)
# Standardize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
# Perform PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
data_pca = pca.fit_transform(scaled_data)
print("Explained variance ratio:", pca.explained_variance_ratio_)
# Create a DataFrame for the PCA results
pca_df = pd.DataFrame(data_pca, columns=['Principal Component 1', 'Principal Component 2'])
print(pca_df.head())
plt.figure(figsize=(10, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=data.target, cmap='plasma')
plt.title('PCA of Breast Cancer Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

