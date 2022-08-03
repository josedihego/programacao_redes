# -*- coding: utf-8 -*-

import socket
import struct

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]
def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

arquivo = open('arquivos/ips_scapy', 'r')
texto =  arquivo.read()

linhas = texto.splitlines()

ipsPrimeiro = {}
macsPrimeiro = {}

for linha in linhas:
    ipsPrimeiro.update({ ip2int(linha.split('  ')[2]) : linha.split('  ')[1]})

for chave in sorted(ipsPrimeiro):
    print "valor %s: ip %s : mac %s" % (int2ip(chave), chave, ipsPrimeiro[chave])










