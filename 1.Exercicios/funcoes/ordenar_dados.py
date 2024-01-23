#6. Crie uma função que:
#▪ Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão
#igual) e um booleano (reverso, falso por padrão).
#▪ Retorne dados ordenados pelo item indicado pela chave e em ordem
#decrescente se reverso for verdadeiro.

def ordena_dados(dados, chave = 0, reverso = False):
    dados_ordenados = sorted(dados, key=lambda x: x[chave], reverse = reverso)
    return dados_ordenados

lista_de_tuplas = [(1, 5, 3), (2, 3, 1), (4, 2, 8), (0, 7, 6)]
resultado = ordena_dados(lista_de_tuplas, chave = 2, reverso = True)
print(resultado)