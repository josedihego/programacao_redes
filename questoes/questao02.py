# -*- coding: utf-8 -*-


n1 = 0
n2 = 0
n3 = 0
media_aluno = 0
maior_media = 0
soma_medias = 0
QNT_ALU = 40

for a in range(1,QNT_ALU+1):
    print 'informe a 1ª nota'
    n1 = float(input())
    print 'informe a 2ª nota'
    n2 = float(input())
    print 'informe a 3ª nota'
    n3 = float(input())
    media_aluno = (n1+n2+n3) / 3
    print 'Média do aluno n°',a, ':', media_aluno
    soma_medias = soma_medias + media_aluno
    if media_aluno > maior_media:
        maior_media = media_aluno

print 'Maior média: ',maior_media
print 'Média turma: ', soma_medias/QNT_ALU

