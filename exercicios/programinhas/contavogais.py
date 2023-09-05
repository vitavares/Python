palavra = input('Digite uma palavra: ')
vogais = ['a', 'e', 'i', 'o', 'u']
quant_vogais = 0

for i in range(len(palavra)):
    if palavra[i] in vogais:
        quant_vogais += 1

print(f'Essa palavra tem {quant_vogais} vogais.')