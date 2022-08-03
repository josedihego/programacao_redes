# -*- coding: utf-8 -*-
total = 0
arquivo_maria = open('arquivos/vendas_maria.txt', 'r')
texto_maria = arquivo_maria.read()
linhas_maria = texto_maria.split('\n')
for linha in linhas_maria:
    valor  = float(linha.split('/')[3])
    total = total + valor

arquivo_joao = open('arquivos/vendas_joao.txt', 'r')
texto_joao = arquivo_joao.read()
linhas_joao = texto_joao.split('\n')
for linha in linhas_joao:
    valor = float(linha.split('/')[3])
    total = total + valor

arquivo_resumo = open('arquivos/resumo.txt', 'w') # dica na lista use 'a'
# pois o arquivo pode já existir. Dessa maneira evita-se perder seu conteúdo

arquivo_resumo.write(texto_maria)
arquivo_resumo.write('\n'+texto_joao)
arquivo_resumo.write('\nTOTAL '+ str(total))
arquivo_resumo.close()