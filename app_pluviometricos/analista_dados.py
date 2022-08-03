
arquivo = open('feira.txt', 'r')

linhas = arquivo.readlines()
anos = []
val_jan = []
val_fev = []
val_mar = []
val_abr = []
val_mai = []
val_jun = []
val_jul = []
val_ago = []
val_set = []
val_out = []
val_nov = []
val_dez = []
for l in linhas:
    valores = l.split(' ')
    if(valores[0]=='ano'):
        anos = valores
    elif(valores[0]=='Jan.'):
        val_jan = valores
    elif (valores[0] == 'Fev.'):
        val_fev = valores
    elif (valores[0] == 'Mar.'):
        val_mar = valores
    elif (valores[0] == 'Abr.'):
        val_abr = valores
    elif (valores[0] == 'Mai.'):
        val_mai = valores
    elif (valores[0] == 'Jun.'):
        val_jun = valores
    elif (valores[0] == 'Jul.'):
        val_jul = valores
    elif (valores[0] == 'Ago.'):
        val_ago = valores
    elif (valores[0] == 'Set.'):
        val_set = valores
    elif (valores[0] == 'Out.'):
        val_out = valores
    elif (valores[0] == 'Nov.'):
        val_nov = valores
    else:
        val_dez = valores

# função somatorio_ano receberá:
# (1) um determindo ano
# (2) descobrirá a posição do ano recebido no array
#     por exemplo: o ano de 2003 esta na posição 8
# (3) a função ira na lista de cada mes na posição encontrada
# e somará as chuvas daquele mês ao total geral
#     por exemplo: ano de 2003 esta na posição 8
#                  assim, as chuvas de janeiro estão na posição 8 do mes de janeiro
#                         as chuvas de fevereiro estão na posição 8 do mes de fevereiro
# e assim por diante
def limpar(texto):
    res = texto.replace('*','')
    res = res.replace(',','.')
    return float(res)

def somatorio_ano(ano):
    p = 0
    while(anos[p] != ano):
        p = p + 1
    soma = limpar(val_jan[p]) + limpar(val_fev[p]) + limpar(val_mar[p]) + limpar(val_abr[p]) + limpar(val_mai[p]) + limpar(val_jun[p]) + limpar(val_jul[p]) + limpar(val_ago[p]) + limpar(val_set[p]) + limpar(val_out[p]) + limpar(val_nov[p]) + limpar(val_dez[p])
    print(soma)

somatorio_ano('2005')