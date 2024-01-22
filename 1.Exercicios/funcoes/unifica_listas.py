#3. Implementar uma função que receba uma lista de listas de comprimentos
#quaisquer e retorne uma lista de uma dimensão.
# Receber uma lista de listas e transformar em apenass uma.


def uni_listas(x):
    lista_unificada = []

    for i in range(0, len(x)):
        for e in range(0, len(x[i])):
            lista_unificada.append(x[i][e])
    return lista_unificada

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
lista_final = uni_listas(lista_de_listas)
print(lista_final)