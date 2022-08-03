# -*- coding: utf-8 -*-

# 'r' leitura apenas
# 'w' escrita apenas
# 'a' para escrita em adição ao conteúdo existente
# 'r+' para leitura e escrita
arquivo = open('/home/jdso/Desktop/saudacoes.txt', 'w')
arquivo.write('oi\n')
arquivo.write('galera de redes\n')
arquivo.write('tudo bem?\n')
arquivo.write('até mais\n')
arquivo.close()


arquivo = open('/home/jdso/Desktop/saudacoes.txt', 'w')
arquivo.write('ainda não...\n')
arquivo.close()


arquivo = open('/home/jdso/Desktop/saudacoes.txt', 'r')
print(arquivo.read())