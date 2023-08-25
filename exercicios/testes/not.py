# Operador 'not'
# not True = False
# not False = True

senha = input('Senha: ')

# Uma string vazia é False, então se a senha não for digitada, vai entrar no if.
if not senha:
    print('Você não digitou nada.')
elif senha == '12345678':
    print('Senha correta!')
else:
    print('Senha incorreta!')