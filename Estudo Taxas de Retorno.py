#!/usr/bin/env python
# coding: utf-8

# Calculando Taxas de Retorno

# In[1]:


import pandas as pd
import pandas_datareader as pdr
import numpy as np


# In[2]:


# Para importar dados por meio do pandas_DataReader 
# Para importar colunas em específico, usar ["Nome da Coluna"]
# Nesse exercício irei usar o Indice Ibovespa
BVSP = pdr.DataReader('^BVSP', data_source='yahoo', start='1995-1-1')['Adj Close']
BVSP


# In[3]:


# .shift(1) é utilizado para a divisão de cada array ser feito pelo anterior

dr_BVSP = BVSP/BVSP.shift(1)-1

# dr_ é daily return
dr_BVSP


# In[4]:


#Utilizo o iloc pois ele ira travar todos as minhas divisões na primeira linha. 

cr_BVSP = (BVSP/BVSP.iloc[0]-1)*100

# cr_ é acumulative return

cr_BVSP


# In[5]:


#Gráfico demonstra a variação diárias percentual dos preços 
dr_BVSP.plot(figsize=(10,10))


# In[6]:


#Gráfico do retorno acumulado
cr_BVSP.plot(figsize=(15,10))


# In[7]:


# Uma boa ideia seria também encontrar os valores em logaritmo
ldr_BVSP = np.log(BVSP/BVSP.shift(1))

# ldr é log daily return
ldr_BVSP


# In[8]:


#Gráfico da variação diária logarítima
ldr_BVSP.plot(figsize=(10,10))


# In[9]:


# Para provar que os dois são bem diferentes, vou dividi-los, se forem bem próximos o resultado tem que ser próximo a 1. 
divisao = ldr_BVSP/dr_BVSP
divisao


# In[19]:


# Diferença nominal entre as duas formas de calcular o retorno diário
diferenca = dr_BVSP - ldr_BVSP
diferenca


# In[20]:


#Graficamente

diferenca.plot(figsize=(20,10))


# In[24]:


#Calculo da variância
print("Variance of Log Returns :", round(ldr_BVSP.var()*100, 4),"%")
print("Variance of Linear Return :", round(dr_BVSP.var()*100, 4),"%")


# In[23]:


#Calculo do desvio-padrão
print("Standard Deviation of Log Returns :",round((ldr_BVSP.var()*0.5)*100, 4),"%")
print("Standard Deviation of Linear Return :", round((dr_BVSP.var()*0.5)*100, 4),"%")


# In[26]:


#Experimento, quais foram os piores e melhores dias do Ibovespa? 

print(min(ldr_BVSP[1:])*100)
print(min(dr_BVSP[1:])*100)    
print(max(ldr_BVSP[1:])*100)
print(max(dr_BVSP[1:])*100) 


# In[ ]:




