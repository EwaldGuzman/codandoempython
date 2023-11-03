
# Bibliotecas Python
from customtkinter import *
from openpyxl import load_workbook
from tkinter import messagebox
from datetime import datetime
from PIL import Image

import pathlib
import pandas as pd


# Bibliotecas Minhas
from geometria_sistema import Responsive_windows, Responsive_container
import salvar_google_sheets
import acessos
import criar_planilha_consulta

class Cadastro_Consulta:

    # Inicializador de propriedades
    def __init__(self, win, usuario):

        self.user = usuario
        num = self.user.find('#')
        self.cadastro = pathlib.Path(fr'Tabelas_xlsx/Cadastros_xlsx/Consultas - Proficional {self.user[num:]}.xlsx').absolute()

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
        self.imagen_perfil()
        self.campos()

    # Limpar janela aberta
    def limpar_windows(self):

        for obj in self.windows.winfo_children():
            obj.destroy()

    # Containes principais
    def contains_principal(self):

        size = Responsive_windows(self.windows)

        self.header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(3), fg_color='#000000', corner_radius=0)
        self.sub_header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(10), fg_color='#FFFFFF', corner_radius=0, border_width=1)
        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(90), fg_color=None, corner_radius=0)

        self.header.pack(fill=BOTH)
        self.sub_header.pack(fill=BOTH)
        self.body.pack(fill=BOTH)

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
        self.list.pack(side=RIGHT, padx=size.container_w(10), pady=size.container_h(1))

        self.logo = CTkFrame(self.sub_header, fg_color='transparent')
        self.logo.pack(side=LEFT, padx=size.container_w(10))

        self.logo_lb = CTkLabel(self.logo, text='APAE - Zé Doca-MA', text_color='black', font=('Mistral', size.container_w(4)))
        self.logo_lb.pack(pady=size.container_h(5))

        self.relatorio_btn = CTkButton(self.list, text='RELATÓRIOS', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.relatorio, fg_color='transparent', hover_color='#F7F7F7')
        # self.filtar_btn = CTkButton(self.list, text='FILTRAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=None, fg_color='transparent', hover_color='#F7F7F7')
        # self.enviar_btn = CTkButton(self.list, text='ENVIAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=None, fg_color='transparent', hover_color='#F7F7F7')
        # self.imprimir_btn = CTkButton(self.list, text='IMPRIMIR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=None, fg_color='transparent', hover_color='#F7F7F7')
        self.voltar_btn = CTkButton(self.list, text='VOLTAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.inicio, fg_color='transparent', hover_color='#F7F7F7')
        self.sair_btn = CTkButton(self.list, text='SAIR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.fechar_app, fg_color='transparent', hover_color='#F7F7F7')


        self.relatorio_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        # self.filtar_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        # self.enviar_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        # self.imprimir_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        self.voltar_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        self.sair_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))

    # Fechar App
    def fechar_app(self):

        self.windows.quit()

    # Barra de rolagem
    def scroll(self):

        size = Responsive_container(self.body)

        self.Yscroll = CTkScrollableFrame(self.body, width=size.container_w(77), height=size.container_h(100), fg_color='#FFFFFF', corner_radius=1, border_color='black')
        self.Yscroll.pack(side=RIGHT)

    # Containes Secundarios
    def contains(self):

        size = Responsive_container(self.body)

        self.perfil = CTkFrame(self.body, width=size.container_w(26), height=size.container_h(100), fg_color='white', corner_radius=0, border_width=2)
        # self.imagen_fr = CTkFrame(self.Yscroll, width=size.container_w(100), height=size.container_h(20.5), fg_color='white', corner_radius=0, border_width=0)
        self.dados = CTkFrame(self.Yscroll, width=size.container_w(45), height=size.container_h(100), fg_color='#ffffff', corner_radius=5, border_width=1)

        self.perfil.pack(side=LEFT, anchor=N)
        # self.imagen_fr.pack()
        self.dados.pack(pady=size.container_h(3))

    # Todos os campos de cadastro
    def campos(self):

        size = Responsive_container(self.dados)

        self.titulo = CTkLabel(self.dados, text='CADASTRO DE CONSULTAS', font=('', 30))
        self.titulo.pack(pady=(size.container_h(3), 0))

        # Frame
        self.linha1 = CTkFrame(self.dados, fg_color='transparent', width=size.container_w(70))
        self.linha2 = CTkFrame(self.dados, fg_color='transparent', width=size.container_w(70))
        self.linha3 = CTkFrame(self.dados, fg_color='transparent', width=size.container_w(70))
        self.linha4 = CTkFrame(self.dados, fg_color='transparent', width=size.container_w(70))
        self.linha5 = CTkFrame(self.dados, fg_color='transparent')

        # Label
        # self.numero_fixa_lb = CTkLabel(self.dados, text='Fixa:', font=(self.tipo_font, self.font_lb), width=size.container_w(68), anchor=W)
        self.data_consulta_lb = CTkLabel(self.linha1, text='Data da Consulta:', font=(self.tipo_font, self.font_entry), width=size.container_w(20), anchor=W)
        self.sus_lb = CTkLabel(self.linha1, text='SUS:', font=(self.tipo_font, self.font_entry), width=size.container_w(39), anchor=W)
        self.paciente_lb = CTkLabel(self.dados, text='Paciente', font=(self.tipo_font, self.font_entry), width=size.container_w(68), anchor=W)
        self.data_lb = CTkLabel(self.linha2, text='Data de Nasc.:', font=(self.tipo_font, self.font_entry), width=size.container_w(19), anchor=W)
        self.idade_lb = CTkLabel(self.linha2, text='Idade', font=(self.tipo_font, self.font_entry), width=size.container_w(15), anchor=W)
        self.fone_lb = CTkLabel(self.dados, text='Telefone', font=(self.tipo_font, self.font_entry), width=size.container_w(68), anchor=W)
        self.Lagradouro_lb = CTkLabel(self.dados, text='Lagradouro:', font=(self.tipo_font, self.font_entry), width=size.container_w(68), anchor=W)
        self.numero_lb = CTkLabel(self.linha3, text='Numero:', font=(self.tipo_font, self.font_entry), width=size.container_w(10), anchor=W)
        self.bairro_lb = CTkLabel(self.linha3, text='Bairro:', font=(self.tipo_font, self.font_entry), width=size.container_w(39), anchor=W)
        self.cidade_lb = CTkLabel(self.linha4, text='Cidade:', font=(self.tipo_font, self.font_entry), width=size.container_w(39), anchor=W)
        self.cep_lb = CTkLabel(self.linha4, text='CEP:', font=(self.tipo_font, self.font_entry), width=size.container_w(17), anchor=W)
        self.descricao_lb = CTkLabel(self.dados, text='Descrição:', font=(self.tipo_font, self.font_entry), width=size.container_w(68), anchor=W)

        # Entry
        # self.numero_fixa_entry = CTkEntry(self.dados, font=(self.tipo_font, self.font_lb), width=size.container_w(15), height=size.container_h(4), border_width=1)
        self.data_fr = CTkFrame(self.linha1, border_width=1, fg_color='white', height=size.container_h(4))
        self.data_consulta_entry = CTkLabel(self.data_fr, text=f'{self.data}', font=(self.tipo_font, self.font_lb), width=size.container_w(20), corner_radius=5, fg_color='white', justify=CENTER)
        self.sus_entry = CTkEntry(self.linha1, font=(self.tipo_font, self.font_lb), width=size.container_w(40), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.paciente_entry = CTkEntry(self.dados, font=(self.tipo_font, self.font_lb), width=size.container_w(70), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.data_entry = CTkEntry(self.linha2, font=(self.tipo_font, self.font_lb), width=size.container_w(25), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.data_fr2 = CTkFrame(self.linha2, border_width=1, fg_color='white', height=size.container_h(4))
        self.idade_entry = CTkLabel(self.data_fr2, text='', font=(self.tipo_font, self.font_lb), width=size.container_w(15), fg_color='white', justify=CENTER)
        self.fone_entry = CTkEntry(self.dados, font=(self.tipo_font, self.font_lb), width=size.container_w(36), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.lagradouro_entry = CTkEntry(self.dados, font=(self.tipo_font, self.font_lb), width=size.container_w(70), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.numero_entry = CTkEntry(self.linha3, font=(self.tipo_font, self.font_lb), width=size.container_w(10), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.bairro_entry = CTkEntry(self.linha3, font=(self.tipo_font, self.font_lb), width=size.container_w(40), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.cidade_entry = CTkEntry(self.linha4, font=(self.tipo_font, self.font_lb), width=size.container_w(40), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)
        self.cep_entry = CTkEntry(self.linha4, font=(self.tipo_font, self.font_lb), width=size.container_w(18), height=size.container_h(4), border_width=1, fg_color='white', justify=CENTER)

        self.data_entry.bind('<FocusOut>', self.idade)

        # Textbox
        self.descricao_txt = CTkTextbox(self.dados, font=(self.tipo_font, self.font_lb), width=size.container_w(70), height=size.container_h(20), border_width=1, fg_color='white')

        # Botões
        self.salvar_btn = CTkButton(self.linha5, text='Guardar', width=size.container_w(12), height=size.container_h(3), command=self.cadastrar)
        self.cancelar_btn = CTkButton(self.linha5, text='Cancelar', width=size.container_w(12), height=size.container_h(3), command=None)

        # Pos

        # self.numero_fixa_lb.pack(padx=size.container_w(15))
        # self.numero_fixa_entry.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W)

        self.linha1.pack(padx=size.container_w(15), pady=size.container_h(3), anchor=W, fill=X)

        self.data_consulta_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.data_fr.grid(column=0, row=1, sticky=NSEW)
        self.data_consulta_entry.pack(padx=size.container_w(1), pady=(size.container_h(0.5), 0))
        self.sus_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(3), 0))
        self.sus_entry.grid(column=1, row=1, sticky=E, padx=(size.container_w(1), 0))

        self.paciente_lb.pack(padx=size.container_w(15))
        self.paciente_entry.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W)

        self.linha2.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W, fill=X)
        self.data_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.data_entry.grid(column=0, row=1, sticky=W)
        self.idade_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(3), 0))
        self.data_fr2.grid(column=1, row=1, sticky=NSEW, padx=(size.container_w(2), 0))
        self.idade_entry.pack(padx=size.container_w(1), pady=(size.container_h(0.5), 0))

        self.fone_lb.pack(padx=size.container_w(15))
        self.fone_entry.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W)
        self.Lagradouro_lb.pack(padx=size.container_w(15))
        self.lagradouro_entry.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W)

        self.linha3.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W, fill=X)
        self.numero_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.numero_entry.grid(column=0, row=1, sticky=W)
        self.bairro_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(1), 0))
        self.bairro_entry.grid(column=1, row=1, sticky=E, padx=(size.container_w(1), 0))

        self.linha4.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), anchor=W, fill=X)
        self.cidade_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.cidade_entry.grid(column=0, row=1, sticky=W)
        self.cep_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(1), 0))
        self.cep_entry.grid(column=1, row=1, sticky=E, padx=(size.container_w(1), 0))

        self.descricao_lb.pack(padx=size.container_w(15))
        self.descricao_txt.pack(pady=(0, size.container_h(3)))

        self.linha5.pack(padx=size.container_w(15), pady=(0, size.container_h(3)), side=RIGHT)
        self.salvar_btn.pack(side=LEFT, anchor=E, padx=size.container_w(1))
        self.cancelar_btn.pack(side=LEFT, anchor=E)

    # Imagen de fundo no perfil lateral
    def imagen_perfil(self):

        size = Responsive_container(self.perfil)

        self.img_logo = CTkImage(light_image=Image.open('Imagens/logo-lado.png'), dark_image=Image.open('Imagens/logo-lado.png'), size=(size.container_w(85), size.container_h(100)))

        self.img_lb = CTkLabel(self.perfil, text='', image=self.img_logo)
        self.img_lb.pack()

    # Chamar Janela Inicio
    def inicio(self):
        from tela_boas_vindas import Tela_Inicial
        Tela_Inicial(self.windows)

    # Coletar dados de cadastro
    def dados_cadastro(self):

        dados = [
            self.data,
            self.sus_entry.get(),
            self.paciente_entry.get().strip().upper(),
            self.data_entry.get(),
            self.calcular_idade(),
            self.fone_entry.get(),
            self.lagradouro_entry.get().strip().upper(),
            self.numero_entry.get(),
            self.bairro_entry.get().strip().upper(),
            self.cidade_entry.get().strip().upper(),
            self.cep_entry.get(),
            self.descricao_txt.get('0.0', END).strip().upper()
        ]

        return dados

    # Verificar campo vazio
    def validacao(self):

        dados = self.dados_cadastro()
        dados.pop(0)
        self.vazio = 0
        for i in dados:
            if i == "":
                self.vazio += 1

        if self.vazio == 0:
            return False
        else:
            return True

    # Calcular idade exata da pessoa
    def calcular_idade(self):

        try:
            data_nasc = self.data_entry.get().replace('/', '')
            dia_nasc = int(data_nasc[:2])
            mes_nasc = int(data_nasc[2:4])
            ano_nasc = int(data_nasc[4:])

            data_atual = self.data.replace('/', '')
            dia_atual = int(data_atual[:2])
            mes_atual = int(data_atual[2:4])
            ano_atual = int(data_atual[4:])


            if mes_atual < mes_nasc:
                idade = (ano_atual-ano_nasc) - 1
            elif dia_atual < dia_nasc and mes_atual == mes_nasc:
                idade = (ano_atual-ano_nasc) - 1
            else:
                idade = (ano_atual-ano_nasc)

            return idade
        except:
            pass

    # Adicionar idade no Campo Idade
    def idade(self, a):
        self.idade_entry.configure(text=self.calcular_idade())

    # Cadastrar dados coletado
    def cadastrar(self):

        # try:
        #
        c = self.validacao()

        if c == True:

            messagebox.showinfo('Atenção!', 'Preencha todos os campos do formulário')
        else:



            messagebox.showinfo('Atenção!', 'Aguarde, estamos salvando seu relatório')
            dados = self.dados_cadastro()
            tabela = load_workbook(self.cadastro)
            ficha = tabela.active
            ficha.append(dados)
            tabela.save(self.cadastro)

            self.limpar_registro()

            linha = self.cont_linhas()
            user = acessos.user[self.user]
            comando = salvar_google_sheets
            comando.Salvar(user['ID'], f'Página1!A{linha+1}', [dados]).gravar()
            messagebox.showinfo('Atenção!', 'Dados salvos com sucesso')
        #
        # except:
        #
        #     messagebox.showinfo('Atenção!', '"ERRO" ao cadastrar')

    # Quantidade de linha cadastradas
    def cont_linhas(self):

        tabela = pd.read_excel(self.cadastro)

        linha = tabela['PACIENTE'].count()

        return linha

    # Limpar todos os campos de cadastro
    def limpar_registro(self):

        self.sus_entry.delete(0, END)
        self.paciente_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.idade_entry.configure(text='')
        self.fone_entry.delete(0, END)
        self.lagradouro_entry.delete(0, END)
        self.numero_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.descricao_txt.delete(0.0, END)
        self.sus_entry.focus_set()

    # Filtar registro
    def filtro3x(self, DADOS):

        entry = [self.sus_entry.get(), self.paciente_entry.get(), self.data_entry.get()]

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

    def relatorio(self):

        import consulta_secundario
        consulta_secundario.Pesquisar_Consulta(self.windows, self.user)
