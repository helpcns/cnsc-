#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# In[ ]:


#data =load_iris()


# In[2]:


iris=load_iris()
x=iris.data
y=iris.target


# In[3]:


#x_train,x_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.4,random_state=5)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=5)
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


# In[4]:


print("Acuraccy of KNN\t\t\t\t",accuracy_score(y_pred,y_test))


# In[5]:


pd.DataFrame({'actual':y_test,'predction':y_pred,'correct classification':(y_test==y_pred)})


# In[ ]:





# In[ ]:




