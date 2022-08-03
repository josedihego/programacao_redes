# -*- coding: utf-8 -*-

from ftplib import FTP
#1. ter um código para ler usuário e senha
# como? Usando uma variável usuario e outra chamada senha

ftp = FTP('') # cria um objeto FTP
ftp.connect('10.25.201.53',1026) # tenta conectar-se ao servidor FTP
ftp.login('maria', 'ma08') # tenta logar pode ser em anonimato login()
ftp.cwd('/') # estabelece o diretório dentro do servidor

def enviarArquivo():
 nome_arquivo = input('Informe o nome do arquivo:')
 ftp.storbinary('STOR '+nome_arquivo, open(nome_arquivo, 'rb'))
 # armazena arquivo remotamente no servidor FTP em modo binário de leitura
enviarArquivo()

#1. criar a função abaixo baseada na função  baixarArquivo()
def baixarResumo():
 print('fazer o download do arquivo resumo.txt')
 # lembrete usar : open(nome_arquivo, 'w')

#2.
def computar_reenviar_resumo():
 print('1. baixar resumo atual ')
 print('2. juntar a arquivo enviado ao resumo atual')
 print('3. enviar de volta resumo atualizado ')

def baixarArquivo():
 nome_arquivo = input('Informe o nome do arquivo:')
 arquivo_local = open(nome_arquivo, 'wb')
 # abre arquivo em modo binário de escrita
 ftp.retrbinary('RETR ' + nome_arquivo, arquivo_local.write, 1024)
 # maxblocksize = 1024
 arquivo_local.close()

baixarArquivo()

def criarDiretorio():
 nome_diretorio = input('informe o nome do novo diretório: ')
 ftp.mkd(nome_diretorio)

def removerDiretorio():
 nome_diretorio = input('informe o nome do diretório a ser removido: ')
 ftp.rmd(nome_diretorio)

def removerArquivo():
 nome_arquivo = input('informe o nome do arquivo a ser removido: ')
 ftp.delete(nome_arquivo)

def renomearArquivo():
  nome_atual = input('informe o nome atual do  arquivo: ')
  nome_novo = input('informe o novo nome do  arquivo: ')
  ftp.rename(nome_atual, nome_novo)

opcao = 0
while(opcao != 1):
 print('Informe uma das opções')
 print('\t 1. sair')
 print('\t 2. listar arquivos')
 print('\t 3. enviar arquivo')
 print('\t 4. baixar arquivo')
 print('\t 5. deletar arquivo')
 print('\t 6. criar diretório')
 print('\t 7. deletar diretório')
 print('\t 8. renomear arquivo')
 #print('\t 9. baixar resumo')
 # input() sempre retorna uma string, assim o int() se faz necessário
 opcao = int(input())
 if opcao == 1:
  ftp.quit()
 elif(opcao == 2):
  ftp.retrlines('LIST')
 elif(opcao == 3):
  enviarArquivo()
  #computar_reenviar_resumo()
 elif(opcao == 4):
  baixarArquivo()
 elif(opcao==5):
  removerArquivo()
 elif(opcao==6):
  criarDiretorio()
 elif (opcao == 7):
  removerDiretorio()
 elif (opcao == 8):
  renomearArquivo()
 #elif (opcao==9) :
  #baixarResumo()


