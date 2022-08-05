class Locadora:
    def __init__(self, nome, CNPJ):
        self.nome = nome
        self.CNPJ = CNPJ
        self.clientes = []
        self.automoveis = []
        self.alugueis = []

    def cadastrar_cliente(self, cliente_novo):
        self.clientes.append(cliente_novo)

    def listar_clientes(self):
        for c in self.clientes:
            print(c)
    def remover_cliente(self,CPF):
        cliente_remover = None
        for c in self.clientes:
            if c.CPF == CPF:
                cliente_remover = c
        if cliente_remover!=None:
            self.clientes.remove(cliente_remover)

class Cliente:
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF
    def __str__(self):
        return f'Nome: {self.nome} , CPF: {self.CPF}'

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

# executar alguns testes

locadoraBonsAmigos = Locadora(nome='Locadora Bons/Boas Amigos(as)',CNPJ='03.778.130/0001-48')
maria = Cliente(nome='Maria do Socorro',CPF='111.111.111-11')
zeca = Cliente(nome='Zeca Pagodinho',CPF='222.222.222-22')
joana = Cliente(nome='Joana',CPF='333.333.333-33')
tina = Cliente(nome='Tina Taner',CPF='444.444.444-44')
locadoraBonsAmigos.cadastrar_cliente(maria)
locadoraBonsAmigos.cadastrar_cliente(zeca)
locadoraBonsAmigos.cadastrar_cliente(joana)
locadoraBonsAmigos.cadastrar_cliente(tina)
locadoraBonsAmigos.listar_clientes()
print('Depois da remoção do 222.222.222-22')
locadoraBonsAmigos.remover_cliente('222.222.222-22')
locadoraBonsAmigos.listar_clientes()