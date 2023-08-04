#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1. o produto do dobro do primeiro com metade do segundo .
# 2. a soma do triplo do primeiro com o terceiro.
# 3. o terceiro elevado ao cubo.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
num3 = float(input('Digite um número real: '))

primeiro = (num1*2)*(num2/2)
segundo = (num1*3)+num3
terceiro = num3**3

print(f'1:{primeiro}')
print(f'2:{segundo}')
print(f'3:{terceiro}')