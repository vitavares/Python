# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

lado = float(input('Lado em metros: '))
dobro = (lado ** 2) * 2
print(f'O dobro da área deste quadrado é {round(dobro, 2)}')