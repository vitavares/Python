# Média de 3 números.

soma = 0
for i in range(3):
    num = int(input('Número: '))
    soma += num

media = soma / 3
print(f'A média destes números é {media}')