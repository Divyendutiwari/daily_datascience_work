import numpy as np
data=np.array([45, 23, 67, 12, 89, 34])
print(data>60)
print(data[data>60])
print(np.sort(data))
print(data[(data>=30)&(data<=70)])