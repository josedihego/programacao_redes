# -*- coding: utf-8 -*-

#!/usr/bin/python
import requests
import sys
import shutil
import re
import threading
from bs4 import BeautifulSoup

numero_threads = 0
MAXIMO_THREADS = 5

def baixar_conteudo(link):
    r = requests.get( link )
    if r.status_code == 200:
        return BeautifulSoup( r.text )
    else:
        sys.exit( 'Respostas Inválida' )

def filtrar_imagens(html):
    imgs = html.findAll('img' )
    if imgs:
        return imgs
    else:
        sys.exit('Sem imagens na página')

def baixar_imagem(link, nome_pasta, name):
    global numero_threads
    numero_threads = numero_threads + 1
    try:
        r = requests.get( link, stream=True )
        if r.status_code == 200:
            r.raw.decode_content = True
            f = open('/home/jdso/Desktop/imagens/'+nome_pasta+ '/'+ name, 'wb' )
            shutil.copyfileobj(r.raw, f)
            f.close()
            print('Baixando imagem: %s' % name)
    except Exception as error:
        print('Erro %s : %s' % (name, error))
    numero_threads = numero_threads - 1

def main():
    arquivo = open('arquivos/urls', 'r')
    lista_urls = arquivo.readlines()
    for url in lista_urls:
        html = baixar_conteudo(url.replace('\n',''))
        tags = filtrar_imagens(html)
        for tag in tags:
            src = tag.get( 'src' )
            if src:
                src = re.match( r'((?:https?:\/\/.*)?\/(.*\.(?:png|jpg)))', src )
                if src:
                    (link, name) = src.groups()
                    if not link.startswith('http'):
                        link = 'https://www.drivespark.com' + link
                    nome_pasta = url.replace('\n','').replace('/','').replace('http:','')
                    _t = threading.Thread(target=baixar_imagem, args=(link, nome_pasta, name.split('/')[-1]))
                    _t.daemon = True
                    _t.start()

                    while numero_threads >= MAXIMO_THREADS:
                        pass

        while numero_threads > 0:
            pass


if __name__ == '__main__':
    main()
