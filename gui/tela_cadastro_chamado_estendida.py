# -*- coding: utf-8 -*-

from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


tela_principal = Tk()
tela_principal.title("Gerenciamento de chamados")
largura_tela = tela_principal.winfo_screenwidth()
altura_tela = tela_principal.winfo_screenheight()
largura = 1300
altura = 500
x = (largura_tela / 2) - (largura / 2)
y = (altura_tela / 2) - (altura / 2)
tela_principal.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
tela_principal.resizable(True, False)


# ==================================MÉTODOS============================================
def inicializar_base_dados():
    global conexao, cursor
    conexao = sqlite3.connect('chamados_estendida.db')
    cursor = conexao.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `chamado` (cha_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, titulo TEXT, descricao TEXT, urgencia TEXT, responsavel TEXT, usuario TEXT, senha TEXT)")


def acicionar_chamado():
    if TITULO.get() == "" or DESCRICAO.get() == "" or URGENCIA.get() == "" or RESPONSAVEL.get() == "" or USUARIO.get() == "" or SENHA.get() == "":
        txt_resultado.config(
            text="Você deve informar todos os campos", fg="red")
    else:
        inicializar_base_dados()
        cursor.execute(
            "INSERT INTO `chamado` (titulo, descricao, urgencia, responsavel, usuario, senha) VALUES(?, ?, ?, ?, ?, ?)",
            (str(TITULO.get()), str(DESCRICAO.get()), str(URGENCIA.get()), str(RESPONSAVEL.get()), str(USUARIO.get()),
             str(SENHA.get())))
        conexao.commit()
        TITULO.set("")
        DESCRICAO.set("")
        URGENCIA.set("")
        RESPONSAVEL.set("")
        USUARIO.set("")
        SENHA.set("")
        cursor.close()
        conexao.close()
        txt_resultado.config(text="Inserido com sucesso", fg="green")


