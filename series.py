#it is 1-d array like object that has powerful data manipulation library
import pandas as pd
data=[1,2,3,4,5]
series=pd.Series(data)
print(series)
data2={'a':1,'b':2}
series2=pd.Series(data2)
print(series2)
#combining the kata and key pair
data3=[2,3,4,5,6]
inde=['a','s','d','f','g']
por=pd.Series(data,index=inde)
print(por)