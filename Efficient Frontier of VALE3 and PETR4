#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


assets = ['VALE3.SA', 'PETR4.SA']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start ='2010-01-01')['Adj Close']


# In[5]:


pf_data


# In[30]:


d_return = (pf_data/pf_data.shift(1)-1)*100
print("Daily Stocks Returns \n",d_return,"\n")

print("Adjusted", assets ,"Price \n\n",(pf_data/pf_data.iloc[0]*100).plot(figsize=(20,10)))


# In[33]:


log_return = np.log(pf_data/pf_data.shift(1))
log_return


# In[38]:


print(log_return.mean())
print("\n",log_return.cov()*250)
print("\n",log_return.corr()*250)


# In[40]:


num_assets = len(assets)
num_assets


# In[54]:


weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights


# weighted average of the expected return
# 

# In[55]:


np.sum(weights*log_return.mean())*250


# weighted average of the expected variance

# In[57]:


np.dot(weights.T, np.dot(log_return.cov()*250,weights))


# weighted average of the expected volatility

# In[58]:


np.sqrt(np.dot(weights.T, np.dot(log_return.cov()*250,weights)))


# Creating all the portfolios possible

# In[62]:


pfolio_return = []
pfolio_volatility = []

for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_return.append(np.sum(weights*log_return.mean())*250)
    pfolio_volatility.append(np.sqrt(np.dot(weights.T, np.dot(log_return.cov()*250,weights))))


# In[63]:


pfolio_returns = np.array(pfolio_return)
pfolio_volatilities = np.array(pfolio_volatility)

pfolio_returns
pfolio_volatilities


# In[68]:


pfolio_table = pd.DataFrame({'Return':pfolio_returns,'Volatility': pfolio_volatilities})
pfolio_table


# In[79]:


pfolio_table.plot(x='Volatility',y='Return',kind='scatter',figsize=(20,10),s=5)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')


# In[81]:


min(pfolio_volatilities)


# In[ ]:




