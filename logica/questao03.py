
n = int(input('Informe o valor do número natural n: '))
m = int(input('Informe o valor do número natural m: '))
max = 0
ponto = (0,0)

for x in range(0,m):
    for y in range(0,n):
      res = x*y - x**2 + y
      if(res >max):
          max = res
          ponto = (x,y)

print(max)
print(ponto)