def listar_chamados():
    tabela.delete(*tabela.get_children())
    inicializar_base_dados()
    if(USUARIO.get() == ''):
        cursor.execute("SELECT * FROM `chamado` ORDER BY `titulo` DESC")
    else:
        cursor.execute(
            "SELECT * FROM `chamado` WHERE usuario=? ORDER BY `titulo` DESC", (USUARIO.get(),))
    fetch = cursor.fetchall()
    for data in fetch:
        tabela.insert('', 'end', values=(
            data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    conexao.close()
    txt_resultado.config(text="Chamados lidos com sucesso", fg="green")


def remover_chamado():
    inicializar_base_dados()
    try:
        tabela.item(tabela.selection())['values'][0]
    except IndexError as e:
        txt_resultado.config(text="Selecione um chamado primeiro", fg="red")
        return
    nome = str(tabela.item(tabela.selection())['values'][0])
    result = tkMessageBox.askquestion(
        'Você realmente deseja remover ' + nome + '?', icon="error")
    if result == 'yes':
        cursor.execute('DELETE FROM chamado WHERE titulo = ?', (nome,))
        conexao.commit()
        cursor.close()
        conexao.close()
        txt_resultado.config(text="Removido com sucesso", fg="green")
        listar_chamados()


def sair():
    result = tkMessageBox.askquestion(
        'Você realmente quer sair?', icon="error")
    if result == 'yes':
        tela_principal.destroy()
        exit()


# ==================================VARIÁVEIS==========================================
TITULO = StringVar()
DESCRICAO = StringVar()
URGENCIA = StringVar()
RESPONSAVEL = StringVar()
USUARIO = StringVar()
SENHA = StringVar()

# ==================================FRAME==============================================
topo = Frame(tela_principal, width=900, height=50, bd=8, relief="raise")
topo.pack(side=TOP)
esquerda = Frame(tela_principal, width=300, height=500, bd=8, relief="raise")
esquerda.pack(side=LEFT)
direita = Frame(tela_principal, width=600, height=500, bd=8, relief="raise")
direita.pack(side=RIGHT)
formularios = Frame(esquerda, width=300, height=450)
formularios.pack(side=TOP)
botoes = Frame(esquerda, width=300, height=100, bd=8, relief="raise")
botoes.pack(side=BOTTOM)
opcoes = Frame(formularios)
alta = Radiobutton(opcoes, text="Alta", variable=URGENCIA,
                   value="A", font=('arial', 16)).pack(side=LEFT)
baixa = Radiobutton(opcoes, text="Baixa", variable=URGENCIA,
                    value="B", font=('arial', 16)).pack(side=LEFT)

# ==================================NOMES=======================================
txt_nome_tela = Label(topo, width=900, font=(
    'arial', 24), text="Registro de Chamados")
txt_nome_tela.pack()
txt_titulo = Label(formularios, text="Título:", font=('arial', 16), bd=15)
txt_titulo.grid(row=0, stick="e")
txt_descricao = Label(formularios, text="Descrição:",
                      font=('arial', 16), bd=15)
txt_descricao.grid(row=1, stick="e")
txt_urgencia = Label(formularios, text="Urgência:", font=('arial', 16), bd=15)
txt_urgencia.grid(row=2, stick="e")
txt_responsavel = Label(formularios, text="Responsável:",
                        font=('arial', 16), bd=15)
txt_responsavel.grid(row=3, stick="e")
txt_usuario = Label(formularios, text="Usuário:", font=('arial', 16), bd=15)
txt_usuario.grid(row=4, stick="e")
txt_senha = Label(formularios, text="Senha:", font=('arial', 16), bd=15)
txt_senha.grid(row=5, stick="e")
txt_resultado = Label(botoes)
txt_resultado.pack(side=TOP)

# ==================================CAMPOS DE ENTRADA=======================================
titulo = Entry(formularios, textvariable=TITULO, width=30)
titulo.grid(row=0, column=1)
descricao = Entry(formularios, textvariable=DESCRICAO, width=30)
descricao.grid(row=1, column=1)
opcoes.grid(row=2, column=1)
responsavel = Entry(formularios, textvariable=RESPONSAVEL, width=30)
responsavel.grid(row=3, column=1)
usuario = Entry(formularios, textvariable=USUARIO, width=30)
usuario.grid(row=4, column=1)
senha = Entry(formularios, textvariable=SENHA, show="*", width=30)
senha.grid(row=5, column=1)

# ==================================BOTÕES=====================================
btn_criar = Button(botoes, width=10, text="Cadastrar",
                   command=acicionar_chamado)
btn_criar.pack(side=LEFT)
btn_listar = Button(botoes, width=10, text="Listar", command=listar_chamados)
btn_listar.pack(side=LEFT)
btn_atualizar = Button(botoes, width=10, text="Atualizar", state=DISABLED)
btn_atualizar.pack(side=LEFT)
btn_remover = Button(botoes, width=10, text="Remover", command=remover_chamado)
btn_remover.pack(side=LEFT)
btn_sair = Button(botoes, width=10, text="Sair", command=sair)
btn_sair.pack(side=LEFT)

# ==================================LISTA DE CHAMADOS=======================================
barra_rolagem_y = Scrollbar(direita, orient=VERTICAL)
barra_rolagem_x = Scrollbar(direita, orient=HORIZONTAL)
tabela = ttk.Treeview(direita, columns=("Título", "Descrição", "Urgência", "Responsável", "Usuário", "Senha"),
                      selectmode="extended", height=500, yscrollcommand=barra_rolagem_y.set, xscrollcommand=barra_rolagem_x.set)
barra_rolagem_y.config(command=tabela.yview)
barra_rolagem_y.pack(side=RIGHT, fill=Y)
barra_rolagem_x.config(command=tabela.xview)
barra_rolagem_x.pack(side=BOTTOM, fill=X)
tabela.heading('Título', text="Título", anchor=W)
tabela.heading('Descrição', text="Descrição", anchor=W)
tabela.heading('Urgência', text="Urgência", anchor=W)
tabela.heading('Responsável', text="Responsável", anchor=W)
tabela.heading('Usuário', text="Usuário", anchor=W)
tabela.heading('Senha', text="Senha", anchor=W)
tabela.column('#0', stretch=NO, minwidth=0, width=0)
tabela.column('#1', stretch=NO, minwidth=0, width=80)
tabela.column('#2', stretch=NO, minwidth=0, width=120)
tabela.column('#3', stretch=NO, minwidth=0, width=80)
tabela.column('#4', stretch=NO, minwidth=0, width=150)
tabela.column('#5', stretch=NO, minwidth=0, width=120)
tabela.column('#6', stretch=NO, minwidth=0, width=120)
tabela.pack()

# ==================================INICIALIZAÇÃO=====================================
if __name__ == '__main__':
    tela_principal.mainloop()
