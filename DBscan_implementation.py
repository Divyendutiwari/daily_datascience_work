import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons
x,y=make_moons(n_samples=250,noise=0.05)
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()
#standardization
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
from sklearn.cluster import DBSCAN
dbscan=DBSCAN(eps=0.3,min_samples=5)
dbscan.fit(x_scaled)
labels=dbscan.labels_
plt.scatter(x_scaled[:,0],x_scaled[:,1],c=labels)
plt.show()