

Figura 1.

arquivo_limites = open('log_sites_limite.txt', 'r')
conteudo_limites = arquivo_limites.read()
conteudo_limites = conteudo_limites.split('\n')

Figura 2.

192.168.1.1#300
192.175.3.4#800


i = 0
while ______:
    print("------***-------PACOTE ", i, "------***-------")
    i = i+1
    pacote = meuSocket.recvfrom(65565)



L = [120,123,155,67,82,190]
for e in L:
    if (_____):
        print(e)




print('Você deve informar uma lista de valores')
valor_lido = 0
lista = []
while(valor_lido != 'Parar'):
  print('Informe um valor inteiro ou digite a palavra Parar para sair')
  valor_lido = input()
  if(valor_lido!='Parar'):
    numero = int(valor_lido)
    lista.append(numero)




L = [45, 80, 12, 27, 32, 49, 80, 100, -1, 30]
somatorio = 0
for v in L:
  somatorio = somatorio + v
media = _____ / len(L)




def funcao_misteriosa(lista):
  media = calc_media(lista)
  selecionados = []
  for v in lista:
    if(v > media):
      selecionados.append(v)
  return  selecionados



gerenteFTP = FTPHandler
gerenteFTP.authorizer = autoridade

servidor = FTPServer(('____________', _________), gerenteFTP)
servidor.serve_forever()



192.168.5.103, 1026