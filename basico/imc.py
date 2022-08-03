# -*- coding: utf-8 -*-


nome = raw_input('Informe seu nome:')
print nome, ', qual sua altura?'
altura = input()
print nome, ', qual seu peso em kg?'
peso = input()

IMC = peso/(altura**2)

print nome, ' seu IMC é de: ', IMC, '\n'

if IMC < 18.5 :
    print nome, ' você esta com Baixo Peso'
elif IMC >=18.5 and IMC < 25:
    print nome, ' você esta com Peso Normal'
else:
    msg = nome + ' você esta com Sobrepeso e'
    if IMC >= 25 and IMC < 30:
        msg =  msg+ ' Pré-obeso'
    elif IMC >= 30 and IMC < 35:
        msg = msg + ' Obeso I'
    elif IMC >=35 and IMC < 40:
        msg = msg + ' Obeso II'
    else:
        msg = msg + ' Obeso III'
print msg


