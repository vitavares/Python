#5. Escreva uma função que:
#▪ Receba uma frase como parâmetro.
#▪ Retorne uma nova frase com cada palavra com as letras invertidas.

def gera_frase(frase):
    frase_desordenada = ' '
    palavras = frase.split()
    for i in range(0, len(palavras)):
        palavras[i] = palavras[i][::-1]
    frase_desordenada = ' '.join(palavras)
    print(frase_desordenada)

frase_inicial = input('Digite uma frase: ')
gera_frase(frase_inicial)