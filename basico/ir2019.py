# -*- coding: utf-8 -*-

print 'Olá, informe seu rendimento bruto:'
salario = float(input())
faixa = 1
imposto = 0

if salario <= 1903.98:
    faixa =1
    imposto = 0
elif salario >= 1903.99 and salario <= 2826.65:
    faixa = 2
    imposto = 0 + (salario-1903.99) * 0.075
elif salario >= 2826.66 and salario <= 3751.05:
    faixa = 3
    imposto = 0 + (2826.65-1903.99) * 0.075+\
              (salario - 2826.66) * 0.15
elif salario >= 3751.06 and salario <= 4664.68:
    faixa = 4
    imposto = 0 + (2826.65 - 1903.99) * 0.075 + \
              (3751.05 - 2826.66) * 0.15+\
              (salario -3751.06)*0.225
else:
    imposto = 0 + (2826.65 - 1903.99) * 0.075 + \
              (3751.05 - 2826.66) * 0.15 + \
              (4664.68 - 3751.06) * 0.225+\
              (salario - 4664.69) * 0.275
    faixa = 5


print 'Sua faixa foi: ', faixa
print 'Imposto a recolher:', imposto
print  'Aliquota efetiva:', imposto/salario*100, '%'