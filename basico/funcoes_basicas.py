# -*- coding: utf-8 -*-
import math

def delta(a,b,c):
    return (b**2) - (4 *a * c)


def raizes(a, b, c):
    if(delta(a,b,c) >=0):
        x1 = ((-1 * b) + math.sqrt(delta(a,b,c)))/ (2*a)
        x2 = ((-1 * b) - math.sqrt(delta(a,b,c)))/ (2*a)
        print 'raízes ', x1 , ' e ', x2

    else:
        print 'não existem raízes reais'


print delta(2.0,-3.0,1.0)
raizes(2.0,-3.0,1.0)