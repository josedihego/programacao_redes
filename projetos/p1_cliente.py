import sys
import socket
host = 'localhost'
port = 1600

my_system = sys.platform

# Cria socket TCP/IP
socket_cliente = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)
# Conecta o socket cm o servidor
server_addr = (host, port)
print('Conectando ao %s na porta %s' %
      server_addr)
socket_cliente.connect(server_addr)

# Envio de mensagens
try:
    # Senvio da mensagem
    message = my_system
    # substiuir essa mensagem com o nome do SO
    print('Enviando %s' % message)
    socket_cliente.sendall(message.encode('utf-8'))
except socket.error as erro:
    print('Erro de socket: %s' % str(erro))
except Exception as erro:
    print('Outro erro: %s' % str(erro))
finally:
    print('Encerrando conexão com servidor')
    socket_cliente.close()