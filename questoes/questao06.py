# -*- coding: utf-8 -*-
print('Informe a quantidade de números a serem testados:')

n = int(input())

L = []

for i in range(0,n):
    valor = int(input())
    L.append(valor)

encontrouPar = False
encontrouImpar = False

for e in L:
    if(e%2==0):
        encontrouPar = True
    else:
        encontrouImpar = True

if(encontrouImpar and encontrouPar):
    print (-1)
elif (not encontrouPar):
    print(1)
else:
    print(0)