#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.neural_network import MLPClassifier


# In[2]:


iris=load_iris()
x=iris.data
y=iris.target

ss=StandardScaler()
x=ss.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)


# In[3]:


classifier=MLPClassifier(activation='logistic',solver='sgd',verbose=True,random_state=1,learning_rate_init=0.5,hidden_layer_sizes=(4,5))
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)


# In[4]:


cm=confusion_matrix(y_test,y_pred)
print('Confusion Matrix:',cm,sep='\n')
acc=accuracy_score(y_test,y_pred)
print('Accuracy:',acc)

