# Echo server program
import socket

HOST = '10.25.202.1'
PORTA = 50007 # qualquer porta não privilegiada
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
    socket_servidor.bind((HOST, PORTA))
    socket_servidor.listen(1)
    con, end = socket_servidor.accept()
    with con:
        print('Conectado ao cliente', end)
        while True:
            data = con.recv(1024)
            if not data: break
            con.sendall(data)