
# Bilbiotecas Pyrhon
from customtkinter import *
from tkinter import messagebox
from datetime import datetime
from PIL import Image
from openpyxl import load_workbook
import pandas as pd
from pathlib import Path

# Bibliotecas Minhas
from geometria_sistema import Responsive_windows, Responsive_container
import salvar_google_sheets
import acessos

# Classe Principal
class Cadastro_paciente:

    def __init__(self, win):

        self.cadastro = Path('Tabelas_xlsx/Cadastros_xlsx/Consultas - Proficional #00.xlsx').absolute()
        self.data = datetime.now().strftime('%d/%m/%Y')

        self.font_lb = 'arial'
        self.size_font_lb = 16
        self.size_font_entry = 18
        self.stile_font_lb = 'bold'

        self.windows = win
        self.limpar_windows()

        self.cor_entry = '#FFFFFF'

        self.contains_principal()
        self.contatos()
        self.list_menu()
        self.iniciar_scroll()
        self.contains_scroll()
        self.cadastro_paciente()
        self.contar_cadastro()

    def limpar_windows(self):

        for obj in self.windows.winfo_children():
            obj.destroy()

    def contains_principal(self):

        size = Responsive_windows(self.windows)

        self.header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(3), fg_color='#000000', corner_radius=0)
        self.sub_header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(10), fg_color='#FFFFFF', corner_radius=0, border_width=1)
        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(90), fg_color=None, corner_radius=0)

        self.header.pack(fill=BOTH)
        self.sub_header.pack(fill=BOTH)
        self.body.pack(fill=BOTH)

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

    def list_menu(self):

        size = Responsive_container(self.sub_header)

        self.list = CTkFrame(self.sub_header, fg_color='transparent')
        self.list.pack(side=RIGHT, padx=size.container_w(10), pady=size.container_h(1))

        self.logo = CTkFrame(self.sub_header, fg_color='transparent')
        self.logo.pack(side=LEFT, padx=size.container_w(10))

        self.logo_lb = CTkLabel(self.logo, text='APAE - Zé Doca-MA', text_color='black', font=('Mistral', size.container_w(4)))
        self.logo_lb.pack(pady=size.container_h(5))

        self.relatorio_btn = CTkButton(self.list, text='RELATÓRIOS', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.formulario, fg_color='transparent', hover_color='#F7F7F7')
        self.voltar_btn = CTkButton(self.list, text='VOLTAR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.inicio, fg_color='transparent', hover_color='#F7F7F7')
        self.sair_btn = CTkButton(self.list, text='SAIR', text_color='black', font=('arial', size.container_w(1)), width=size.container_w(5), height=size.container_h(70), command=self.fechar_app, fg_color='transparent', hover_color='#F7F7F7')


        self.relatorio_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        self.voltar_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))
        self.sair_btn.pack(side=LEFT, padx=None, pady=size.container_h(15))

    def fechar_app(self):

        self.windows.quit()

    def iniciar_scroll(self):

        size = Responsive_container(self.body)

        self.Yscroll = CTkScrollableFrame(self.body, width=size.container_w(100), height=size.container_h(100), fg_color='#FFFFFF', corner_radius=0)

        self.Yscroll.pack()

    def contains_scroll(self):

        size = Responsive_container(self.body)

        self.imagem = CTkFrame(self.Yscroll, width=size.container_w(100), height=size.container_h(35), fg_color='light grey', corner_radius=0)

        self.contains_cadastro = CTkFrame(self.Yscroll, width=size.container_w(50), height=size.container_h(100), fg_color='#F6F4FA')

        self.imagem.pack(fill=BOTH, pady=(0, size.container_h(2)))
        self.contains_cadastro.pack(pady=(0, size.container_h(5)))

        size = Responsive_container(self.imagem)
        self.img_fundo = CTkImage(light_image=Image.open('Imagens/cadastro_paciente.png'), dark_image=Image.open(
            'Imagens/cadastro_paciente.png'), size=(size.container_w(100), size.container_h(100)))

        CTkLabel(self.imagem, text='', image=self.img_fundo, width=size.container_w(100), height=size.container_h(100)).pack()

    def cadastro_paciente(self):

        size = Responsive_container(self.contains_cadastro)

        # Container
        self.turno_fr = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.cor_fr = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.limitacao_fr = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.historico_fr = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.medicamento_fr = CTkFrame(self.contains_cadastro, fg_color='transparent')

        self.linha1 = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.linha2 = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.linha3 = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.linha4 = CTkFrame(self.contains_cadastro, fg_color='transparent')
        self.linha5 = CTkFrame(self.contains_cadastro, fg_color='transparent')

        # Label
        self.titulo_lb = CTkLabel(self.contains_cadastro, text='IDENTIFICAÇÃO DO PACIENTE', font=('times new roman', 34), width=size.container_w(100))

        self.prontuario_n_lb = CTkLabel(self.linha1, text='PRONTUARIO Nº:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(30), anchor=W)
        self.data_lb = CTkLabel(self.linha1, text='DATA DO ATENDIMENTO:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(28), anchor=W)
        self.sus_lb = CTkLabel(self.contains_cadastro, text='SUS:', font=('', self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)

        self.paciente_lb = CTkLabel(self.contains_cadastro, text='NOME DO PACIENTE:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.data_nasc_lb = CTkLabel(self.linha2, text='Data de Nasc.:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(30), anchor=W)
        self.contato_lb = CTkLabel(self.linha2, text='Telefone:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(28), anchor=W)
        self.rua_lb = CTkLabel(self.contains_cadastro, text='Lagradouro:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.numero_lb = CTkLabel(self.linha3, text='Número:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(10), anchor=W)
        self.bairro_lb = CTkLabel(self.linha3, text='Bairro:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(47), anchor=W)
        self.cidade_lb = CTkLabel(self.linha4, text='Cidade:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(38), anchor=W)
        self.cep_lb = CTkLabel(self.linha4, text='CEP:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(19), anchor=W)

        self.procedimento_lb = CTkLabel(self.contains_cadastro, text='PROCEDIMENTO SOLICITADO:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.escolaridade_lb = CTkLabel(self.contains_cadastro, text='ESCOLARIDADE:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.turno_lb = CTkLabel(self.contains_cadastro, text='Turno:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.escola_lb = CTkLabel(self.contains_cadastro, text='Escola que Frequenta:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.deficiencia_lb = CTkLabel(self.contains_cadastro, text='TIPO DE DEFICIENCIA:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.cor_lb = CTkLabel(self.contains_cadastro, text='RAÇA/COR/ETNIA:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.limitacao_lb = CTkLabel(self.contains_cadastro, text='LIMITAÇÕES:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.outras_lb = CTkLabel(self.contains_cadastro, text='Outras:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.historico_lb = CTkLabel(self.contains_cadastro, text='HISTÓRICO: Realizou tratamento?:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.qual_lb = CTkLabel(self.contains_cadastro, text='Qual?:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.quando_lb = CTkLabel(self.contains_cadastro, text='Quando?', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.resultado_lb = CTkLabel(self.contains_cadastro, text='Quais os Resultados:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.tratamento_lb = CTkLabel(self.contains_cadastro, text='Parecer sobre tratamento:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.queixa_lb = CTkLabel(self.contains_cadastro, text='QUEIXA PRINCIPAL:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.data_queixa_lb = CTkLabel(self.contains_cadastro, text='Inicio da Queixa:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.medicamento_lb = CTkLabel(self.contains_cadastro, text='PRESS.MED.USO CONTINUO:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)
        self.tipo_lb = CTkLabel(self.contains_cadastro, text='Que tipo de medicamento:', font=(self.font_lb, self.size_font_lb, self.stile_font_lb), width=size.container_w(82), anchor=W)

        # Entry
        self.prontuario_n_entry = CTkEntry(self.linha1, font=('', self.size_font_entry), width=size.container_w(29), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.data_entry = CTkEntry(self.linha1, font=('', self.size_font_entry), width=size.container_w(29), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.sus_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.paciente_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.data_nasc_entry = CTkEntry(self.linha2, font=('', self.size_font_entry), width=size.container_w(29), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.contato_entry = CTkEntry(self.linha2, font=('', self.size_font_entry), width=size.container_w(29), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.rua_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.numero_entry = CTkEntry(self.linha3, font=('', self.size_font_entry), width=size.container_w(10), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.bairro_entry = CTkEntry(self.linha3, font=('', self.size_font_entry), width=size.container_w(48), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.cidade_entry = CTkEntry(self.linha4, font=('', self.size_font_entry), width=size.container_w(38), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.cep_entry = CTkEntry(self.linha4, font=('', self.size_font_entry), width=size.container_w(20), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.procedimento_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.escolaridade_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(40), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.escola_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.deficiencia_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.outras_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.qual_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(50), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.quando_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(30), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.resultado_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.tratamento_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.data_queixa_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(30), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)
        self.tipo_entry = CTkEntry(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(4), border_width=1, fg_color=self.cor_entry, justify=CENTER)

        # Textbox
        self.queixa_txt = CTkTextbox(self.contains_cadastro, font=('', self.size_font_entry), width=size.container_w(83), height=size.container_h(20), border_width=1, fg_color=self.cor_entry)


        # RadioButton

        size_font = Responsive_windows(self.windows)

        # Variaveis
        self.turno_var = StringVar()
        self.etnia_var = StringVar()
        self.historico_var = StringVar()
        self.medicamento_var = StringVar()
        self.cognitiva_var = StringVar()
        self.locomocao_var = StringVar()
        self.visao_var = StringVar()
        self.audicao_var = StringVar()


        self.matutino = CTkRadioButton(self.turno_fr, variable=self.turno_var, value='matutino', text='Matutino', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.vespertino = CTkRadioButton(self.turno_fr, variable=self.turno_var, value='vespertino', text='Vespertino', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.noturno = CTkRadioButton(self.turno_fr, variable=self.turno_var, value='noturno', text='Noturno', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.branca = CTkRadioButton(self.cor_fr, variable=self.etnia_var, value='branca', text='Branca', font=('', size.container_w(1.9)), width=size.container_w(10), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.negra = CTkRadioButton(self.cor_fr, variable=self.etnia_var, value='negra', text='Negra', font=('', size.container_w(1.9)), width=size.container_w(8), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.amarela = CTkRadioButton(self.cor_fr, variable=self.etnia_var, value='amarela', text='Amarela', font=('', size.container_w(1.9)), width=size.container_w(11), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.parda = CTkRadioButton(self.cor_fr, variable=self.etnia_var, value='parda', text='Parda', font=('', size.container_w(1.9)), width=size.container_w(8), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.indigena = CTkRadioButton(self.cor_fr, variable=self.etnia_var, value='indigena', text='Indigena', font=('', size.container_w(1.9)), width=size.container_w(11), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.desconhecida = CTkRadioButton(self.cor_fr, variable=self.etnia_var, value='desconhecida', text='Desc.', font=('', size.container_w(1.9)), width=size.container_w(11), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.h_sim = CTkRadioButton(self.historico_fr, variable=self.historico_var, value='SIM', text='Sim', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.h_nao = CTkRadioButton(self.historico_fr, variable=self.historico_var, value='NÃO', text='Não', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.m_sim = CTkRadioButton(self.medicamento_fr, variable=self.medicamento_var, value='SIM', text='Sim', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')
        self.m_nao = CTkRadioButton(self.medicamento_fr, variable=self.medicamento_var, value='NÃO', text='Não', font=('', size.container_w(1.9)), border_width_unchecked=1, border_width_checked=9, fg_color='black', hover_color=None, border_color='black')

        # Chekbox
        self.cognitiva = CTkCheckBox(self.limitacao_fr, variable=self.cognitiva_var, onvalue="SIM", offvalue="NÃO", text='Cognitiva', font=('', size.container_w(1.9)), border_width=1)
        self.locomocao = CTkCheckBox(self.limitacao_fr, variable=self.locomocao_var, onvalue="SIM", offvalue="NÃO", text='Locomoção', font=('', size.container_w(1.9)), border_width=1)
        self.visao = CTkCheckBox(self.limitacao_fr, variable=self.visao_var, onvalue="SIM", offvalue="NÃO", text='Visão', font=('', size.container_w(1.9)), border_width=1)
        self.audicao = CTkCheckBox(self.limitacao_fr, variable=self.audicao_var, onvalue="SIM", offvalue="NÃO", text='Audição', font=('', size.container_w(1.9)), border_width=1)

        self.cognitiva.deselect()
        self.locomocao.deselect()
        self.visao.deselect()
        self.audicao.deselect()

        # Button
        self.salvar_btn = CTkButton(self.linha5, text='Salvar', font=('', size_font.font_windows(16)), width=size.container_w(15), height=size.container_h(4), command=self.cadastrar_paciente)
        self.cancelar_btn = CTkButton(self.linha5, text='Cancelar', font=('', size_font.font_windows(16)), width=size.container_w(15), height=size.container_h(4), command=None)


        # Pos
        self.titulo_lb.pack(pady=size.container_h(3))

        self.linha1.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.prontuario_n_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.prontuario_n_entry.grid(column=0, row=1, sticky=W)
        self.data_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(1), 0))
        self.data_entry.grid(column=1, row=1, sticky=E)


        self.sus_lb.pack()
        self.sus_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.paciente_lb.pack()
        self.paciente_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.linha2.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.data_nasc_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.data_nasc_entry.grid(column=0, row=1, sticky=W)
        self.contato_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(1), 0))
        self.contato_entry.grid(column=1, row=1, sticky=E)

        self.rua_lb.pack()
        self.rua_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.linha3.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.numero_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.numero_entry.grid(column=0, row=1, sticky=W)
        self.bairro_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(2), 0))
        self.bairro_entry.grid(column=1, row=1, sticky=E)

        self.linha4.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.cidade_lb.grid(column=0, row=0, sticky=W, padx=(size.container_w(1), 0))
        self.cidade_entry.grid(column=0, row=1, sticky=W)
        self.cep_lb.grid(column=1, row=0, sticky=E, padx=(size.container_w(2), 0))
        self.cep_entry.grid(column=1, row=1, sticky=E)

        self.procedimento_lb.pack()
        self.procedimento_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.escolaridade_lb.pack()
        self.escolaridade_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.turno_lb.pack()
        self.turno_fr.pack(anchor=W, padx=size.container_w(14), pady=(size.container_h(1.5), size.container_h(3)))
        self.matutino.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.vespertino.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.noturno.pack(side=LEFT, padx=(0, size.container_w(1)))

        self.escola_lb.pack()
        self.escola_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.deficiencia_lb.pack()
        self.deficiencia_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.cor_lb.pack()
        self.cor_fr.pack(anchor=W, padx=size.container_w(14), pady=(size.container_h(1.5), size.container_h(3)))
        self.branca.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.negra.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.amarela.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.parda.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.indigena.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.desconhecida.pack(side=LEFT, padx=(0, size.container_w(1)))

        self.limitacao_lb.pack()
        self.limitacao_fr.pack(anchor=W, padx=size.container_w(14), pady=(size.container_h(1.5), size.container_h(3)))
        self.cognitiva.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.locomocao.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.visao.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.audicao.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.outras_lb.pack()
        self.outras_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.historico_lb.pack()
        self.historico_fr.pack(anchor=W, padx=size.container_w(14), pady=(size.container_h(1.5), size.container_h(3)))
        self.h_sim.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.h_nao.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.qual_lb.pack()
        self.qual_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.quando_lb.pack()
        self.quando_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.resultado_lb.pack()
        self.resultado_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.tratamento_lb.pack()
        self.tratamento_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.queixa_lb.pack()
        self.queixa_txt.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))
        self.data_queixa_lb.pack()
        self.data_queixa_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.medicamento_lb.pack()
        self.medicamento_fr.pack(anchor=W, padx=size.container_w(14), pady=(size.container_h(1.5), size.container_h(3)))
        self.m_sim.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.m_nao.pack(side=LEFT, padx=(0, size.container_w(1)))
        self.tipo_lb.pack()
        self.tipo_entry.pack(anchor=W, padx=size.container_w(10), pady=(0, size.container_h(3)))

        self.linha5.pack(anchor=E, padx=size.container_w(10), pady=(0, size.container_h(5)))
        self.salvar_btn.pack(side=LEFT, padx=(0, size.container_w(2)))
        self.cancelar_btn.pack(side=LEFT)

    def dados_cadastro(self):

        idade = self.calcular_idade()

        dados = [

            self.data_entry.get(),
            self.sus_entry.get(),
            self.paciente_entry.get().strip().upper(),
            self.data_nasc_entry.get(),
            idade,
            self.contato_entry.get(),
            self.rua_entry.get().strip().upper(),
            self.numero_entry.get().strip().upper(),
            self.bairro_entry.get().strip().upper(),
            self.cidade_entry.get().strip().upper(),
            self.cep_entry.get(),
            self.procedimento_entry.get().strip().upper(),
            self.escolaridade_entry.get().strip().upper(),
            self.turno_var.get().upper(),
            self.escola_entry.get().strip().upper(),
            self.deficiencia_entry.get().upper(),
            self.etnia_var.get().upper(),
            self.cognitiva_var.get().strip().upper(),
            self.locomocao_var.get().strip().upper(),
            self.visao_var.get().strip().upper(),
            self.audicao_var.get().strip().upper(),
            self.outras_entry.get().strip().upper(),
            self.historico_var.get().upper(),
            self.qual_entry.get().strip().upper(),
            self.quando_entry.get(),
            self.resultado_entry.get().strip().upper(),
            self.tratamento_entry.get().strip().upper(),
            self.queixa_txt.get('0.0', END).strip().upper(),
            self.data_queixa_entry.get().strip().upper(),
            self.medicamento_var.get().upper(),
            self.tipo_entry.get().strip().upper()

        ]
        return dados

    # Calcular idade exata da pessoa
    def calcular_idade(self):

        try:
            data_nasc = self.data_nasc_entry.get().replace('/', '')
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

    def cadastrar_paciente(self):

        dados = self.dados_cadastro()

        vazio = [i for i in dados if i == ""]

        if len(vazio) != 0:
            messagebox.showinfo('Atenção!', 'Preencha todos os campos do formulário')
        else:

            messagebox.showinfo('Atenção!', 'Estamos salvando suas informações')

            tabela = load_workbook(self.cadastro)
            ficha = tabela.active
            ficha.append(dados)
            tabela.save(self.cadastro)
            messagebox.showinfo('Infomativo', 'Dados salvos com sucesso')

            self.limpar_relatorio()

            tabela = pd.read_excel(self.cadastro)

            linha = tabela['DATA CONSULTA'].count()

            user = acessos.user['USER#00']
            comando = salvar_google_sheets
            comando.Salvar(user['ID'], f'Página1!A{linha+1}', [dados]).gravar()
            messagebox.showinfo('Atenção!', 'Dados salvos com sucesso')

    def contar_cadastro(self):

        tabela = pd.read_excel(self.cadastro)

        tot = tabela['DATA CONSULTA'].count()+1

        self.prontuario_n_entry.delete(0, 'end')
        self.prontuario_n_entry.insert(0, tot)
        self.data_entry.insert(0, self.data)

    def limpar_relatorio(self):

        self.data_entry.delete(0, 'end')
        self.sus_entry.delete(0, 'end')
        self.paciente_entry.delete(0, 'end')
        self.data_nasc_entry.delete(0, 'end')
        self.contato_entry.delete(0, 'end')
        self.rua_entry.delete(0, 'end')
        self.numero_entry.delete(0, 'end')
        self.bairro_entry.delete(0, 'end')
        self.cidade_entry.delete(0, 'end')
        self.cep_entry.delete(0, 'end')
        self.procedimento_entry.delete(0, 'end')
        self.escolaridade_entry.delete(0, 'end')
        self.turno_var = ""
        self.escola_entry.delete(0, 'end')
        self.deficiencia_entry.delete(0, 'end')
        self.etnia_var = ""
        self.cognitiva_var = ""
        self.locomocao_var = ""
        self.visao_var = ""
        self.audicao_var = ""
        self.outras_entry.delete(0, 'end')
        self.historico_var = ""
        self.qual_entry.delete(0, 'end')
        self.quando_entry.delete(0, 'end')
        self.resultado_entry.delete(0, 'end')
        self.tratamento_entry.delete(0, 'end')
        self.queixa_txt.delete(0.0, 'end')
        self.data_queixa_entry.delete(0, 'end')
        self.medicamento_var = ""
        self.tipo_entry.delete(0, 'end')

        self.matutino.deselect()
        self.vespertino.deselect()
        self.noturno.deselect()
        self.branca.deselect()
        self.negra.deselect()
        self.amarela.deselect()
        self.parda.deselect()
        self.indigena.deselect()
        self.desconhecida.deselect()
        self.h_sim.deselect()
        self.h_nao.deselect()
        self.m_sim.deselect()
        self.m_nao.deselect()
        self.cognitiva.deselect()
        self.locomocao.deselect()
        self.visao.deselect()
        self.audicao.deselect()
        self.sus_entry.focus_set()

        self.contar_cadastro()

    # Funções
    # Cadastros
    def formulario(self):

        import cadastro_pag2
        cadastro_pag2.Pesquisar_Cadastro(self.windows)

    # Voltar
    def inicio(self):
        from tela_boas_vindas import Tela_Inicial
        Tela_Inicial(self.windows)
