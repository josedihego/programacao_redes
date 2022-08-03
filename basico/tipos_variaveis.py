# -*- coding: utf-8 -*-
import smtplib
email = 'fl.lira@gmail.com'
senha = 'fl@d8362'


server = smtplib.SMTP('smtp.gmail.com', 587 )
server.starttls()
server.login(email, senha)

emails = ['flaviuslira@outlook.com']
mensagem = "Vai estudar!"

for dest in emails:
    server.sendmail(email, dest, mensagem)

server.quit()