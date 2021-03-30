#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
# csv format
df= pd.read_csv(r'F:\WORK\Python Pandas\3rd Different ways of creationg DataFrame\weather_data.csv')


# In[2]:


df


# In[6]:


# Excel Format
xldf= pd.read_excel(r"F:\WORK\Python Pandas\3rd Different ways of creationg DataFrame\weather_data.xlsx")


# In[7]:


xldf


# In[10]:


# Python Dictonary DataFrame

weater_data={
    'day':['1/1/2017','1/2/2017','1/3/2017'],
    'temperature':[32,35,28],
    'windspeed':[6,7,2],
    'event':['Rain','Sunny','Snow']  
}
df=pd.DataFrame(weater_data)


# In[11]:


df


# In[13]:


# Tiples List

weater_data=[
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df=pd.DataFrame(weater_data, columns=["day","temperature",'windspeed',"event"])


# In[14]:


df


# In[15]:


# List of Dictonary

weater_data=[
   
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'}
    
]


# In[16]:


df=pd.DataFrame(weater_data)
df


# In[ ]:




