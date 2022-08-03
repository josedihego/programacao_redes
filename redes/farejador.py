# -*- coding: utf-8 -*-

import socket
import sys
from struct import *

try:
    #  socket.AF_INET: Um par (host, porta) é usado para a família  de endereços AF_INET,f
    #  host: nome de um host, um domínio (daring.cwi.nl) ou endereço IPv4 (100.50.200.5)
    #  porta: um inteiro
    # socket.SOCK_RAW: pacote TCP/IP não processado
    # socket.IPPROTO_TCP: indica o protocolo
    meuSocket = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error as msg:
    print('Socket não pode ser criado', str(msg[0]), ' Mensagem ', msg[1])
    sys.exit()

# recebimento de pacotes
i = 1

# definir uma variavel chamada media_TTL que inicialmente é 0
# voce também ira definir uma variavel chamada soma_TTL que inicialmente é 0

while True:
    print("------***-------PACOTE ", i, "------***-------")
    i = i+1
    # recvfrom recebe dados com buffer de 65565 bytes
    pacote = meuSocket.recvfrom(65565)

    # os primeiros elementos são os dados recebidos
    # o segundo pacote[1] é o enderço do socket que envia os dados
    pacote = pacote[0]

    # primeiros 20 caracteres do cabeçalho IP
    cabIPBruto = pacote[0:20]

    # Desempacotamento do cabeçalho
    cabIP = unpack('!BBHHHBBH4s4s', cabIPBruto)

    # versão
    versao = cabIP[0] >> 4
    # tamanho do cabeçalho IP
    tamCabIP = cabIP[0] & 0xF
    # time to live
    ttl = cabIP[5]
    # protocolo
    protocolo = cabIP[6]
    # inet_ntoa: Converte um endereço IP a partir de uma sequência de  32-bits em um texto
    enderecoFonte = socket.inet_ntoa(cabIP[8])
    enderecoDestino = socket.inet_ntoa(cabIP[9])

    print("-------Cabeçalho IP--------------------")
    print('Versão : ' , str(versao))
    print('Tamanho do cabeçalho IP : ' , str(tamCabIP))
    print('TTL : ' , str(ttl))
    print('Protocolo : ' , str(protocolo))
    print('Endereço fonte : ' , str(enderecoFonte))
    print('Endereço destino : ' , str(enderecoDestino))

    cabTCPBruto = pacote[(tamCabIP * 4):(tamCabIP * 4) + 20]

    # desempacotamento cabeçalho TCP
    cabTCP = unpack('!HHLLBBHHH', cabTCPBruto)

    portaFonte = cabTCP[0]
    portaDest = cabTCP[1]
    sequencia = cabTCP[2]
    confirmacao = cabTCP[3]
    reservaDOFF = cabTCP[4]  # data offset
    tamCabTCP = reservaDOFF >> 4

    print("-------Cabeçalho TCP--------------------")
    print('Porta fonte: ', str(portaFonte))
    print('Porta destino: ', str(portaDest))
    print('Número da sequência: ',  str(sequencia))
    print('Ack: ',  str(confirmacao))
    print('Tamanho do cabeçalho TCP: ', str(tamCabTCP))

    tamCab = (tamCabIP * 4) + (tamCabTCP * 4)
    tamDados = len(pacote) - tamCab

    dados = pacote[tamCab:]

    # print 'Dados : ' + dados
