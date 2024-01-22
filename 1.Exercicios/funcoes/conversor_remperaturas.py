#1. Implementar duas funções:
#▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
#▪ Outra que converta temperatura em graus Fahrenheit para Celsius.

def c_to_f(temp):
    f = (1.8 * temp) + 32
    return f

def f_to_c(temp):
    c = (temp - 32) / 1.8
    return c

temperatura = float(input('Temperatura atual: '))
escala = int(input('Escala utilizada:\n[1] Celsius\n[2]Fahrenheit\n'))

if escala == 1:
    temp_f = c_to_f(temperatura)
    print(temperatura, ' ºC equivalem a ', temp_f, 'ºF.')
elif escala == 2:
    temp_c = f_to_c(temperatura)
    print(temperatura, ' ºF equivalem a ', temp_c, 'ºC.')