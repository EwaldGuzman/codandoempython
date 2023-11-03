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

class Enviar_email:

    # Inicializador de propriedades
    def __init__(self, win):

        self.cadastro = pathlib.Path('Tabelas_xlsx/Cadastros_xlsx/Cadastro de Prontuario.xlsx').absolute()

        self.data = datetime.now().strftime('%d/%m/%Y')
        self.font_lb = 20
        self.font_entry = 16
        self.tipo_font = 'times new roman'

        self.windows = win
        self.limpar_windows()

        self.contains_principal()
        self.contatos()
        # self.list_menu()
        self.contains()
        self.campos()


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
        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(100), fg_color='#FFFFFF', corner_radius=0)

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

    # Containes de campo
    def contains(self):

        size = Responsive_container(self.body)


        self.campo_fr = CTkFrame(self.body, width=size.container_w(100), height=size.container_h(100), fg_color='transparent', border_width=1)
        self.enviar_fr = CTkFrame(self.campo_fr, width=size.container_w(70), height=size.container_h(90), fg_color='transparent')

        self.campo_fr.pack(padx=size.container_w(2))
        self.enviar_fr.pack(padx=size.container_w(5), pady=size.container_h(3), side=LEFT)

    # Campos de envio
    def campos(self):

        size = Responsive_container(self.enviar_fr)

        # Label
        self.destinatario = CTkLabel(self.enviar_fr, text='Destino', font=('', size.container_w(1.5)))
        self.assunto = CTkLabel(self.enviar_fr, text='Assunto', font=('', size.container_w(1.5)))
        self.mensagem = CTkLabel(self.enviar_fr, text='Mensagem', font=('', size.container_w(1.5)))

        # Entry
        self.destinatario_entry = CTkEntry(self.enviar_fr, font=('', size.container_w(1.5)), width=size.container_w(70), height=size.container_h(4), corner_radius=100, border_width=1)
        self.assunto_entry = CTkEntry(self.enviar_fr, font=('', size.container_w(1.5)), width=size.container_w(70), height=size.container_h(4), corner_radius=100, border_width=1)
        self.mensagem_entry = CTkTextbox(self.enviar_fr, font=('', size.container_w(1.5)), width=size.container_w(70), height=size.container_h(30), border_width=1)

        # Buttons
        self.buttons = CTkFrame(self.enviar_fr, fg_color='transparent')
        self.enviar_btn = CTkButton(self.buttons, text='Enviar', font=('', size.container_w(1)), width=size.container_w(10), height=size.container_h(3), command=self.enviar)
        self.cancelar_btn = CTkButton(self.buttons, text='Cancelar', font=('', size.container_w(1)), width=size.container_w(10), height=size.container_h(3), command=None)

        # Poss
        self.destinatario.grid(column=0, row=0, sticky=E, padx=size.container_w(1))
        self.destinatario_entry.grid(column=1, row=0, sticky=W, pady=size.container_h(1))
        self.assunto.grid(column=0, row=1, sticky=E, padx=size.container_w(1))
        self.assunto_entry.grid(column=1, row=1, sticky=W, pady=(0, size.container_h(1)))
        # self.mensagem.grid(column=0, columnspan=2, row=2, sticky=W)
        self.mensagem_entry.grid(column=0, columnspan=2, row=3, sticky=EW)
        self.buttons.grid(column=1, row=4, sticky=E, pady=size.container_h(2))
        self.enviar_btn.pack(side=LEFT, padx=size.container_w(1))
        self.cancelar_btn.pack(side=LEFT)

    # Fechar App
    def fechar_app(self):

        self.windows.quit()

    # Voltar pagina
    def voltar(self):

        from cadastro_pag1 import Cadastro_paciente
        Cadastro_paciente(self.windows)

    # Enviar email
    def enviar(self):
        anexo = r'X:\         \APAE\Tabelas_xlsx\Cadastros_xlsx\Cadastro de Prontuario.xlsx'
        arquivo = 'Cadastro de Prontuario.xlsx'
        import enviar_email
        enviar_email.Enviar_Email(
            self.destinatario_entry.get(),
            self.assunto_entry.get(),
            self.mensagem_entry.get(0.0, 'end').strip(),
            anexo,
            arquivo
        )

        messagebox.showinfo('Informação', 'Email enviado com sucesso!')
