# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
#Área do circulo => A = π . r2

import math

raio = float(input('Área do círculo (Metros): '))
area = math.pi * (raio ** 2)
print(f'A área do círculo é de {round(area, 2)} quadrados')
