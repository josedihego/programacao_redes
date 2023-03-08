#https://wiki.python.org.br/EstruturaDeRepeticao

popA = 80000
popB = 200000
taxaA = 0.03
taxaB = 0.015
anos = 0

while(popA <= popB):
    popA = popA * (1 + taxaA)
    popB = popB * (1 + taxaB)
    anos = anos + 1

print(f'Em {anos} anos a população da A ultrapassará a de B')
