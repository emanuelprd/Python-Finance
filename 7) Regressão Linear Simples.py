#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[75]:


tickers = ['^BVSP','VALE3.SA']

data = pd.DataFrame()

for t in tickers:
        data[t] = wb.DataReader(t, data_source='yahoo', start = '2017-06-26')['Adj Close']


# In[76]:


r_data = data/data.iloc[0]
r_data


# In[77]:


X = r_data['^BVSP']
Y = r_data['VALE3.SA']


# In[152]:


plt.figure(figsize=(12, 8))
plt.scatter(X,Y,s=10,c='black')
plt.title(('Scatter-Plot VALE3 vs BVSP'),fontsize=20)
plt.xlabel('IBOVESPA',fontsize=12)
plt.ylabel('VALE3',fontsize=12)


# In[79]:


X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()


# In[80]:


reg.summary()


# In[82]:


slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)


# In[89]:


print("Slope", round(slope,5))
print("intercept", round(intercept,5))
print("r_value", round(r_value,5))
print("p_value", round(p_value,5))
print("std_err", round(std_err,5))


# In[249]:


line = slope*x+intercept

reg_label = ' y = ' + str(round(slope,5))+'x + '+ str(round(intercept,5))+'\n R² = '+ str(round(r_value,2))+'\n β = '+ str(round(slope,2))

plt.figure(figsize=(12, 8))
plt.plot(x, line,label = reg_label,c='black')
plt.scatter(X,Y,s=10,c='black')
plt.legend(loc='best',fontsize=15)
plt.xlim(0.5,2.5) 
plt.ylim(0.5,3)
plt.title(('Linear Regression VALE3 vs BVSP'),fontsize=20)
plt.xlabel('IBOVESPA',fontsize=12)
plt.ylabel('VALE3',fontsize=12)


# In[ ]:




