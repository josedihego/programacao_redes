# -*- coding: utf-8 -*-

print('Informe um valor a ser testado:')

valorInformado = int(input())
ehPrimo = True
teste = 2
while ehPrimo and teste < valorInformado:
    if(valorInformado%teste==0):
        ehPrimo = False
    teste = teste  +1

if ehPrimo:
    print('O número ', valorInformado, ' é primo')
else:
    print('O número ', valorInformado, ' NÃO é primo')