# -*- coding: utf-8 -*-

lista_valores = [5,6,7,-1,10,12]

numero = input('Informe um valor: ')

if lista_valores.count(numero) > 0:
    print numero, ' esta na lista ', lista_valores
else:
    print numero, ' NÃO esta na lista ', lista_valores
