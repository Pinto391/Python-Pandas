#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
df=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\stock_data.csv",skiprows=1)


# In[7]:


df


# In[19]:


# With no header and manually insert header

df=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\stock_data.csv",header=None, names=["tickets","eps","revenue","price","people"])


# In[20]:


df


# In[21]:


# Read spacific rows

df=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\stock_data.csv", nrows=3)


# In[22]:


df


# In[25]:


# Replacing none value

df=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\stock_data.csv", na_values=["not available","n.a."])
df


# In[26]:


# Replacing none value + negative value to NaN

df=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\stock_data.csv", na_values={
    'ticktes':["not available","n.a."],
    'esp':["not available","n.a."],
    'revenue':["not available","n.a.",-1],
    'price':["not available","n.a."],
    'people':["not available","n.a."]
    
})
df


# In[27]:


# Write csv file
df.to_csv('new.csv', index=False)


# In[31]:


# Read from Excel

df=pd.read_excel(r"F:\WORK\py-master\pandas\4_read_write_to_excel\stock_data.xlsx")


# In[32]:


df


# In[45]:


# Replacing none value by function

def convert_na(cell):
    if cell=="not available":
        return None
    return cell
df=pd.read_excel(r"F:\WORK\py-master\pandas\4_read_write_to_excel\stock_data.xlsx", converters={
    'eps':convert_na
    
    
})
df  


# In[46]:


df.to_excel("new.xlsx", sheet_name="stokes")


# In[48]:


# Add two dataframe in a single excel in seperate sheet
df_weather=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\weather_data.csv")

df_stock=pd.read_csv(r"F:\WORK\Python Pandas\Reading & Writing csv & excel file\stock_data.csv")


# In[49]:


with pd.ExcelWriter('weather_stock.xlsx') as writer:
    df_weather.to_excel(writer,sheet_name='weather')
    df_stock.to_excel(writer,sheet_name='stoke')


# In[ ]:




