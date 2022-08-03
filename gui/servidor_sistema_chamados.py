# -*- coding: utf-8 -*-

# Equipe: Maria e José


import socket

meuSocket = socket.socket()
meuEndereco = '10.25.201.147'#socket.gethostname()
minhaPorta = 12345
meuSocket.bind((meuEndereco, minhaPorta))

meuSocket.listen(5)
while True:
    cliente, endereco = meuSocket.accept()
    #print 'Conectado com o endereço', endereco
    print (cliente.recv(1024))
    msg = input()
    cliente.send(msg)
    cliente.close()