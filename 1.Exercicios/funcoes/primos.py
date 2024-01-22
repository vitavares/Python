#2. Implementar uma função que retorne verdadeiro se o número for primo 
#(falso caso contrário). Testar de 1 a 100.

def primos(x):
    div_encontrados = []
    for i in range(2, x+1):
        if (x%i) == 0:
            div_encontrados.append(i)
    if len(div_encontrados) == 1 and div_encontrados[0] == x:
        print('é um número primo.')
    else:
        print('não é um número primo.')

for i in range(1, 100):
    print('Número: ', i)
    primos(i)
    print('\n')