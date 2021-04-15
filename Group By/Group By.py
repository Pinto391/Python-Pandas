#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df=pd.read_csv(r"F:\WORK\Python Pandas\Group By\weather_by_cities.csv")
df


# In[3]:


gr=df.groupby('city')
gr 


# In[6]:


for city, city_df in gr:
    print(city)
    print(city_df)


# In[7]:


gr.get_group('paris')


# In[8]:


gr.max()


# In[9]:


gr.describe()


# In[12]:


gr.mean()


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
gr.plot()


# In[ ]:




