#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


# In[3]:


iris=datasets.load_iris()
x=iris.data
y=iris.target
colormap=np.array(['red','blue','green'])
plt.figure()
plt.subplot(1,3,1)
plt.scatter(x[:,2],x[:,3],c=colormap[y])
plt.title('real')

plt.subplot(1,3,2)
model=KMeans(n_clusters=3,random_state=0).fit(x)
y1 = model.labels_
plt.scatter(x[:,2],x[:,3],c=colormap[y1])
plt.title('kmeans')

plt.subplot(1,3,3)
model1=GaussianMixture(n_components=3,random_state=0).fit(x)
y2=model1.predict(x)
plt.scatter(x[:,2],x[:,3],c=colormap[y2])
plt.title("em")


print('the accuracy score of kmeans:',metrics.accuracy_score(y,y1))
print('the accuracy score of Em :',metrics.accuracy_score(y,y2))


# In[ ]:





# In[ ]:





# In[ ]:




