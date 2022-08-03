# -*- coding: utf-8 -*-

lista = []
valor = 0
while valor!='SAIR':
    print 'Informe um valor para a lista ou SAIR para terminar.'
    valor = raw_input()
    if valor!='SAIR':
        lista.append(int(valor))
print  lista

print 'Informe o código de erro na LISTA'
codigo_erro = input()

tamanho = len(lista)

soma = 0
pos = 0
while codigo_erro != lista[pos] and pos < tamanho:
    soma = soma + lista[pos]
    pos = pos + 1

print 'Soma de valores até erro: ', soma
