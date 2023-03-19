divisor = int(input('Digite o divisor: '))
dividendo = int(input('Digite o dividendo: '))
lista = []

while dividendo >= divisor:
    if dividendo % divisor == 0:
        lista.append(dividendo)
    dividendo -= 1

print(lista)