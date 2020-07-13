#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importação das biblioetecas, especial atenção para aos scipy e statsmodels que serão utilizados para fazer a regressão. 
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt


# In[3]:


#importando dados de uma sheet do Excel, para isso utilizar pd.read_excel(r"")
data = pd.read_excel(r"C:\Users\User\Desktop\Estudo.xlsx")


# In[5]:


#Definindo as variáveis dependentes(Y) e independentes(X)
X = data[['EMBI+ Risco-Brasil','Dólar']]
Y = data['Ibovespa Fechamanto']


# Notação para realizar a regressão:
# 
# X = sm.add_constant(X)
# 
# reg = sm.OLS(Y, X).fit()

# In[8]:


X = sm.add_constant(X)

#.fit() é um método que define as variáveis como parâmetros dependente e independente
reg = sm.OLS(Y, X).fit()


# In[9]:


# .summary() é um função que da um resumo dos dados
reg.summary()


# In[13]:


# %matplotlib notebook é usado para poder mover o gráfico 3D
get_ipython().run_line_magic('matplotlib', 'notebook')
# Biblioeteca para poder plotar os gráficos em 3 dimensões
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))

#Necessário para gerar o gráfico
ax = fig.add_subplot(projection ='3d')

#Definindo os eixos ( x,y,z)
x = data[['Dólar']]
y = data[['EMBI+ Risco-Brasil']]
z = data[['Ibovespa Fechamanto']]

#Plotagem de gráfico de dispersão em 3D
ax.scatter3D(x, y, z, color='black')

ax.set_ylabel('EMBI+',fontsize=14)
ax.set_xlabel('Dólar',fontsize=14)
ax.set_zlabel('Ibovespa Fechamanto', fontsize=14)

plt.show()


# In[ ]:




