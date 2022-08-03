# -*- coding: utf-8 -*-

#funcção fatorial sem recursão
def fatorial(x):
    fat = 1
    for v in range(1,x+1):
        fat = fat * v
    return  fat

# função fatorial recursiva
def fatorialR(x):
    if x==1: return 1
    else: return x * fatorialR(x-1)


# função fibonacci
# 1 1 2 3 5 8 13 21 34 55...
def fibonacci(n):
    ultimo = 1
    penultimo = 1
    for v in range(1,n):
       aux = ultimo
       ultimo = ultimo + penultimo
       penultimo = aux
    return penultimo

def fibonacciR(n):
    if n==1 or n==2: return 1
    else: return fibonacciR(n-1) + fibonacciR(n-2)

print fibonacciR(1)
print fibonacciR(2)
print fibonacciR(3)
print fibonacciR(4)
print fibonacciR(5)





















