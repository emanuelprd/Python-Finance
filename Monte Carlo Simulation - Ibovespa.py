#!/usr/bin/env python
# coding: utf-8

# Libraries used in this simulation

# In[1]:


import pandas as pd
import numpy as np
from pandas_datareader import data as wp
import matplotlib.pyplot as plt
from scipy.stats import norm


# Extracting my data from yahoo finance

# In[2]:


tickers = ['^BVSP']

my_data = pd.DataFrame()

for t in tickers:
    my_data[t] = wp.DataReader(t, data_source = 'yahoo',start='2019-11-01')['Adj Close']


# In[3]:


print(my_data)
my_data.plot(figsize=(20,10))


# Daily returns formula

# In[4]:


ibov_return = my_data/my_data.shift(1)-1
ibov_return


# Some people says that log returns are better, but it's less intuitive. 

# In[5]:


log_return = np.log(1+my_data.pct_change())
log_return


# I decided the first formula 

# In[59]:


m = ibov_return.mean()
var = ibov_return.var()
std = np.sqrt(var)


# I'm using the Geometric Brownian Motion formula to generate to run the simulation. the formula is: 
# 
# GBM = np.exp(drift + std(x)*norm.ppf(np.random.rand(intervals,iterations)))
# 
# drift = mean(x) - (1/2)*(x)

# In[7]:


drift = m - (0.5*var)
drift


# In[8]:


np.array(drift)


# In[9]:


norm.ppf(0.95)


# In[44]:


intervals = 30
iterations = 1000


# In[45]:


d_return = np.exp(drift.values + std.values*norm.ppf(np.random.rand(intervals,iterations)))
d_return


# In[46]:


d0 = my_data.iloc[-1]
d0


# In[47]:


fprice = np.zeros_like(d_return)
fprice[0] = d0

for n in range(1,intervals):
    fprice[n] = fprice[n-1]*d_return[n]

fprice


# In[48]:


plt.figure(figsize=(20,10))
plt.plot(fprice)


# In[56]:


plt.hist(fprice[-1], bins = 40, histtype = 'step')
plt.show()


# In[50]:


print("Média :",round(fprice.mean(),))
print("Máximo :",round(fprice.max(),))
print("Mínimo :",round(fprice.min(),))
print("Desvio-Padrão :",round(fprice.std(),))


# In[34]:


fprice[-1]


# In[ ]:





# In[ ]:




