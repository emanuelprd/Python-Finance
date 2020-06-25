#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas_datareader as pdr


# Para importar utilizado a função DataReader do pandas_datareader, é importante frisar que o Python é uma linguagem CaseSensitive e para extrair os dados utilizando o Yahoo Finance é simples: 
# 
# pdr.DataReader('Nome do Ativo',data_source = "Yahoo", start = 'Ano-Mês-Dia')

# In[2]:


ibovespa1 = pdr.DataReader('^BVSP', data_source = "yahoo", start='2020-1-1')


# In[3]:


ibovespa1


# Eu posso colocar entre colchetes a coluna do meu DataFrame e importar somente a informação que eu desejo

# In[4]:


ibovespa2 = pdr.DataReader('^BVSP', data_source = "yahoo", start='2020-1-1')['Adj Close']


# In[5]:


ibovespa2


# In[ ]:




