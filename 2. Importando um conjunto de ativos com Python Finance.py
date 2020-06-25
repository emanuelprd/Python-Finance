#!/usr/bin/env python
# coding: utf-8

# Pandas é uma biblioeteca para análise e manipulação de dados, o pandas_datareader é um modulo para importar e ler os dados.

# In[18]:


import pandas as pd
import pandas_datareader as pdr


# Na 1# variable tickers é criado uma lista[] onde cada item é o nome dos ativos conforme rotulado no Yahoo Finance e é criado uma 2# variable que vai receber o classe DataFrame para conseguir colocar os meus dados em um frame. 
# 
# Crio variable t onde t é um item da minha list que vai ser importando da base de dados do Yahoo Finance por meio do pandas_datareader

# In[19]:


tickers = ['VALE3.SA','PETR4.SA']

my_data = pd.DataFrame()

for t in tickers:
    my_data[t] = pdr.DataReader(t, data_source = 'yahoo',start='2000-01-01')['Adj Close']


# In[20]:


my_data


# In[ ]:




