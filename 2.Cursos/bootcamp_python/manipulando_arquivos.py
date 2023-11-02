# %%
import os
# %%
# Criando arquivo
arquivo = 'arquivo.txt'
# %%
# Abrindo arquivo de modo que ele permita escrita
file = open(arquivo, 'w')
file.write('#Familia Sigmoidal')
file.close()
# %%
os.listdir()
# %%
# Abrir arquivo para leitura
file = open(arquivo, 'r')

# Lendo arquivo
text = file.read()
print(text)
# %%
# A função whitch nos deixa manipular o arquivo com ele aberto
with open('teste.txt', 'w') as txt:
    txt.write("Testando a função.")
# %%
# Acrescentar informações em um arquivo existente
with open('teste.txt', 'a') as txt:
    txt.write('\nAcrescentando informações')
# %%
# Lendo o arquivo
with open('teste.txt', 'r') as txt:
    print(txt.read())
# %%
# Renomeando o arquivo
os.rename('teste.txt', 'sigmodal.txt')
os.listdir()