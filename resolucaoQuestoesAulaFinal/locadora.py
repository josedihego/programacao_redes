class Locadora:
    def __init__(self, nome, CNPJ):
        self.nome = nome
        self.CNPJ = CNPJ
        self.clientes = []
        self.automoveis = []
        self.alugueis = []

class Cliente:
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF

class Automovel:
    def __init__(self,placa, modelo, cor, ano):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

class Aluguel:
    def __init__(self, cliente, automovel, preco, data_saida, data_entrega):
        self.cliente = cliente
        self.automovel = automovel
        self.preco = preco
        self.data_saida = data_saida
        self.data_entrega = data_entrega
