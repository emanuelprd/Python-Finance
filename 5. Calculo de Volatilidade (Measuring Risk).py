#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[87]:


tickers = ['ITUB4.SA','VVAR3.SA']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start = '2019-01-26')['Adj Close']


# In[88]:


sec_rn = sec_data/sec_data.iloc[0]
sec_rn.plot(figsize = (10,5))


# Para o calculo da volatilidade (standard deviation) será utilizado o log-retorno pois já trazer os dados na base preferível ![image.png](attachment:image.png)

# In[89]:


sec_r = np.log(sec_data/sec_data.shift(1))
sec_r


# In[90]:


sec_r.mean()*252


# Para o calculo da volatilidade é utilizada a respectiva formula ![image.png](attachment:image.png)

# In[94]:


sec_r.std()*(252**0.5)


# In[92]:





# In[ ]:




