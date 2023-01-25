# função com retorno

def velocidade(espaço, tempo):
    v = espaço/tempo
    return v

aceleração = velocidade(100, 20)/20

print('Velocidade = ', round(velocidade(100, 20), 2))
print('Aceleração = ', round(aceleração, 2))