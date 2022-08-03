# -*- coding: utf-8 -*-


lista = [1,4,5,6,7,8,9]
soma =0.0

listaPosicoes = range(0,len(lista)+1,2)
for i in listaPosicoes:
    soma = soma + lista[i]

media = soma/ len(listaPosicoes)

print media