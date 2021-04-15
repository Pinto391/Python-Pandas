#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
df=pd.read_csv(r"F:\WORK\Python Pandas\Handle Missing Data by Replace Function\weather_data.csv")
df


# In[5]:


new_df=df.replace(-99999,np.NaN)
new_df


# In[7]:


new_df=df.replace({
    
    'temperature':-99999,
    'windspeed':-99999,
    'event':'0'    
    
},np.NAN)
new_df


# In[17]:


p=pd.read_csv(r"F:\WORK\Python Pandas\Handle Missing Data by Replace Function\new_weather_data.csv")
p 


# In[19]:


# Replace by Regular Expression

p=df.replace({
    'temperature':'[A-Za-z]',
    'windspeed':'[A-Za-z]'
    
    
},'',regex=True)
p 


# In[23]:


p=df.replace({
    'temperature':-99999,
    'windspeed':-99999
},np.NAN)
p 


# In[ ]:





# In[ ]:




