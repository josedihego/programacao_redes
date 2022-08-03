# -*- coding: utf-8 -*-

salario = input('Informe seu rendimento')

imposto = 0

if salario > 1903.98:
    if salario > 2826.65:
        imposto = imposto + (2826.65 - 1903.99) * 0.075
        if salario > 3751.05:
            imposto = imposto + (3751.05 - 2826.66) * 0.15
            if salario > 4664.68:
                imposto = imposto + (4664.68-3751.06) * 0.225
                imposto = imposto + (salario - 4664.68) * 0.275
            else:
                imposto = imposto + (salario - 3751.06) * 0.225
        else:
            imposto = imposto + (salario - 2826.66) * 0.15
    else:
        imposto = imposto + (salario - 1903.99) * 0.075

print "Você pagará de imposto ao leão: ", imposto