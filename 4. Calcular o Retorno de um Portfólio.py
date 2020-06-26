#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[2]:


tickers = ['VALE3.SA','PETR4.SA','USIM5.SA','CSNA3.SA']
data = pd.DataFrame()

for t in tickers:
    data[t] = wb.DataReader(t, data_source = 'yahoo', start = '2000-01-01')['Adj Close']


# Para normalizar os retornos e traze-los a mesma base basta utilizar a property .iloc[0] que irá travar o meu preço ao primeiro valor da minha lista

# In[18]:


rn_data = data/data.iloc[0]
rn_data


# In[19]:


rn_data.plot(figsize = (20,10))


# Por meio do np.array eu crio um objeto array em uma lista[] e que irá representar o peso da minha carteira em cada ativo. 

# In[20]:


weights = np.array([0.25, 0.25, 0.25, 0.25])


# Utilizo a property .mean() para encontrar a média da variação diária

# In[21]:


rd_data = (data/data.shift(1)-1)*100
rd_data.mean()


# Utilizo a função .dot que irá multiplicar ( x, y) = x * y e assim vou saber o resultado ponderado desse portfolio

# In[22]:


pfolio = np.dot(rd_data.mean()*250, weights)


# In[23]:


print(str(round(pfolio,2))+'% a.a')


# In[ ]:




