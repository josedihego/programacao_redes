# -*- coding: utf-8 -*-
arquivo = open('arquivos/VENDAS.txt', 'r')
texto =  arquivo.read()

linhas = texto.splitlines()

vendedores= []
produtos = []
datas = []
precos = []

for l in linhas:
    dados = l.split('#')
    vendedores.append(dados[0])
    produtos.append(dados[1])
    datas.append(dados[2])
    precos.append(float(dados[3]))


print 'Vendedor com maior número de vendas:', max(set(vendedores), key=vendedores.count)
print 'Produto mais vendido:',max(set(produtos), key=produtos.count)
print 'Data com mais vendas:', max(set(datas), key=datas.count)
print 'Média preços:', sum(precos)/ len(precos)
