#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta


# In[2]:


end_data = datetime.now()
start_data = datetime.now() - timedelta(days=365*3)


# In[3]:


#Extração de Dados
vale = yf.download('VALE3.SA', start=start_data, end=end_data, progress=False)
petr = yf.download('PETR4.SA', start=start_data, end=end_data, progress=False)

vale


# In[4]:


for stock_df in (vale,petr):
    stock_df['Retorno Normalizado'] = stock_df['Adj Close']/stock_df.iloc[0]['Adj Close']  

vale


# In[5]:


for stock_df, aloc in zip((vale,petr),[.9,.1]):
    stock_df['Alocação'] = stock_df['Retorno Normalizado']*aloc
    
vale


# In[6]:


portfolio = pd.concat([vale['Alocação'],petr['Alocação']],axis=1)
portfolio.plot()


# In[7]:


portfolio['Total'] = portfolio.sum(axis=1)
portfolio['Total'].plot()


# In[8]:


stock_df


# In[10]:


#Extração de Dados
stocks = ["PETR4.SA", "SUZB3.SA", "RANI3.SA"]
proporção = [.25,.45,.35]
p_data = pd.DataFrame()

for s in stocks:
    p_data[s] = yf.download(s, start=start_data, end=end_data, progress=False)['Adj Close']
    
#retorno acumulado
ra_data = p_data/p_data.iloc[0]-1

portfolio = pd.concat([vale['Alocação'],petr['Alocação']],axis=1)

ra_data.plot(figsize=(10,8))
plt.legend(loc='best')


# In[ ]:





# In[ ]:




