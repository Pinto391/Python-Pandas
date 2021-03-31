#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd 

# Conver to date type

df= pd.read_csv(r"F:\WORK\Python Pandas\Handle Missing Data\weather_data.csv", parse_dates=["day"])
df


# In[3]:


new_df=df.fillna(value=0)
new_df


# In[4]:


new_df =df.fillna(
{
    'temperature':0,
    'windspeed':0,
    'event': "No Event"
})
new_df


# In[5]:


# Fill na vlaue to previous value
new_df=df.fillna(method='ffill')
new_df


# In[6]:


# Fill na vlaue to backward value
new_df=df.fillna(method='bfill')
new_df


# In[7]:


# Interpolate "best way to fill missing value"

new_df=df.interpolate()
new_df


# In[13]:


# Interpolate "best way to fill missing value using time"
df.set_index('day',inplace=True)
new_df=df.interpolate( method='time')
new_df


# In[14]:


# Drop Na Values
new_df=df.dropna()
new_df


# In[15]:


# Drop Na Values when all values are NaN (how='all'/ thresh=1/2/3...)

new_df=df.dropna(how='all')
new_df


# In[17]:


# Insert time range
dt=pd.date_range("01-01-2017","01-11-2017")
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)
df


# In[ ]:




