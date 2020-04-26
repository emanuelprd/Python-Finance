#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando as Libraries que serão utilizadas

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm


# In[28]:


# Objetivo é analisar a reação do par BRL/USD com as taxa de juros, extraio os meus dados do YahooFinance

currencies = ['BRLUSD=X']
c_data = pd.DataFrame()

for c in currencies:
    c_data[c] = wb.DataReader(c, data_source = 'yahoo', start ='2020-01-08', end ='2020-03-24' )['Adj Close']  
    


# In[68]:


#Ajustando os meus retornos

c_return = (c_data/c_data.iloc[0]-1)*100


# In[4]:


c_return.plot(figsize=(20,10))


# In[69]:


# Como no YahooFinance não tinha os dados de taxas de juros futuro que gostaria, extrai os dados do Investing e coloquei em um sheet do Excel

i_data = pd.read_excel(r'C:\Users\User\Desktop\INTEREST BONDS.xlsx',usecols = "A")
i_return = (i_data/i_data.iloc[0]-1)*100


# In[6]:


c_return.plot(figsize=(20,10))
i_return.plot(figsize=(20,10))


# In[60]:


#Definindo meus eixos

y = c_return['BRLUSD=X']
x = i_return['BRAZIL']
plt.figure(figsize=(12, 8))
plt.scatter(X,Y)
plt.xlabel('BRLUSD')
plt.ylabel('DI1FUT')
plt.title('Linear Regression of BRLUSD and DI1FUT')


# In[62]:


#Resultados da regressão, o scipy nos da esses informações facilmente. 

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x,y)

print("R squared is equal to: ", round((rvalue),2))

if rvalue > 0.85: 
    conclusion = print("DI1FUT", "explain well the moviments of ",currencies)
else:
    conclusion = print("DI1FUT", "do not explain well the moviments of",currencies)
        


# In[61]:


# Ajustando os dados

x= np.array(x)
y = np.array(y)
x1 = sm.add_constant(x)
reg = sm.OLS(y,x1).fit()
reg.summary()

