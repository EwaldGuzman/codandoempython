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

class Visualiza_Cadastro:

    # Inicializador de propriedades
    def __init__(self, win, dados):

        self.cadastro = pathlib.Path('Tabelas_xlsx/Cadastros_xlsx/Consultas - Proficional #00.xlsx').absolute()

        self.data = datetime.now().strftime('%d/%m/%Y')
        self.font_lb = 20
        self.font_entry = 16
        self.tipo_font = 'times new roman'

        self.windows = win
        self.dados = dados
        self.limpar_windows()

        self.contains_principal()
        self.contatos()
        self.scroll()
        self.list_menu()
        self.contains()
        self.campos()
        self.carregar_infor()

    # Limpar janela aberta
    def limpar_windows(self):

        for obj in self.windows.winfo_children():
            obj.destroy()

    # Containes principais
    def contains_principal(self):

        size = Responsive_windows(self.windows)

        self.header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(3), fg_color='#000000', corner_radius=0)
        self.imagem_fr = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(10), fg_color='#FFFFFF')

        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(90), fg_color=None, corner_radius=0)

        self.header.pack(fill=BOTH)
        self.imagem_fr.pack()

        self.body.pack(fill=BOTH)

        size = Responsive_container(self.imagem_fr)

        self.img_fundo = CTkImage(light_image=Image.open('Imagens/view_fundo.png'), dark_image=Image.open(
            'Imagens/view_fundo.png'), size=(size.container_w(100), size.container_h(100)))

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
        size = Responsive_windows(self.windows)

        self.sub_header = CTkFrame(self.Yscroll, width=size.windows_w(100), height=size.windows_h(5), fg_color='#FFFFFF', corner_radius=0)
        self.sub_header.pack(fill=BOTH)

        size = Responsive_container(self.sub_header)

        self.list = CTkFrame(self.sub_header, fg_color='transparent')
        self.list.pack(side=RIGHT, padx=size.container_w(5), pady=size.container_h(4))

        self.enviar_btn = CTkButton(self.list, text='ENVIAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.enviar_email, fg_color='transparent', hover_color='#F7F7F7')
        self.imprimir_btn = CTkButton(self.list, text='IMPRIMIR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=None, fg_color='transparent', hover_color='#F7F7F7')
        self.voltar_btn = CTkButton(self.list, text='VOLTAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.voltar, fg_color='transparent', hover_color='#F7F7F7')
        self.sair_btn = CTkButton(self.list, text='SAIR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.fechar_app, fg_color='transparent', hover_color='#F7F7F7')

        self.enviar_btn.pack(side=LEFT, padx=None, pady=size.container_h(2))
        self.imprimir_btn.pack(side=LEFT, padx=None, pady=size.container_h(2))
        self.voltar_btn.pack(side=LEFT, padx=None, pady=size.container_h(2))
        self.sair_btn.pack(side=LEFT, padx=None, pady=size.container_h(2))

    # Fechar App
    def fechar_app(self):

        self.windows.quit()

    # Iniciar Scroll
    def scroll(self):

        size = Responsive_container(self.body)

        self.Yscroll = CTkScrollableFrame(self.body, width=size.container_w(100), height=size.container_h(100), fg_color='#ffffff')

        self.Yscroll.pack()

    # Corpo da ficha
    def contains(self):

        size = Responsive_container(self.body)

        self.cont_doc = CTkFrame(self.Yscroll, width=size.container_w(70), height=size.container_h(90), fg_color='#ffffff', border_width=1)

        self.cont_doc.pack(pady=(size.container_h(2), size.container_h(4)))

        size = Responsive_container(self.cont_doc)

        self.folha = CTkFrame(self.cont_doc, width=size.container_w(100), height=size.container_h(100), fg_color='#ffffff')

        self.folha.pack(padx=size.container_w(2), pady=size.container_h(2))

        # self.local = CTkFrame(self.cont_doc, width=size.container_w(90), height=size.container_h(10), fg_color='#ffffff')
        #
        # self.local.pack(padx=size.container_w(20), pady=(size.container_h(1), size.container_h(3)), side=RIGHT)

    # Campos de cadastro
    def campos(self):

        size = Responsive_container(self.body)

        linha = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.data_lb = CTkLabel(linha, text='Data da Consulta', font=('', size.container_w(1)), text_color='grey')
        self.data_entry = CTkEntry(linha, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(15), height=size.container_h(5))
        self.sus_lb = CTkLabel(linha, text='Cartão SUS', font=('', size.container_w(1)), text_color='grey')
        self.sus_entry = CTkEntry(linha, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(20), height=size.container_h(5))
        self.nascimento_lb = CTkLabel(linha, text='Data de Nascimento', font=('', size.container_w(1)), text_color='grey')
        self.nascimento_entry = CTkEntry(linha, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(15), height=size.container_h(5))

        linha2 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.paciente_lb = CTkLabel(linha2, text='Paciente', font=('', size.container_w(1)), text_color='grey')
        self.paciente_entry = CTkEntry(linha2, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(30), height=size.container_h(5))
        self.idade_lb = CTkLabel(linha2, text='Idade', font=('', size.container_w(1)), text_color='grey')
        self.idade_entry = CTkEntry(linha2, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(10), height=size.container_h(5))
        self.cor_lb = CTkLabel(linha2, text='Cor/Raça/Etnia', font=('', size.container_w(1)), text_color='grey')
        self.cor_entry = CTkEntry(linha2, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(15), height=size.container_h(5))

        linha3 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.telefone_lb = CTkLabel(linha3, text='Contato', font=('', size.container_w(1)), text_color='grey')
        self.telefone_entry = CTkEntry(linha3, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(15), height=size.container_h(5))
        self.rua_lb = CTkLabel(linha3, text='Lagradouro', font=('', size.container_w(1)), text_color='grey')
        self.rua_entry = CTkEntry(linha3, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(30), height=size.container_h(5))
        self.numero_lb = CTkLabel(linha3, text='Número', font=('', size.container_w(1)), text_color='grey')
        self.numero_entry = CTkEntry(linha3, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(10), height=size.container_h(5))

        linha4 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.bairro_lb = CTkLabel(linha4, text='Bairro', font=('', size.container_w(1)), text_color='grey')
        self.bairro_entry = CTkEntry(linha4, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(20), height=size.container_h(5))
        self.cidade_lb = CTkLabel(linha4, text='Cidade', font=('', size.container_w(1)), text_color='grey')
        self.cidade_entry = CTkEntry(linha4, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(20), height=size.container_h(5))
        self.cep_lb = CTkLabel(linha4, text='CEP', font=('', size.container_w(1)), text_color='grey')
        self.cep_entry = CTkEntry(linha4, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(15), height=size.container_h(5))

        linha5 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.procedimento_lb = CTkLabel(linha5, text='Procedimento Solicitado', font=('', size.container_w(1)), text_color='grey')
        self.procedimento_entry = CTkEntry(linha5, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(57), height=size.container_h(5))

        linha6 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.escolaridade_lb = CTkLabel(linha6, text='Escolaridade', font=('', size.container_w(1)), text_color='grey')
        self.escolaridade_entry = CTkEntry(linha6, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(20), height=size.container_h(5))
        self.turno_lb = CTkLabel(linha6, text='Turno', font=('', size.container_w(1)), text_color='grey')
        self.turno_entry = CTkEntry(linha6, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(10), height=size.container_h(5))
        self.escola_lb = CTkLabel(linha6, text='Escola', font=('', size.container_w(1)), text_color='grey')
        self.escola_entry = CTkEntry(linha6, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(25), height=size.container_h(5))

        linha7 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.deficiencia_lb = CTkLabel(linha7, text='Deficiência', font=('', size.container_w(1)), text_color='grey')
        self.deficiencia_entry = CTkEntry(linha7, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(57), height=size.container_h(5))

        linha8 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.cognitiva_lb = CTkLabel(linha8, text='Limitações/Cognitiva', font=('', size.container_w(1)), text_color='grey')
        self.cognitiva_entry = CTkEntry(linha8, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(13.5), height=size.container_h(5))
        self.locomocao_lb = CTkLabel(linha8, text='Limitações/Locomoção', font=('', size.container_w(1)), text_color='grey')
        self.locomocao_entry = CTkEntry(linha8, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(13.5), height=size.container_h(5))
        self.visao_lb = CTkLabel(linha8, text='Limitações/Visão', font=('', size.container_w(1)), text_color='grey')
        self.visao_entry = CTkEntry(linha8, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(13.5), height=size.container_h(5))
        self.audicao_lb = CTkLabel(linha8, text='Limitação/Audição', font=('', size.container_w(1)), text_color='grey')
        self.audicao_entry = CTkEntry(linha8, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(13.5), height=size.container_h(5))

        linha9 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.outras_lb = CTkLabel(linha9, text='Outras', font=('', size.container_w(1)), text_color='grey')
        self.outras_entry = CTkEntry(linha9, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(57), height=size.container_h(5))

        linha10 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.historico_lb = CTkLabel(linha10, text='Realizou Tratamento?', font=('', size.container_w(1)), text_color='grey')
        self.historico_entry = CTkEntry(linha10, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(17), height=size.container_h(5))
        self.qual_lb = CTkLabel(linha10, text='Qual?', font=('', size.container_w(1)), text_color='grey')
        self.qual_entry = CTkEntry(linha10, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(25), height=size.container_h(5))
        self.quando_lb = CTkLabel(linha10, text='Quando?', font=('', size.container_w(1)), text_color='grey')
        self.quando_entry = CTkEntry(linha10, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(10), height=size.container_h(5))

        linha11 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.resultado_lb = CTkLabel(linha11, text='Quais os Resultados?', font=('', size.container_w(1)), text_color='grey')
        self.resultado_entry = CTkEntry(linha11, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(57), height=size.container_h(5))

        linha12 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.tratamento_lb = CTkLabel(linha12, text='Parecer sobre Tratamento', font=('', size.container_w(1)), text_color='grey')
        self.tratamento_entry = CTkEntry(linha12, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(57), height=size.container_h(5))

        linha13 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.queixa_lb = CTkLabel(linha13, text='Queixa Principal', font=('', size.container_w(1)), text_color='grey')
        self.queixa_entry = CTkTextbox(linha13, font=('', size.container_w(1)), fg_color='white', border_width=1, width=size.container_w(57), height=size.container_h(20))

        linha14 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.inicio_lb = CTkLabel(linha14, text='Inicio da Queixa', font=('', size.container_w(1)), text_color='grey')
        self.inicio_entry = CTkEntry(linha14, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(15), height=size.container_h(5))
        self.medicamento_lb = CTkLabel(linha14, text='Press.Med.Uso Continuo', font=('', size.container_w(1)), text_color='grey')
        self.medicamento_entry = CTkEntry(linha14, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(25), height=size.container_h(5))

        linha15 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.tipo_lb = CTkLabel(linha15, text='Tipo de Medicamento', font=('', size.container_w(1)), text_color='grey')
        self.tipo_entry = CTkEntry(linha15, font=('', size.container_w(1)), fg_color='white', justify=CENTER, border_width=1, corner_radius=100, width=size.container_w(57), height=size.container_h(5))

        linha16 = CTkFrame(self.folha, width=size.container_w(100), fg_color='#ffffff')
        self.sair = CTkButton(linha16, text='Sair/Não Salvar', command=self.voltar)
        self.salvar = CTkButton(linha16, text='Sair/Salvar', command=self.salvar_sair)

        linha.pack(padx=size.container_w(10), anchor=W)
        self.data_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.data_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.sus_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.sus_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.nascimento_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.nascimento_entry.grid(column=2, row=1, sticky=W)

        linha2.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.paciente_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.paciente_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.idade_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.idade_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.cor_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.cor_entry.grid(column=2, row=1, sticky=W)

        linha3.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.telefone_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.telefone_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.rua_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.rua_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.numero_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.numero_entry.grid(column=2, row=1, sticky=W)

        linha4.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.bairro_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.bairro_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.cidade_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.cidade_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.cep_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.cep_entry.grid(column=2, row=1, sticky=W)

        linha5.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.procedimento_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.procedimento_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha6.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.escolaridade_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.escolaridade_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.turno_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.turno_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.escola_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.escola_entry.grid(column=2, row=1, sticky=W)

        linha7.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.deficiencia_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.deficiencia_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha8.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.cognitiva_lb.grid(column=0, row=1, sticky=W, padx=(size.container_w(1), 0))
        self.cognitiva_entry.grid(column=0, row=2, sticky=W, padx=(0, size.container_w(1)))
        self.locomocao_lb.grid(column=1, row=1, sticky=W, padx=(size.container_w(1), 0))
        self.locomocao_entry.grid(column=1, row=2, sticky=W, padx=(0, size.container_w(1)))
        self.visao_lb.grid(column=2, row=1, sticky=W, padx=(size.container_w(1), 0))
        self.visao_entry.grid(column=2, row=2, sticky=W, padx=(0, size.container_w(1)))
        self.audicao_lb.grid(column=3, row=1, sticky=W, padx=(size.container_w(1), 0))
        self.audicao_entry.grid(column=3, row=2, sticky=W, padx=(0, size.container_w(1)))

        linha9.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.outras_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.outras_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha10.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.historico_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.historico_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.qual_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.qual_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.quando_lb.grid(column=2, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.quando_entry.grid(column=2, row=1, sticky=W)

        linha11.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.resultado_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.resultado_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha12.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.tratamento_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.tratamento_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha13.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.queixa_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.queixa_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha14.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), anchor=W)
        self.inicio_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.inicio_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))
        self.medicamento_lb.grid(column=1, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.medicamento_entry.grid(column=1, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha15.pack(padx=size.container_w(10), pady=size.container_h(2), anchor=W)
        self.tipo_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.tipo_entry.grid(column=0, row=1, sticky=W, padx=(0, size.container_w(1)))

        linha16.pack(padx=size.container_w(10), anchor=E)
        self.sair.grid(column=0, row=0, sticky=W)
        self.salvar.grid(column=1, row=0, sticky=W, padx=(size.container_w(0.5), size.container_w(1.5)))

    # Carregar informações
    def carregar_infor(self):

        dados = self.dados

        self.data_entry.insert(0, dados[0])
        self.sus_entry.insert(0, dados[1])
        self.paciente_entry.insert(0, dados[2])
        self.nascimento_entry.insert(0, dados[3])
        self.idade_entry.insert(0, dados[4])
        self.telefone_entry.insert(0, dados[5])
        self.rua_entry.insert(0, dados[6])
        self.numero_entry.insert(0, dados[7])
        self.bairro_entry.insert(0, dados[8])
        self.cidade_entry.insert(0, dados[9])
        self.cep_entry.insert(0, dados[10])
        self.procedimento_entry.insert(0, dados[11])
        self.escolaridade_entry.insert(0, dados[12])
        self.turno_entry.insert(0, dados[13])
        self.escola_entry.insert(0, dados[14])
        self.deficiencia_entry.insert(0, dados[15])
        self.cor_entry.insert(0, dados[16])
        self.cognitiva_entry.insert(0, dados[17])
        self.locomocao_entry.insert(0, dados[18])
        self.visao_entry.insert(0, dados[19])
        self.audicao_entry.insert(0, dados[20])
        self.outras_entry.insert(0, dados[21])
        self.historico_entry.insert(0, dados[22])
        self.qual_entry.insert(0, dados[23])
        self.quando_entry.insert(0, dados[24])
        self.resultado_entry.insert(0, dados[25])
        self.tratamento_entry.insert(0, dados[26])
        self.queixa_entry.insert(0.0, dados[27])
        self.inicio_entry.insert(0, dados[28])
        self.medicamento_entry.insert(0, dados[29])
        self.tipo_entry.insert(0, dados[30])

    # Filtar registro
    def filtro3x(self, dados, campos):

        entry = campos

        dados_treeview = pd.DataFrame(dados)

        # Filtro Datas
        if entry[0] == "":
            pass
        else:
            dados_treeview = pd.DataFrame(dados_treeview.loc[dados_treeview['DATA CONSULTA'] == entry[0]])

        # Filtro SUS
        if entry[1] == "":
            pass
        else:
            dados_treeview = pd.DataFrame(dados_treeview.loc[dados_treeview['SUS'] == entry[1]])

        # Filtro Paciente
        if entry[2] == "":
            pass
        else:
            dados_treeview = pd.DataFrame(dados_treeview.loc[dados_treeview['PACIENTE'] == entry[2]])

        return dados_treeview

    # Coletando informações de campos
    def coletar_dados(self):

        infor = [
            str(self.data_entry.get()),
            int(self.sus_entry.get()),
            self.paciente_entry.get().strip().upper(),
            self.nascimento_entry.get(),
            int(self.idade_entry.get()),
            int(self.telefone_entry.get()),
            self.rua_entry.get().strip().upper(),
            int(self.numero_entry.get()),
            self.bairro_entry.get().strip().upper(),
            self.cidade_entry.get().strip().upper(),
            int(self.cep_entry.get()),
            self.procedimento_entry.get().strip().upper(),
            self.escolaridade_entry.get().strip().upper(),
            self.turno_entry.get().strip().upper(),
            self.escola_entry.get().strip().upper(),
            self.deficiencia_entry.get().strip().upper(),
            self.cor_entry.get().strip().upper(),
            self.cognitiva_entry.get().strip().upper(),
            self.locomocao_entry.get().strip().upper(),
            self.visao_entry.get().strip().upper(),
            self.audicao_entry.get().strip().upper(),
            self.outras_entry.get().strip().upper(),
            self.historico_entry.get().strip().upper(),
            self.qual_entry.get().strip().upper(),
            self.quando_entry.get(),
            self.resultado_entry.get().strip().upper(),
            self.tratamento_entry.get().strip().upper(),
            self.queixa_entry.get(0.0, 'end').strip().upper(),
            self.inicio_entry.get(),
            self.medicamento_entry.get().strip().upper(),
            self.tipo_entry.get().strip().upper(),

        ]
        return infor

    # Calcular idade exata da pessoa
    def calcular_idade(self):

        try:
            data_nasc = self.nascimento_entry.get().replace('/', '')
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

    # Funções

    # Sair e Salvar
    def salvar_sair(self):

        dados = list(self.coletar_dados())

        campos = [self.data_entry.get(), int(self.sus_entry.get()), self.paciente_entry.get().upper()]

        tabela = pd.read_excel(self.cadastro)
        linha = self.filtro3x(tabela, campos).index
        ficha = list(tabela.columns)

        for k, i in enumerate(ficha):
            tabela.loc[linha, i] = dados[k]

        tabela.to_excel(self.cadastro, index=False)

        messagebox.showinfo('', 'concluido')

        self.voltar()

    # Voltar
    def voltar(self):

        import cadastro_pag2
        cadastro_pag2.Pesquisar_Cadastro(self.windows)

    # Pagina email
    def enviar_email(self):

        import pagina_email
        pagina_email.Enviar_email(self.windows)





