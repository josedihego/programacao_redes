# -*- coding: utf-8 -*-

#print 28/5
#print 28/5.0

L = []

print 'Informe os valores a serem inseridos na lista' \
      'ou digite SAIR para encerrar.'

valor_digitado = 'qualquer coisa'

while valor_digitado.lower() != 'sair':
    valor_digitado = raw_input()
    if(valor_digitado.lower() != 'sair'
            and valor_digitado.isdigit()):
        L.append(int(valor_digitado))
    else:
        print 'opção inválida'



print L

print 'Média:', sum(L)/float(len(L))

