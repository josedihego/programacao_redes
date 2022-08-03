# -*- coding: utf-8 -*-

from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


tela_principal = Tk()
tela_principal.title("Startup David & Antônio")
largura_tela = tela_principal.winfo_screenwidth()
altura_tela = tela_principal.winfo_screenheight()
largura = 500
altura = 500
x = (largura_tela / 2) - (largura / 2)
y = (altura_tela / 2) - (altura / 2)
tela_principal.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
tela_principal.resizable(False, False)
tela_principal.configure(background='white')

topo = Frame(tela_principal, width=500, height=50, bd=8, relief="raise")
topo.pack(side=TOP)

txt_nome_tela = Label(topo, width=500, bg='#000', fg='#800', font=(
    'arial', 20), text="Calculo da Média")
txt_nome_tela.pack()

botoes = Frame(tela_principal, width=300, height=100, bd=8, relief="raise")
botoes.pack(side=BOTTOM)

NOTA1 = StringVar()
nota1 = Entry(tela_principal, textvariable=NOTA1, borderwidth=15, width=30)
nota1.pack()

NOTA2 = StringVar()
nota2 = Entry(tela_principal, textvariable=NOTA2,borderwidth=15, width=30)
nota2.pack()

NOTA3 = StringVar()
nota3 = Entry(tela_principal, textvariable=NOTA3,borderwidth=15, width=30)
nota3.pack()

MEDIA = StringVar()
media = Entry(tela_principal, textvariable=MEDIA,borderwidth=15, width=30)
media.pack()


def calcular_media():
    nota1 = float(NOTA1.get())
    nota2 = float(NOTA2.get())
    nota3 = float(NOTA3.get())
    media = (nota1+ nota2 +  nota3)/3
    MEDIA.set(media)

btn_media = Button(botoes, width=10, text="Calcular Média",
                   command=calcular_media)

btn_media.pack(side= BOTTOM)



# ==================================INICIALIZAÇÃO=====================================
if __name__ == '__main__':
    tela_principal.mainloop()


