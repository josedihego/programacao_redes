# -*- coding: utf-8 -*-

from random import randint

fimJogo = False
errouUltima = False
qErros = 0
qTentativas = 0.0

while fimJogo==False:
    n1 = randint(0,10)
    n2 = randint(11,20)
    soma = n1 + n2
    print 'Qual a soma  de', n1, ' e ', n2 , '?'
    resposta = input()
    if(soma != resposta):
        qErros = qErros +1
        if(errouUltima==True):
            fimJogo = True
        else:
            errouUltima = True
    else:
        errouUltima = False

    qTentativas =  qTentativas + 1

print "Fim do jogo. Taxa de acerto = ", (qTentativas-qErros)/(qTentativas) *100, "%"
