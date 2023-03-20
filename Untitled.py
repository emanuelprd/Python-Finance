#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta


# In[2]:


end_data = datetime.now()
start_data = datetime.now() - timedelta(days=365*3)


# In[3]:


#Extração de Dados
stocks = ["KLBN4.SA", "SUZB3.SA", "RANI3.SA"]
p_data = pd.DataFrame()

for s in stocks:
    p_data[s] = yf.download(s, start=start_data, end=end_data, progress=False)['Adj Close']

#retorno acumulado
ra_data = p_data/p_data.iloc[0]-1

ra_data.plot(figsize=(10,8))
plt.legend(loc='best')


# In[ ]:




