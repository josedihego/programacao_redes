# -*- coding: utf-8 -*-
from random import randint
errosSeguidos = 0
tentativas = 0
acertos = 0
while errosSeguidos < 2:
    tentativas = tentativas+1
    n1 = randint(0,10)
    n2 = randint(0,10)
    print('Qual a soma de ', n1, '+',n2,'?')
    resposta = int(input())
    if(resposta!= (n1+n2)):
        errosSeguidos=errosSeguidos+1
    else:
        errosSeguidos = 0
        acertos = acertos+1
print('Fim do jogo')
print('Taxa de acerto: ',acertos/tentativas)