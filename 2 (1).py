#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv


# In[3]:


a=[]
with open("1.csv","r") as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)


# In[4]:


num_att=len(a[0])-1

s=['0']*num_att
g=['?']*num_att
print(s)
print(g)


# In[5]:


temp=[]
for i in range(0,num_att):
    s[i]=a[0][i]
print(s)
print(g)


# In[6]:


for i in range(1,len(a)):
    if a[i][num_att]=='yes':
        for j in range(0,num_att):
            if s[j]!=a[i][j]:
                s[j]='?'
                
        for j in range(0,num_att):
            for k in range(0,len(temp)):
                if s[j]!=temp[k][j] and temp[k][j]!='?':
                    del temp[k]
                    
                    
    if a[i][num_att]=='no':
        for j in range(0,num_att):
            if a[i][j]!=s[j] and s[j]!='?':
                g[j]=s[j]
                temp.append(g)
                g=['?']*num_att
   # print(s)
    
    if len(temp)==0:
        print(g)
    else:
        print(temp)
print(s)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




