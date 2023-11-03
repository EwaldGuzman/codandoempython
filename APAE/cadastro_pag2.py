# Bibliotecas Python
from customtkinter import *
from openpyxl import load_workbook
from tkinter import messagebox
from datetime import datetime
from PIL import Image
from tkinter import ttk

import pathlib
import pandas as pd


# Bibliotecas Minhas
import geometria_sistema
from geometria_sistema import Responsive_windows, Responsive_container

class Pesquisar_Cadastro:

    # Inicializador de propriedades
    def __init__(self, win):

        self.cadastro = pathlib.Path('Tabelas_xlsx/Cadastros_xlsx/Consultas - Proficional #00.xlsx').absolute()

        self.data = datetime.now().strftime('%d/%m/%Y')
        self.font_lb = 20
        self.font_entry = 16
        self.tipo_font = 'times new roman'

        self.windows = win
        self.limpar_windows()

        self.contains_principal()
        self.contatos()
        self.list_menu()
        self.scroll()
        self.contains()
        self.lista()
        self.campos()
        self.carregar_treeview()

    # Limpar janela aberta
    def limpar_windows(self):

        for obj in self.windows.winfo_children():
            obj.destroy()

    # Containes principais
    def contains_principal(self):

        size = Responsive_windows(self.windows)

        self.header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(3), fg_color='#000000', corner_radius=0)
        self.imagem_fr = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(28))
        self.sub_header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(5), fg_color='#FFFFFF', corner_radius=0)
        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(90), fg_color=None, corner_radius=0)

        self.header.pack(fill=BOTH)
        self.imagem_fr.pack()
        self.sub_header.pack(fill=BOTH)
        self.body.pack(fill=BOTH)

        size = Responsive_container(self.imagem_fr)

        self.img_fundo = CTkImage(light_image=Image.open('Imagens/cadastro_paciente.png'), dark_image=Image.open(
            'Imagens/cadastro_paciente.png'), size=(size.container_w(100), size.container_h(100)))

        self.imagem_lb = CTkLabel(self.imagem_fr, text='', image=self.img_fundo)
        self.imagem_lb.pack()

    # Opções de contato
    def contatos(self):

        size = Responsive_container(self.header)

        self.zap_img = CTkImage(light_image=Image.open('Imagens/whatsapp.png'), dark_image=Image.open('Imagens/whatsapp.png'), size=(size.container_h(80), size.container_h(80)))
        self.face_img = CTkImage(light_image=Image.open('Imagens/facebook.png'), dark_image=Image.open('Imagens/facebook.png'), size=(size.container_h(80), size.container_h(80)))
        self.insta_img = CTkImage(light_image=Image.open('Imagens/instagram.png'), dark_image=Image.open('Imagens/instagram.png'), size=(size.container_h(90), size.container_h(90)))

        self.zap_lb = CTkLabel(self.header, text='', image=self.zap_img)
        self.zap2_lb = CTkLabel(self.header, text='(98) 98602-0924', text_color='white')
        self.insta_lb = CTkLabel(self.header, text='', image=self.insta_img)
        self.insta2_lb = CTkLabel(self.header, text='instagran', text_color='white')
        self.face_lb = CTkLabel(self.header, text='', image=self.face_img)
        self.face2_lb = CTkLabel(self.header, text='facebook', text_color='white')

        self.zap_lb.pack(side=LEFT, pady=size.container_h(10), padx=(size.container_w(1), size.container_w(0.4)))
        self.zap2_lb.pack(side=LEFT)
        self.insta2_lb.pack(side=RIGHT, padx=(0, size.container_w(1)))
        self.insta_lb.pack(side=RIGHT, pady=size.container_h(10), padx=(size.container_w(1), size.container_w(0.4)))
        self.face2_lb.pack(side=RIGHT)
        self.face_lb.pack(side=RIGHT, pady=size.container_h(10), padx=(size.container_w(1), size.container_w(0.4)))

    # Menu de opções
    def list_menu(self):

        size = Responsive_container(self.sub_header)

        self.list = CTkFrame(self.sub_header, fg_color='transparent')
        self.list.pack(side=RIGHT, padx=size.container_w(5), pady=size.container_h(4))

        self.voltar_btn = CTkButton(self.list, text='VOLTAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.voltar, fg_color='transparent', hover_color='#F7F7F7')
        self.sair_btn = CTkButton(self.list, text='SAIR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.fechar_app, fg_color='transparent', hover_color='#F7F7F7')

        self.voltar_btn.pack(side=LEFT, padx=None, pady=size.container_h(2))
        self.sair_btn.pack(side=LEFT, padx=None, pady=size.container_h(2))

    # Barra de rolagem
    def scroll(self):

        size = Responsive_container(self.body)

        self.Yscroll = CTkScrollableFrame(self.body, width=size.container_w(100), height=size.container_h(100), fg_color='#FFFFFF', corner_radius=1, border_color='black')
        self.Yscroll.pack()

    # Containes de campo
    def contains(self):

        size = Responsive_container(self.body)


        self.campo_fr = CTkFrame(self.Yscroll, width=size.container_w(90), height=size.container_h(20), fg_color='transparent')
        self.pesquisa_fr = CTkFrame(self.campo_fr, width=size.container_w(90), height=size.container_h(20), fg_color='transparent')
        self.tabela_fr = CTkFrame(self.Yscroll, width=size.container_w(90), height=size.container_h(20), fg_color='transparent')

        self.campo_fr.pack(fill=X, padx=size.container_w(2))
        self.pesquisa_fr.pack(pady=size.container_h(3), side=LEFT)
        self.tabela_fr.pack()

    # Treeview - Scrollbar
    def lista(self):

        size = Responsive_container(self.tabela_fr)

        self.scroll_y = CTkScrollbar(self.tabela_fr, orientation='vertical')
        self.scroll_x = CTkScrollbar(self.tabela_fr, orientation='horizontal')

        self.scroll_y.pack(side=RIGHT, fill=Y, padx=(0, size.container_w(2)))
        self.scroll_x.pack(side=BOTTOM, fill=X, padx=size.container_w(2))

        self.lista_treeview = ttk.Treeview(self.tabela_fr, columns=(
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
        ), show='headings', height=15, yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.lista_treeview.column('#1', width=int(size.container_w(10)))
        self.lista_treeview.column('#2', width=int(size.container_w(10)))
        self.lista_treeview.column('#3', width=int(size.container_w(10)))
        self.lista_treeview.column('#4', width=int(size.container_w(10)))
        self.lista_treeview.column('#5', width=int(size.container_w(5)))
        self.lista_treeview.column('#6', width=int(size.container_w(10)))
        self.lista_treeview.column('#7', width=int(size.container_w(10)))
        self.lista_treeview.column('#8', width=int(size.container_w(5)))
        self.lista_treeview.column('#9', width=int(size.container_w(10)))
        self.lista_treeview.column('#10', width=int(size.container_w(10)))
        self.lista_treeview.column('#11', width=int(size.container_w(7)))
        self.lista_treeview.column('#12', width=int(size.container_w(10)))
        self.lista_treeview.column('#13', width=int(size.container_w(10)))
        self.lista_treeview.column('#14', width=int(size.container_w(10)))
        self.lista_treeview.column('#15', width=int(size.container_w(7)))
        self.lista_treeview.column('#16', width=int(size.container_w(10)))
        self.lista_treeview.column('#17', width=int(size.container_w(10)))
        self.lista_treeview.column('#18', width=int(size.container_w(12)))
        self.lista_treeview.column('#19', width=int(size.container_w(12)))
        self.lista_treeview.column('#20', width=int(size.container_w(12)))
        self.lista_treeview.column('#21', width=int(size.container_w(12)))
        self.lista_treeview.column('#22', width=int(size.container_w(10)))
        self.lista_treeview.column('#23', width=int(size.container_w(10)))
        self.lista_treeview.column('#24', width=int(size.container_w(10)))
        self.lista_treeview.column('#25', width=int(size.container_w(7)))
        self.lista_treeview.column('#26', width=int(size.container_w(10)))
        self.lista_treeview.column('#27', width=int(size.container_w(10)))
        self.lista_treeview.column('#28', width=int(size.container_w(7)))
        self.lista_treeview.column('#29', width=int(size.container_w(10)))

        self.lista_treeview.heading('#1', text='ATENDIMENTO')
        self.lista_treeview.heading('#2', text='SUS')
        self.lista_treeview.heading('#3', text='PACIENTE')
        self.lista_treeview.heading('#4', text='NASCIMENTO')
        self.lista_treeview.heading('#5', text='IDADE')
        self.lista_treeview.heading('#6', text='TELEFONE')
        self.lista_treeview.heading('#7', text='RUA')
        self.lista_treeview.heading('#8', text='NÚMERO')
        self.lista_treeview.heading('#9', text='BAIRRO')
        self.lista_treeview.heading('#10', text='CIDADE')
        self.lista_treeview.heading('#11', text='CEP')
        self.lista_treeview.heading('#12', text='PROCEDIMENTO')
        self.lista_treeview.heading('#13', text='ESCOLARIDADE')
        self.lista_treeview.heading('#14', text='TURNO')
        self.lista_treeview.heading('#15', text='ESCOLA')
        self.lista_treeview.heading('#16', text='DEFICIÊNCIA')
        self.lista_treeview.heading('#17', text='RAÇA/COR/ETNIA')
        self.lista_treeview.heading('#18', text='LIMITAÇÃO/COGNITIVA')
        self.lista_treeview.heading('#19', text='LIMITAÇÃO/LOCOMOÇÃO')
        self.lista_treeview.heading('#20', text='LIMITAÇÃO/VISÃO')
        self.lista_treeview.heading('#21', text='LIMITAÇÃO/AUDIÇÃO')
        self.lista_treeview.heading('#22', text='TRATAMENTO')
        self.lista_treeview.heading('#23', text='QUAL')
        self.lista_treeview.heading('#24', text='QUANDO')
        self.lista_treeview.heading('#25', text='PARECER DO TRATAMENTO')
        self.lista_treeview.heading('#26', text='QUEIXA PRINCIPAL')
        self.lista_treeview.heading('#27', text='INICIO DA QUEIXA')
        self.lista_treeview.heading('#28', text='MEDICAMENTO')
        self.lista_treeview.heading('#29', text='TIPO')



        self.lista_treeview.bind('<Double-1>', None)
        self.lista_treeview.bind('<ButtonRelease-1>', self.editar_cadastro)

        self.lista_treeview.pack(side=RIGHT, padx=(size.container_w(2), 0))

        self.scroll_y.configure(command=self.lista_treeview.yview)
        self.scroll_x.configure(command=self.lista_treeview.xview)

    # campos de pesquisa
    def campos(self):
        size = Responsive_container(self.pesquisa_fr)

        self.sus_lb = CTkLabel(self.pesquisa_fr, text='Cartão SUS', font=('', size.container_w(1)))
        self.sus_entry = CTkEntry(self.pesquisa_fr, placeholder_text='SUS...', font=('', size.container_w(1)), width=size.container_w(20), height=size.container_h(25), border_width=1, corner_radius=100)
        self.paciente_lb = CTkLabel(self.pesquisa_fr, text='Nome do Paciente', font=('', size.container_w(1)))
        self.paciente_entry = CTkEntry(self.pesquisa_fr, placeholder_text='Paciente...', font=('', size.container_w(1)), width=size.container_w(20), height=size.container_h(25), border_width=1, corner_radius=100)
        self.data_lb = CTkLabel(self.pesquisa_fr, text='Data de Nascimento', font=('', size.container_w(1)))
        self.data_entry = CTkEntry(self.pesquisa_fr, placeholder_text='Data...', font=('', size.container_w(1)), width=size.container_w(20), height=size.container_h(25), border_width=1, corner_radius=100)


        self.sus_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.sus_entry.grid(column=0, row=1, sticky=W)
        self.paciente_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(2), 0))
        self.paciente_entry.grid(column=1, row=1, sticky=W, padx=size.container_w(1))
        self.data_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.data_entry.grid(column=2, row=1, sticky=W)

        self.filtrar_btn = CTkButton(self.campo_fr, text='Filtrar Resultados', command=self.carregar_treeview_filtro)
        self.limpar_btn = CTkButton(self.campo_fr, text='Limpar Filtro', command=self.limpar_treeview_filtro)

        self.filtrar_btn.pack(side=LEFT, padx=(size.container_w(2), size.container_w(0.3)), pady=(size.container_h(13), 0))
        self.limpar_btn.pack(side=LEFT, pady=(size.container_h(13), 0))

    def carregar_treeview(self):

        dados = pd.read_excel(self.cadastro)
        dados = pd.DataFrame(dados)

        for linha in dados.index:
            self.lista_treeview.insert("", 'end', values=list(dados.loc[linha]))

    # Carregar filtro na lista
    def carregar_treeview_filtro(self):

        dados = pd.read_excel(self.cadastro)
        dados = pd.DataFrame(dados)

        dados = self.filtro3x(dados)

        self.limpar_treeview()

        for linha in dados.index:
            self.lista_treeview.insert("", 'end', values=list(dados.loc[linha]))

    # Limpar filtro da lista
    def limpar_treeview_filtro(self):

        self.sus_entry.delete(0, 'end')
        self.paciente_entry.delete(0, 'end')
        self.data_entry.delete(0, 'end')
        self.limpar_treeview()
        self.carregar_treeview()
        self.sus_entry.configure(placeholder_text='SUS...')
        self.paciente_entry.configure(placeholder_text='Paciente...')
        self.data_entry.configure(placeholder_text='Data...')

    # limpar Treeview
    def limpar_treeview(self):

        for filho in self.lista_treeview.get_children():
            self.lista_treeview.delete(filho)

    # Filtar registro
    def filtro3x(self, DADOS):

        entry = [self.sus_entry.get(), self.paciente_entry.get().upper(), self.data_entry.get()]

        dados_treeview = pd.DataFrame(DADOS)

        # Filtro Datas
        if entry[0] == "":
            pass
        else:
            dados_treeview = pd.DataFrame(dados_treeview.loc[dados_treeview['SUS'] == int(entry[0])])

        # Filtro Paciente
        if entry[1] == "":
            pass
        else:
            dados_treeview = pd.DataFrame(dados_treeview.loc[dados_treeview['PACIENTE'] == entry[1]])

        # Filtro Aniversario
        if entry[2] == "":
            pass
        else:
            dados_treeview = pd.DataFrame(dados_treeview.loc[dados_treeview['NASCIMENTO'] == entry[2]])

        return dados_treeview

    # Opções de edição
    def editar_cadastro(self, a):

        try:
            self.exclui_editar()
        except:
            pass

        size = Responsive_container(self.body)

        self.option_cad = CTkFrame(self.Yscroll, width=size.container_w(100), height=size.container_h(10), corner_radius=0, fg_color='transparent')
        self.option_cad.pack(padx=size.container_w(2), pady=size.container_h(1), side=RIGHT)

        size = Responsive_container(self.option_cad)

        self.ver_btn = CTkButton(self.option_cad, text='Visualizar ficha', width=size.container_w(5), height=size.container_h(30), command=self.editar)
        self.excluir_btn = CTkButton(self.option_cad, text='Excluir ficha', width=size.container_w(5), height=size.container_h(30), command=None)


        self.ver_btn.pack(side=LEFT)
        self.excluir_btn.pack(side=LEFT, padx=size.container_w(1))

    # Rxcluir opções
    def exclui_editar(self):

        self.option_cad.destroy()

    # Fechar App
    def fechar_app(self):

        self.windows.quit()

    # Voltar pagina
    def voltar(self):

        from cadastro_pag1 import Cadastro_paciente
        Cadastro_paciente(self.windows)

    # Editar relatorio
    def editar(self):

        i = self.lista_treeview.selection()[0]
        infor = self.lista_treeview.item(i, 'values')

        import cadastro_pag3
        cadastro_pag3.Visualiza_Cadastro(self.windows, infor)
