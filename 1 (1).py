#!/usr/bin/env python
# coding: utf-8

# In[18]:


import csv
a=[]
with open('1.csv') as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)


# In[19]:


num_att=len(a[0])-1
h=['0']*num_att
print(h)


# In[21]:


for i in range(0,len(a)):
    if a[i][num_att]=='yes':
        for j in range(0,num_att):
            if h[j]=='0' or h[j]==a[i][j]:
                h[j]=a[i][j]
            else:
                h[j]='?'
        print(h)
    if a[i][num_att]=='no':
        print(h)
    


# In[22]:


print(h)


# In[ ]:





# In[ ]:




