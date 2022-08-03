# -*- coding: utf-8 -*-

def converterBinDec(binario):
    decimal = 0
    tam = len(binario)
    for p in range(0,tam):
        decimal = decimal + int(binario[p]) * pow(2,tam-p-1)
    return decimal

def converterDecBin(decimal):
    resultado = decimal
    resto = ''
    while(resultado!=0):
        resto = str(resultado%2) +resto
        resultado = resultado/2
    return  resto


print 'Informe um valor em binário:'
binario = raw_input()
print converterBinDec(binario)

print 'Informe um valor decimal:'
decimal = input()
print converterDecBin(decimal)


