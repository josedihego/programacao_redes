# https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
n = int(input('Informe o valor de n: '))
i = int(input('Informe o valor de i: '))
j = int(input('Informe o valor de j: '))

contador = 0
lista = []
while(len(lista) != n):
    e1 = i * contador
    e2 = j * contador
    if not e1 in lista: lista.append(e1)
    if (not e2 in lista) and len(lista) !=n : lista.append(e2)
    contador = contador + 1

print(lista)