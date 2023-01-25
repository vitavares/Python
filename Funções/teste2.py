def dados(nome, idade=None):
    print('Nome: {}'.format(nome))
    if idade is not None:
        print('Idade: {}'.format(idade))
    else:
        print('Idade não informada.')

dados('ana', 17)
dados('josé')