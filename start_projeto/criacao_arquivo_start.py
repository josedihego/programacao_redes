
media_ttl = 20
nome_arquivo = input('Informe o nome do arquivo a ser criado: ')
meu_arquivo = open(nome_arquivo, 'a')
meu_arquivo.write('\n'+ str(media_ttl))