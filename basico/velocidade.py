# -*- coding: utf-8 -*-

print 'Informe a quantidade de arquivos transmitidos:'
quantidade = input()
print 'Informe o tamanho médio em Mega bytes:'
tamanho = input()
print 'Informe o tempo gasto no envio:'
tempo = input()

velocidade = (quantidade * (tamanho * 8))/ (tempo * 60)

if (velocidade <= 1):
    print 'Velocidade baixa'
elif (velocidade > 1 and velocidade <=5):
    print  'Velocidade média'
else:
    print  'Alta velocidade'

