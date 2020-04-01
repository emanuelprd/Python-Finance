#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
from pandas_datareader import data as wp
import matplotlib.pyplot as plt
from scipy.stats import norm


# In[38]:


tickers = ['^BVSP']

my_data = pd.DataFrame()

for t in tickers:
    my_data[t] = wp.DataReader(t, data_source = 'yahoo',start='2020-01-23')['Adj Close']


# In[39]:


print(my_data)
my_data.plot(figsize=(20,10))


# In[67]:


ibov_return = my_data/my_data.shift(1)-1
ibov_return


# In[60]:


log_return = np.log(1+my_data.pct_change())
log_return


# In[74]:


m = log_return.mean()
var = log_return.var()
std = np.sqrt(var)
print(m)
print(var)
print(std)


# In[76]:


drift = m - (0.5*var)
drift


# In[ ]:




