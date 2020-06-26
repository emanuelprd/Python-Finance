#!/usr/bin/env python
# coding: utf-8

# Importando as minhas bibliotecas

# In[1]:


import pandas as pd
import numpy as np
import pandas_datareader as pdr


# In[2]:


tickers = ['VALE3.SA','PETR4.SA']

my_data = pd.DataFrame()

for t in tickers:
    my_data[t] = pdr.DataReader(t, data_source = 'yahoo',start='2000-01-01')['Adj Close']


# In[3]:


my_data


# Com os dados no formato de frame é possível calcular a taxa de retorno definindo uma variable e calculando =my_data/my_data.shift(1) onde o shift(1) recua a linha em 1 unidade, fazendo com que na prática respeito o calculo de retorno simples diário = p1 / p0. Depois disso há um ajuste dos dados -1 e multiplicando por 100 para ter os valores relativos em percentual 0,05 = 5% 
# 
# rd = retorno diário

# In[4]:


rd_data = my_data/my_data.shift(1)-1
rd_data


# Para calcular o retorno logarítimico é utilizado a função da biblioteca numpy o log() para trazer os valores a base log. 
# 
# lrd = log retorno diário

# In[5]:


lrd_data = np.log(my_data/my_data.shift(1))
lrd_data


# Posso gerar um gráfico utilizando a função .plot() do matplotlib, como a minha variável é uma lista eu posso escolher, caso queira, definir um item dessa lista ['xxxx'] e por fim gerando o meu gráfico em .plot(figsize = (eixo x,eixoy)

# In[7]:


rd_data['VALE3.SA'].plot(figsize = (20,10))


# In[8]:


lrd_data['VALE3.SA'].plot(figsize = (20,10))


# In[ ]:




