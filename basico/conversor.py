# -*- coding: utf-8 -*-



print 'Esolha uma das quatro opçoes abaixo'
print '1. bin -> dec'
print '2. oct -> dec'
print('3. hex -> dec')
print '4. sair'

selecao = input()

print 'Informe o valor a ser convertido:'

valor = raw_input()

def mapLetraNumero(c):
    if c=='A': return 10
    elif c == 'B': return 11
    elif c == 'C':return 12
    elif c == 'D':return 13
    elif c == 'E':return 14
    elif c == 'F':return 15
    else: return c

def converter(valor, base):
    res = 0
    tam = len(valor)
    indice = 1
    for c in valor:
        res = res + int(mapLetraNumero(c)) * base ** (tam-indice)
        indice = indice + 1
    return res

base = 2
if(selecao==2): base = 8
elif (selecao ==3): base = 16

resultado = converter(valor,base)

print resultado