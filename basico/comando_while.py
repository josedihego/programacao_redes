# -*- coding: utf-8 -*-

print('Informe um valor par entre 30 e 100 ')

n = int(input())

while not(n >= 30 and n <=100 and n%2==0):
    n = int(input())

print('Você digitou um número par entre 30 e 100')

