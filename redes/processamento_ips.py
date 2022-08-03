# -*- coding: utf-8 -*-


# pip install netaddr

from netaddr import IPNetwork

def mesmaSubrede(ip1,ip2):
    return IPNetwork(ip1) == IPNetwork(ip2)


listaIP = ['128.233.17.12/255.255.0.0',
           '128.233.12.17/255.255.0.0',
           '10.10.101.1/255.255.0.0',
           '10.11.45.9/255.255.0.0',
           '192.168.10.2/255.255.255.192',
           '192.168.20.5/255.255.255.240',
           '192.168.10.1/255.255.255.128',
           '192.168.0.10/255.255.255.192',
           '192.168.0.18/255.255.255.224',
           '192.168.0.16/255.255.255.128',
           '192.168.0.24/255.255.255.192',
           '10.10.202.23/255.0.0.0',
            '192.168.0.22/255.255.255.192'
           ]

L= []
for eip1 in listaIP:
    L.append(eip1)
    for eip2 in listaIP:
        if mesmaSubrede(eip1,eip2) and eip1!=eip2:
            L.append(eip2)
            listaIP.remove(eip2)
    print(L)
    L = []










