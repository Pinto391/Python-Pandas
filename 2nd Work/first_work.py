#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd 
dataframe= pd.read_csv('F:\WORK\Python Pandas\First Work\weather.csv')


# In[17]:


dataframe


# In[20]:


dataframe['Temperature'].max()


# In[21]:


dataframe['Temperature'].min()


# In[22]:


dataframe['Temperature'].mean()


# In[25]:


dataframe['EST'][dataframe['Events']=='Rain']


# In[27]:


dataframe.fillna(0,inplace=True)
dataframe['WindSpeedMPH'].mean()


# In[29]:


dataframe['EST'] [dataframe['VisibilityMiles']>9]


# In[30]:


dataframe


# In[ ]:




