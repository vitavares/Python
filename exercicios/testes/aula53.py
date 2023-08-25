"""
Flag (Bandeira) -> Marcar um local
None = Não valor
is e is not = é e não é (tipo, valor, identidade)
"""


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
print(passou_no_if)

print(passou_no_if is None)
print(passou_no_if is not None)