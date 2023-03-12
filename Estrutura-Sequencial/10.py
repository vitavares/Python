# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# (c*1.8)+32

c = float(input('Temperatura (Celsius): '))
f = (c * 1.8) + 32
print(f'Temperatura (Fahrenheit): {round(f, 2)}')