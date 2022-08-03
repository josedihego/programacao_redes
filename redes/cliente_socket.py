# -*- coding: utf-8 -*-


import socket
msg = ''
while msg!='Sair':
    meuSocket = socket.socket(socket.AF_INET)
    meuHost = '10.25.202.1'
    minhaPorta = 65432
    meuSocket.connect((meuHost, minhaPorta))
    msg = 'José:' + input()
    meuSocket.sendall(msg.encode('utf-8'))
    resposta  = meuSocket.recv(65565)
    print(resposta.decode('utf-8'))
    meuSocket.close()

