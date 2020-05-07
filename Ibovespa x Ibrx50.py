#!/usr/bin/env python
# coding: utf-8

# O objetivo deste estudo irá analisar a diferença de retorno e risco entre o Ibovespa o IBrX-50.

# In[43]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats.mstats import gmean  


# In[44]:


tickers = ['^BVSP','^IBX50']

my_data = pd.DataFrame()

for t in tickers: 
    my_data[t] = wb.DataReader(t,data_source='yahoo', start = '2016-01-01')['Adj Close']


# In[45]:


my_data


# In[46]:


#n_returns = normalized returns

n_returns = ((my_data/my_data.iloc[0])-1)
n_returns


# In[47]:


n_returns.plot(figsize=(20,10))


# In[96]:


dlog_return = np.log(my_data / my_data.shift(1))
dlog_return.plot(figsize=(20,10))


# In[95]:


print(dlog_return['^BVSP'].mean()*252*100)
print(dlog_return['^IBX50'].mean()*252*100)


# In[94]:


print(dlog_return['^BVSP'].std()*100)
print(dlog_return['^IBX50'].std()*100)

