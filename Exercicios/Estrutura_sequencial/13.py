# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#    Para homens: (72.7*h) - 58
#    Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a sua altura: '))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7
print('Esse é o seu peso ideal caso você seja: ')
print('Mulher: ', round(mulher, 2))
print('Homem: ', round(homem, 2))