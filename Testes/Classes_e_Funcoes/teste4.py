class Carro:
    def __init__(self, marca, modelo, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
    
    def LigarCarro(self):
        print('Ligando ', self.modelo, ' da marca ', self.marca)

    def DesligarCarro(self):
        print('Desligando ', self.modelo, ' da marca ', self.marca)

    def Info(self):
        print('\nINFORMAÇÕES DO SEU CARRO')
        print('\n', self.marca, self.modelo, self.cor, self.valor)

carro1 = Carro('Suzuki', 'jimny', 'vermelho', 150000)
carro1.LigarCarro()
carro1.DesligarCarro()
carro1.Info()