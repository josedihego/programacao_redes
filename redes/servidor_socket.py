# -*- coding: utf-8 -*-

# Equipe: Maria e José


import socket

socketServidor = socket.socket(socket.AF_INET)
meuEndereco = '10.25.202.1'
minhaPorta = 65432
socketServidor.bind((meuEndereco, minhaPorta))

socketServidor.listen(10)
while True:
    cliente, endereco = socketServidor.accept()
    print('Conectado com o endereco', endereco)
    msg = cliente.recv(65565)
    print(msg.decode('utf-8'))
    cliente.sendall('Msg recebida!'.encode('utf-8'))
    cliente.close()