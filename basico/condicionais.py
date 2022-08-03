# -*- coding: utf-8 -*-

n1 = int(input('Informe um valor 1'))
n2 = int(input('Informe um valor 2'))
n3 = int(input('Informe um valor 3'))

if (n1%2==0 and (n2%2==0 or n3%2==0)) or (n2 % 2 == 0 and (n1 % 2 == 0 or n3 % 2 == 0)) or (n3%2==0 and (n1%2==0 or n2%2==0)):
    print ('Ao menos 2 números são pares')
else:
    print ('Não existem dois números pares em ', n1,',', n2,',', n3)