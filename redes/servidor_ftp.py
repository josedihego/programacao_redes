# -*- coding: utf-8 -*-

#instalação do PIP linux
# sudo apt install python3-pip
#instalação do PIP Windows
#Baixar https://bootstrap.pypa.io/get-pip.py abrir o cmd e navegar até a pasta onde baixou o arquivo acima e então executar o comando abaixo
#python get-pip.py

#comando para instalação
# sudo pip install pyftpdlib


from pyftpdlib.authorizers import DummyAuthorizer
# DummyAuthorizer gerencia as permissões de autorização no servidor FTP
# senhas salvas sem qualquer proteção em arquivos de texto
from pyftpdlib.handlers import FTPHandler
# FTPHandler verificação acesso (usuário e senha) e permissões
from pyftpdlib.servers import FTPServer


autoridade = DummyAuthorizer()
autoridade.add_user(
    'admin', 'admin', '/home/jdso/servidorFTP', perm='elradfmw')
autoridade.add_user('maria', 'ma08', '/home/jdso/servidorFTP', perm='elradfmw')
# 1. cadastrar alguns usuários (clientes FTP)
#autoridade.add_anonymous('/home/jdso/servidorFTP', perm='elradfmw')

gerenteFTP = FTPHandler
gerenteFTP.authorizer = autoridade

servidor = FTPServer(('10.25.201.53', 1026), gerenteFTP)
servidor.serve_forever()

#
# "e" = mudar diretório (CWD, CDUP )
# "l" = listar arquivos (LIST, NLST, STAT, MLSD, MLST, SIZE )
# "r" = baixar arquivos (RETR)
# "a" = adicionar dados a um arquivo existente (APPE )
# "d" = remover um arquivo ou diretório (DELE, RMD)
# "f" = renomear um arquivo ou diretório (RNFR, RNTO )
# "m" = criar um diretório (MKD )
# "w" = armazenar um arquivo no servidor (STOR, STOU )
# "M" = mudar as permições de um arquivo (SITE CHMOD )
# "T" = mudar o tempo do arquivo (SITE MFMT )
