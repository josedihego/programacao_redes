
def insertion_sort(A, options):
    for j in range(1,len(A)):
        key = A[j]
        i= j-1
        while(i >=0 and compareOrder(key, A[i], options)):
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key

def compareOrder(key, Ai, options):
    if options=='ASC': return Ai> key
    else: return Ai < key

L = ['Ruan', 'Samuel', 'Marcos', 'Gabriel Telis',
     'Filipe', 'Gabriel Lima', 'Airton', 'Pedro']

print(L)

insertion_sort(L,'DEC')

print(L)


arquivo = open('/home/jdso/Desktop/BSI_04_MAR.txt', 'w')
arquivo.write(str(L))
arquivo.close()