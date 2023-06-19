#!/usr/bin/env python
# coding: utf-8

# In[1]:

pip install yfinance

# In[7]:

#importação das libraries
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pandas.plotting import scatter_matrix

# In[3]:

#Definição dos períodos
end_data = datetime.now()
start_data = datetime.now() - timedelta(days=365*3)

# In[4]:

#Extração de Dados
stocks = ["KLBN4.SA", "SUZB3.SA", "RANI3.SA"]
p_data = pd.DataFrame()

for s in stocks:
    p_data[s] = yf.download(s, start=start_data, end=end_data, progress=False)['Adj Close']

#retorno acumulado
ra_data = p_data/p_data.iloc[0]-1

ra_data.plot(figsize=(10,8))
plt.legend(loc='best')

# In[5]:

round(ra_data.iloc[-1]*100,2)

# In[8]:

#Retorno diário
rd_data = np.log(p_data/p_data.shift(1))
rd_data['KLBN4.SA'].plot(figsize=(10,8))
plt.legend(['KLBN4.SA'])
rd_data.tail()

# In[9]:

#Retorno diário
rd_data2 = p_data/p_data.shift(1)-1
rd_data2['KLBN4.SA'].plot(figsize=(10,8))
rd_data2.tail()

# In[10]:

rd_data.plot(kind='kde')

# In[11]:

#Box Plot
Box_df = pd.concat([rd_data], axis=1)
Box_df.columns = ['KLBN4', 'SUZB3', 'RANI3']
Box_df.plot(kind='box')

# In[12]:

import matplotlib.ticker as tick

scatter_matrix(Box_df, alpha=0.2, hist_kwds={'bins':100},figsize=(10,8))

# In[13]:

#Desvio-Padrão dos dados
print(rd_data.std())

# In[14]:

#Correlação dos dados
print(rd_data.corr())




