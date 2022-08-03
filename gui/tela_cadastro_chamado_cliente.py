# -*- coding: utf-8 -*-

from tkinter import ttk
from tkinter import *
from PIL import Image
from PIL import ImageTk

import sqlite3



class Chamado:

    nome_banco = 'chamados.db'


    def __init__(self, window):


        #criação do banco
        self.criar_banco()

        #inicialização da tela
        self.tela = window
        self.tela.title('REGISTRO DE CHAMADOS')


        # criação de um frame
        frame = LabelFrame(self.tela, text ='REGISTRO DE CHAMADOS', fg= 'pink')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 40) # padding: para todos os lados

        # campo título
        Label(frame, text = 'Título: ').grid(row = 1, column = 0)
        self.titulo = Entry(frame)
        self.titulo.focus()
        self.titulo.grid(row = 1, column = 1)

        # campo descrição
        Label(frame, text = 'Descrição: ').grid(row = 2, column = 0)
        self.descricao = Entry(frame)
        #self.descricao.focus()
        self.descricao.grid(row = 2, column = 1)


        # botão acicionar chamado
        ttk.Button(frame, text = 'Registrar Chamado', command = self.adicionar_chamado).grid(row = 3, columnspan = 2, sticky =W + E)
        # posicionamento do texto dentro do botão  N, E, S, W, NE, NW, SE, and SW

        # mesagem de retorno na tela
        self.mensagem = Label(text ='', fg ='red') # foregound color (cor de fundo)
        self.mensagem.grid(row = 3, column = 0, columnspan = 2, sticky =W + E)

        # tabela de dados
        self.tabela = ttk.Treeview(height = 20, columns = 2)
        self.tabela.grid(row = 4, column = 0, columnspan = 2)
        self.tabela.heading('#0', text ='Título', anchor = CENTER)
        self.tabela.column("#0", minwidth=0, width=400, stretch=NO)
        self.tabela.heading('#1', text ='Descrição', anchor = CENTER)
        self.tabela.column("#1", minwidth=0, width=400, stretch=NO)


        # botões da tabela
        ttk.Button(text = 'Remover', command = self.remover_chamado).grid(row = 5, column = 0, sticky =W + E)
        ttk.Button(text = 'Editar', command = self.editar_chamado).grid(row = 5, column = 1, sticky =W + E)

        # listar chamados
        self.listar_chamados()

    # criação do banco
    def criar_banco(self):
        conn = sqlite3.connect('chamados.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `chamado` (cham_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, titulo TEXT, descricao TEXT)")

    # execução de comando
    def execucao_comando(self, query, parameters = ()):
        with sqlite3.connect(self.nome_banco) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # listar chamados
    def listar_chamados(self):
        # cleaning Table
        dados = self.tabela.get_children()
        for elemento in dados:
            self.tabela.delete(elemento)
        # getting data
        comando_busca = 'SELECT titulo, descricao FROM chamado ORDER BY titulo DESC'
        elementos_retornados = self.execucao_comando(comando_busca)
        # filling data
        for elemento in elementos_retornados:
            self.tabela.insert("" , 0,  text=elemento[0], values=(elemento[1],))

    # validação
    def validar(self):
        tamTitulo = len(self.titulo.get())
        tamDesc = len(self.descricao.get())
        return  tamTitulo > 9 and  tamDesc > 14

    def adicionar_chamado(self):
        if self.validar():
            comando_insercao = 'INSERT INTO chamado VALUES(NULL, ?, ?)'
            parametros =  (self.titulo.get(), self.descricao.get())
            self.execucao_comando(comando_insercao, parametros)
            self.mensagem['text'] = 'Chamado {} adicionado com sucesso'.format(self.titulo.get())
            self.titulo.delete(0, END)
            self.descricao.delete(0, END)
        else:
            self.mensagem['text'] = 'Todos os dados são necessários'
        self.listar_chamados()

    def remover_chamado(self):
        self.mensagem['text'] = ''
        try:
           self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Selecione um chamado'
            return
        self.mensagem['text'] = ''
        name = self.tabela.item(self.tabela.selection())['text']
        query = 'DELETE FROM chamado WHERE titulo = ?'
        self.execucao_comando(query, (name,))
        self.mensagem['text'] = 'Chamado {} removido com sucesso'.format(name)
        self.listar_chamados()

    def editar_chamado(self):
        self.mensagem['text'] = ''
        try:
            self.tabela.item(self.tabela.selection())['values'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Selecione um chamado'
            return
        titulo_antigo = self.tabela.item(self.tabela.selection())['text']
        descricao_antiga = self.tabela.item(self.tabela.selection())['values'][0]
        self.tela_edicao = Toplevel()
        self.tela_edicao.title = 'Editar chamado'
        # título antigo
        Label(self.tela_edicao, text ='Título antigo:').grid(row = 0, column = 1)
        Entry(self.tela_edicao, textvariable = StringVar(self.tela_edicao,
                    value = titulo_antigo), state ='readonly').grid(row = 0, column = 2)
        # título novo
        Label(self.tela_edicao, text ='Título novo:').grid(row = 1, column = 1)
        titulo_novo = Entry(self.tela_edicao)
        titulo_novo.grid(row = 1, column = 2)

        #descrição antiga
        Label(self.tela_edicao, text ='Descrição antiga:').grid(row = 2, column = 1)
        Entry(self.tela_edicao, textvariable = StringVar(self.tela_edicao,
                        value = descricao_antiga), state ='readonly').grid(row = 2, column = 2)
        # descrição nova
        Label(self.tela_edicao, text ='Descrição nova:').grid(row = 3, column = 1)
        descricao_nova= Entry(self.tela_edicao)
        descricao_nova.grid(row = 3, column = 2)

        Button(self.tela_edicao, text ='Atualizar',
               command = lambda: self.editar_chamado_banco(titulo_novo.get(),
                                titulo_antigo, descricao_nova.get())).grid(row = 4, column = 2, sticky = W)
        self.tela_edicao.mainloop()

    def editar_chamado_banco(self, novo_titulo, titulo, nova_descricao):
        comando_atualizacao = 'UPDATE chamado SET titulo = ?, descricao = ? WHERE titulo = ?'
        parametros = (novo_titulo, nova_descricao, titulo)
        self.execucao_comando(comando_atualizacao, parametros)
        self.tela_edicao.destroy()
        self.mensagem['text'] = 'Chamado{} atualizado com sucesso'.format(titulo)
        self.listar_chamados()

if __name__ == '__main__':
    tela = Tk()
    aplicacao = Chamado(tela)
    tela.mainloop()