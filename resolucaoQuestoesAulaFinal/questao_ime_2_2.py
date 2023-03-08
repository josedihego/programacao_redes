# https://www.ime.usp.br/~macmulti/exercicios/repetenc/index.html

n = int(input('Informe o valor de n'))

for h in range(1,n+1):
    for a in range(1,h):
        for b in range(1,h):
            if(a*a + b*b == h*h):
                print(f'{a}² + {b}² = {h}²')