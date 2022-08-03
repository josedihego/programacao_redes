
arquivo = open('/home/jdso/Desktop/redes/dadosAcesso.txt', 'r')
texto =  arquivo.read()

linhas = texto.splitlines()

ips= []
datas = []

for l in linhas:
    ips.append(l.split(' ')[0])
    datas.append(l.split(' ')[1])

print max(set(ips), key=ips.count)
print max(set(datas), key=datas.count)
