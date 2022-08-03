
n = int(input('Informe o valor de n: '))
temImpar = False
temPar = False

for i in range(0,n):
    v = int(input('Informe o '+ str(i+1) + '° valor: '))
    if(v%2==0):
        temPar = True
    else:
        temImpar = True

if temPar and not temImpar:
    print('0 : todos os números lidos são pares')
elif temImpar and not temPar:
    print('1: todos os números lidos são ímpares')
else:
    print('-1: números lidos contém pares e ímpares')
