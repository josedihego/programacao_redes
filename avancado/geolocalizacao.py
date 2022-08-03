# -*- coding: utf-8 -*-

#pip install geoip2

import  geoip2.database

leitor = geoip2.database.Reader('GeoLite2-Country.mmdb')

# ping www.google.com
resposta = leitor.country('216.58.222.100')
print resposta.country.name


#ping ifba
resposta = leitor.country('200.128.35.6')
print 'IFBA:', resposta.country.name

#ping www.wikipedia.com.br
resposta = leitor.country('208.80.154.224')
print resposta.country.name

# ping www.acordacidade.com.br
resposta = leitor.country('104.28.6.2')
print 'País do acorda cidade:', resposta.country.name

# ping euchegola.online
resposta = leitor.country('65.111.191.233')
print  'País do euchegolá: ', resposta.country.name