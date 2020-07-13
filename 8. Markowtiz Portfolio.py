#!/usr/bin/env python
# coding: utf-8

# In[120]:


import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt


# In[121]:


tickers = ['ABEV3.SA','ITUB4.SA']

data = pd.DataFrame()

for t in tickers:
    data[t] = pdr.DataReader(t, data_source = 'yahoo', start ='2018-06-26')['Adj Close']


# rn_data = retorno normalizado

# In[122]:


rn_data = (data/data.iloc[0]-1)*100
rn_data.plot(figsize=(20,8))


# A função .fillna() substituiu os NaN por um valor, no caso foi utilizado o segundo valor da linha .iloc[1].
# 
# rl_data = retorno-log

# In[123]:


rl_data = np.log(data/data.shift(1))
rl_data.fillna(rl_data.iloc[1])


# In[124]:


#Variância
rl_data.var()


# In[125]:


#Covariância
rl_data.cov()


# In[126]:


#Correlação
rl_data.corr()


# In[127]:


n_data = len(tickers)
n_data


# O np.random.random(x) cria uma quantidade de floats aleatórios entre 0 e 1 onde a quantidade de números aleatórios é igual ao valor x

# In[128]:


rn = np.random.random(n_data)
rn


# Pra formar a carteira de Markowitz eu preciso de n carteiras para cada peso(weight) de ativo, para isso é utilizado a notação /= onde pode ser traduzido como sendo weights = 1/weights, ou seja, a sum(weights) vai ser necessariamente igual a 1. Retorno é ponderado pelo peso e o desvio padrão pela formula abaixo:
# 
# ![image.png](attachment:image.png)

# In[158]:


#Transformar em lista
p_return = []
p_var = []

# Loop para 1000 cenários
for x in range(1000):
    weights = np.random.random(n_data)
    weights /= np.sum(weights)
    #Retorno do Portfolio
    p_return.append(np.sum(weights*rl_data.mean())*250)
    #Variância do Portfolio
    p_var.append(np.sqrt(np.dot(weights.T, np.dot(rl_data.cov()*250, weights))))
    
p_return, p_var        


# In[159]:


#Transformar variáveis em arrays ( matrizes)
p_return = np.array(p_return)
p_var = np.array(p_var)

p_return, p_var


# In[212]:


plt.figure(figsize=(12, 8)) 
plt.scatter(p_var, p_return, s=1,c='black')
plt.scatter(p_var.min(), p_return[853], s=100,c='red')

#Parâmetros
plt.xlabel("Expected Volatility")
plt.ylabel("Expected Return")
plt.title("Markowitz Portfolio ABEV3 vs ITUB4")
plt.legend([str(round(p_var.min(),5))])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




