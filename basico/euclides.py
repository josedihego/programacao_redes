# -*- coding: utf-8 -*-

print 'Informe o primeiro valor'
M = input()
print 'Informe o segundo valor'
N = input()

if M < N:
    aux = M
    M = N
    N = aux

R = M % N

while R != 0:
    M = N
    N = R
    R = M % N

print 'O MDC é: ', N