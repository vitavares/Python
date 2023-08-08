#%%
import pandas as pd

#%%
# Atribuindo dados externos ao python com pandas.
df=pd.read_csv('https://raw.githubusercontent.com/carlosfab/curso_data_science_na_pratica/master/modulo_02/BBAS3.SA.csv')
df.head()

# %%
# Saber a quantidade de linhas e colunas
df.shape

# %%
# Selecionar apenas uma coluna do df para vizualizar
df["Close"]
df.Close

# %%
# Medidas básicas
df["Close"].mean() # média
df["Close"].std() # desvio padrão

# %%
# Mostra um quadro com algumas medidas importantes.
df.describe()