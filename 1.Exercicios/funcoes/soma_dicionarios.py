#4. Implementar uma função que receba um dicionário e retorne a soma, a
#média e a variação dos valores.


def medidas_dicio(dicio):
    valores = dicio.values()
    soma = sum(valores)
    media = soma / len(valores)
    var = max(valores) - min(valores)

    print('Soma:', soma, '\nMédia:', media, '\nVariação:', var)

exemplo_dicionario = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
medidas_dicio(exemplo_dicionario)
