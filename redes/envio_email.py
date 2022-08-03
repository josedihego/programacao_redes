senha = 'sua senha'













# -*- coding: utf-8 -*-
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
senha = 'minha senha'

# STOP
remetente = 'education.events.4all@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Transport Layer Security
# toda a comunicação a partir daqui será encriptada
server.login(remetente, senha)
lista = ['marilsonsantana43@gmail.com']
arquivo_entrada = open('arquivos/vendas_joao.txt', 'r')
linhas = arquivo_entrada.readlines()
for dest in lista:
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = dest
    msg['Subject'] = 'Relatório de vendas'
    corpo = str(linhas)
    msg.attach(MIMEText(corpo, 'plain'))
    server.sendmail(remetente, dest, msg.as_string())
server.quit()
