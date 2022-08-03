# -*- coding: utf-8 -*-


def converterBiDec(binario):
    tam = len(binario)
    decimal = 0
    for p in range(tam-1,-1, -1):
        decimal = decimal + (int(binario[tam-1 - p])*pow(2,p))
    return decimal

def converterDecBi(decimal):
    return ''


decimal = converterBiDec('1001')
print(decimal)