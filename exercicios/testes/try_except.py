# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar
#no python, erros = Exceções

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_float = float(numero_str) # se der um erra aqui, vai pular pra linha 12
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')