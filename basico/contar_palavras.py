# -*- coding: utf-8 -*-


palavra = raw_input('Informa uma palavra')
frase = raw_input('Informe uma frase')

# frase: ANA E MARIANA GOSTAM DE BANANA
# palavra: ANA

tamPalavra = len(palavra)
tamFrase = len(frase)
pp=0
ocorrencia = 0

for pf in range(0,tamFrase):
    if frase[pf]==palavra[pp]:
        if(pp==tamPalavra-1):
            ocorrencia = ocorrencia + 1
            pp=0
        pp = pp+1
    else:
        pp=0

print 'A palavra ', palavra, ' aparece ', ocorrencia, ' vezes na \n'
print frase