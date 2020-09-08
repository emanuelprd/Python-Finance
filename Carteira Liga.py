#!/usr/bin/env python
# coding: utf-8

# Biblioetecas que serão utilizadas

# In[24]:


import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt


# Os ativos selecionados são incluidos na lista 'tickers' e extraindos do banco de dados do Yahoo Finance

# In[25]:


tickers = ['ALUP11.SA','B3SA3.SA','HYPE3.SA','ITUB3.SA','PETR4.SA','SLCE3.SA','VALE3.SA','VVAR3.SA','WEGE3.SA','SAPR3.SA']

ativos = pd.DataFrame()

for t in tickers:
    #Período da carteira ( 1 Mês )
    ativos[t] = pdr.DataReader(t, data_source='yahoo', start='2020-08-10', end='2020-09-05')['Adj Close']


# Calculo do retorno da carteira

# In[26]:


rativos = (ativos/ativos.iloc[0]-1)*100
rcarteira = float((sum(rativos.iloc[-1])/len(tickers)))
rcarteira


# Gráfico individualizado de cada ativo da carteira

# In[27]:


fig = plt.figure(figsize=(20, 10))
labels = str(round(rativos.iloc[-1],2))
fig.suptitle(labels,x=0.13, y=0.39,ha='left', fontsize=16)
plt.plot(rativos/10)
plt.rcParams.update({'font.size': 18})
plt.xlabel('Data-Base',fontsize=20)
plt.ylabel('Retorno Percentual(%)',fontsize=20)


# Gráfico da performance geral da carteira 

# In[28]:


grafico = (rativos/10).sum(axis = 1)

plt.figure(figsize=(15,10))
plt.title("Desempenho Carteira LMF",fontsize=25)
plt.xlabel('Data',fontsize=18)
plt.ylabel('Retorno Percentual (%)',fontsize=18)

labels = "Retorno Mensal da Carteira: " + str(grafico.iloc[-1])

grafico.plot(label = labels, figsize=(14,10))

plt.legend(loc='best',fontsize=15)

plt.show()


# In[ ]:




