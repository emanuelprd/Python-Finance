#!/usr/bin/env python
# coding: utf-8

# Importação das biblioetecas que serão utilizadas para o calculo do CAPM

# In[9]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[10]:


#Lista com os tickers que serão utilizados
tickers = ['ABEV3.SA','^BVSP']

#Definindo a minha variável data como um DataFrame()
data = pd.DataFrame()

#Para cada t, sendo t uma variável da minha lista tickers, será importado por meio do DataReader()
for t in tickers:
    data[t]= wb.DataReader(t, data_source = 'yahoo',start='2018-6-29')['Adj Close']


# In[11]:


#Retorno Logarítimico
rl_data = np.log(data/data.shift(1))


# In[13]:


#Covariância dos ativos
cov_data = rl_data.cov()*252
cov_data


# In[14]:


#Covariância do ativo(ABEV3) com o mercado (BVSP)
mk_cov = cov_data.iloc[0,1]
mk_cov


# ![image.png](attachment:image.png)

# In[15]:


b_data = mk_cov/(rl_data['^BVSP'].var()*252)
b_data


# In[16]:


print("Beta:", round((b_data),2),str(tickers[0]))


# In[17]:


rl_data2 = (data/data.iloc[0]-1)*100

rl_data2.plot(figsize=(14,8))
plt.ylabel("Historial return")
plt.title("Retorno Acumulado ABEV3 vs IBovespa",fontsize=18)


# ![image.png](attachment:image.png)

# In[19]:


#Risf Free Rate
rf_rate = float(input("risk-free rate: "))

#Expected Market Rate
m_rate = float(rl_data['^BVSP'].mean()*252)

#CAPM Formula
CAPM = rf_rate + b_data*(m_rate-rf_rate)

print("CAPM =", round((CAPM*100),2),"%")


# In[56]:


#Definindo as variáveis para o gráfico
x = np.array(range(float(b_data))
             
y = rf_rate + 1*(m_rate-rf_rate)*x

plt.title('CAPM ABEV3')

plt.xlabel('Beta')
plt.ylabel('Expected Return E(R)')

plt.plot(x,y, color ='black')


# In[105]:


#Gerando o gráfico
x = np.array(range(200))/100
y = rf_rate + 1*(m_rate-rf_rate)*x

#Gerando o título
plt.title('Security Market Line (SML)')

#Gerar títulos das labels
plt.xlabel('Beta')
plt.ylabel('Expected Return E(R)')

#Plotando os gráficos
plt.plot(x,y, color ='black')
plt.plot(b_data, rf_rate + b_data*(m_rate-rf_rate),'bo', color = 'red')
plt.text(b_data*1.2,rf_rate + b_data*(m_rate-rf_rate),'ABEV3')
plt.axis([0, 3, 0, 0.3])
plt.show()


# In[57]:


b_data


# In[ ]:




