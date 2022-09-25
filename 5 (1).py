#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
df=pd.read_csv('hea.csv')
network = [('age','trestbps'),('age','fbs'), ('sex','trestbps'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'), ('heartdisease','thalach'),('heartdisease','chol')]
model=BayesianNetwork(network)
model.fit(df,estimator=MaximumLikelihoodEstimator)
infer= VariableElimination(model)
print('probability of heartdisease give age=28')
q=infer.query(variables=['heartdisease'],evidence={'age':28})
print(q)


# In[6]:


print('probabiliyt of heatdisease give choloster=100')
q=infer.query(variables=['heartdisease'],evidence={'chol':100})
print(q)


# In[ ]:




