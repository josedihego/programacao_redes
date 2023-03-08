# https://github.com/PacktPublishing/Python-Network-Programming-Cookbook-Second-Edition

import socket
host = 'localhost'
payload_data = 2048
queue_size = 5
port = 1600

# Criação de socket
socket_server = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)
# Habilitando reuso de endereço e porta
socket_server.setsockopt(socket.SOL_SOCKET,
                           socket.SO_REUSEADDR, 1)
# Ligando o socket com a porta
server_addr = (host, port)
print('Iniciando o servidor %s na porta %s'
      % server_addr)
socket_server.bind(server_addr)
# Aguardando clientes.tamanho_fila especifica
# o tamanho máximo da fila de clientes
socket_server.listen(queue_size)
# ler o valor de n
# definir um contador de cliente
n = int(input('Informe a quantidade de clientes que serão atndidos: '))
i = 0

qnt_linux = 0
qnt_macos = 0
qnt_windows = 0;
qnt_other = 0

while i < n: 
    i = i + 1
    print('Esperando mensagens do cliente')
    client, client_addr = socket_server.accept()
    data = client.recv(payload_data)
    # fazer o seu if elif e else
   
    if data:
        if('linux' in str(data)):
            qnt_linux = qnt_linux +1
        elif('macos' in str(data)):
             qnt_macos = qnt_macos + 1
        elif('windows' in str(data)):
            qnt_windows =  qnt_windows + 1
        else:
            qnt_other = qnt_other + qnt_other    
    # end connection
    client.close()

qnt_all  =  qnt_linux+ qnt_macos + qnt_windows + qnt_windows + qnt_other
print('Percentagem linux: ', (qnt_linux/(n*1.0)) * 100, '%')
print('Percentagem  macos: ', (qnt_macos/(n*1.0)) * 100, '%')
print('Percentagem  windows: ', (qnt_windows/(n*1.0)) * 100, '%')
print('Percentagem  outros: ', (qnt_other/(n*1.0)) * 100, '%')