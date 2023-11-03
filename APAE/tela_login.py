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
from consulta_principal import Cadastro_Consulta
import salvar_google_sheets

class Login:

    # Inicializador de propriedades
    def __init__(self, win, MOD, USER, PASS, LIN):


        self.font_lb = 20
        self.font_entry = 16
        self.tipo_font = 'times new roman'

        self.user = USER
        self.password = PASS
        self.lin = LIN

        self.windows = win
        self.limpar_windows()
        self.contains_principal()
        self.contatos()
        self.contains()
        if MOD == 0:
            self.campos_1()
        else:
            self.campos_2()
        self.imagen()

    # Limpar janela aberta
    def limpar_windows(self):

        for obj in self.windows.winfo_children():
            obj.destroy()

    # Containes principais
    def contains_principal(self):

        size = Responsive_windows(self.windows)

        self.header = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(3), fg_color='#000000', corner_radius=0)
        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(97), fg_color='#55BFCC', corner_radius=0)

        self.header.pack(fill=BOTH)
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

    # Containes frames
    def contains(self):

        size = Responsive_container(self.body)

        self.container = CTkFrame(self.body, width=size.container_w(92), height=size.container_h(90), corner_radius=0)
        self.container.pack(padx=size.container_w(4), pady=size.container_h(10))

        size = Responsive_container(self.container)

        self.logo_fr = CTkFrame(self.container, width=size.container_w(65), height=size.container_h(100), corner_radius=0, fg_color='#ffffff', border_width=0)
        self.logo_fr.pack(side=LEFT)

        self.login_fr = CTkFrame(self.container, width=size.container_w(35), height=size.container_h(100), corner_radius=0, fg_color='#E7F7F8', border_width=0)
        self.login_fr.pack(side=LEFT, fill=Y)

    # Campos login
    def campos_1(self):

        size = Responsive_container(self.login_fr)

        # Imagens
        self.logo_img = CTkImage(light_image=Image.open('Imagens/logo.png'), dark_image=Image.open('Imagens/logo.png'), size=(size.container_w(25), size.container_w(25)))
        self.user_img = CTkImage(light_image=Image.open('Imagens/user.png'), dark_image=Image.open('Imagens/user.png'), size=(size.container_w(4), size.container_w(4)))
        self.pass_img = CTkImage(light_image=Image.open('Imagens/pass.png'), dark_image=Image.open('Imagens/pass.png'), size=(size.container_w(4), size.container_w(4)))

        # Label
        self.logo_lb = CTkLabel(self.login_fr, text='', image=self.logo_img)
        self.logo_lb.pack(pady=(size.container_h(16), 0))

        # Frames
        self.linha_user = CTkFrame(self.login_fr, width=size.container_w(80), height=size.container_h(7), corner_radius=100, fg_color='#ffffff', border_width=2)
        self.linha_user.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), fill=X)
        self.linha1_user = CTkFrame(self.login_fr, width=size.container_w(80), height=size.container_h(7), corner_radius=100, fg_color='#ffffff', border_width=2)
        self.linha1_user.pack(padx=size.container_w(10), pady=size.container_h(2), fill=X)

        # Icon
        self.user_icon = CTkLabel(self.linha_user, text='', image=self.user_img)
        self.user_icon.pack(side=RIGHT, padx=(0, size.container_h(2)))

        self.pass_icon = CTkLabel(self.linha1_user, text='', image=self.pass_img)
        self.pass_icon.pack(side=RIGHT, padx=(0, size.container_h(2)))

        # Caixa de seleção
        self.views = CTkCheckBox(self.login_fr, text='Visualizar Senha', checkbox_width=size.container_w(4), checkbox_height=size.container_w(4), border_width=2, border_color='grey')
        self.views.pack(padx=size.container_w(15), anchor=W)

        # Botões
        self.acessar_btn = CTkButton(self.login_fr, command=self.login_0, text='LOGIN', width=size.container_w(80), height=size.container_h(7), fg_color='#55BFCC', hover_color='#55DFE6', text_color='#ffffff', corner_radius=100, font=("", size.container_w(4)))
        self.acessar_btn.pack(padx=size.container_w(10), pady=(size.container_h(2), 0))

        self.voltar_btn = CTkButton(self.login_fr, command=None, text='Voltar', width=size.container_w(10), height=size.container_h(4), fg_color='transparent', hover_color='#ffffff', text_color='grey', corner_radius=0, font=("", size.container_w(2.5)))
        self.voltar_btn.pack(padx=size.container_w(15), pady=(0, size.container_h(2)), anchor=E)


        size = Responsive_container(self.linha_user)

        # Entry
        self.user1_entry = CTkEntry(self.linha_user, font=("", size.container_w(4)), width=size.container_w(70), height=size.container_h(80), corner_radius=100, fg_color='transparent', border_width=0, placeholder_text='Usuario:')
        self.user1_entry.pack(side=LEFT, padx=(size.container_w(3), 0), pady=size.container_h(10))

        self.pass1_entry = CTkEntry(self.linha1_user, font=("", size.container_w(4)), width=size.container_w(70), height=size.container_h(80), corner_radius=100, fg_color='transparent', border_width=0, placeholder_text='Senha:')
        self.pass1_entry.pack(side=LEFT, padx=(size.container_w(3), 0), pady=size.container_h(10))

    # Campos login
    def campos_2(self):

        size = Responsive_container(self.login_fr)

        # Imagens
        self.logo_img = CTkImage(light_image=Image.open('Imagens/logo.png'), dark_image=Image.open('Imagens/logo.png'), size=(size.container_w(25), size.container_w(25)))
        self.user_img = CTkImage(light_image=Image.open('Imagens/user.png'), dark_image=Image.open('Imagens/user.png'), size=(size.container_w(4), size.container_w(4)))
        self.pass_img = CTkImage(light_image=Image.open('Imagens/pass.png'), dark_image=Image.open('Imagens/pass.png'), size=(size.container_w(4), size.container_w(4)))

        # Label
        self.logo_lb = CTkLabel(self.login_fr, text='', image=self.logo_img)
        self.logo_lb.pack(pady=(size.container_h(10), 0))

        # Frames
        self.linha_user = CTkFrame(self.login_fr, width=size.container_w(80), height=size.container_h(7), corner_radius=100, fg_color='#ffffff', border_width=2)
        self.linha_user.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), fill=X)
        self.linha1_user = CTkFrame(self.login_fr, width=size.container_w(80), height=size.container_h(7), corner_radius=100, fg_color='#ffffff', border_width=2)
        self.linha1_user.pack(padx=size.container_w(10), pady=(size.container_h(2), 0), fill=X)
        self.linha2_user = CTkFrame(self.login_fr, width=size.container_w(80), height=size.container_h(7), corner_radius=100, fg_color='#ffffff', border_width=2)
        self.linha2_user.pack(padx=size.container_w(10), pady=size.container_h(2), fill=X)

        # Icon
        self.user_icon = CTkLabel(self.linha_user, text='', image=self.user_img)
        self.user_icon.pack(side=RIGHT, padx=(0, size.container_h(2)))

        self.pass_icon = CTkLabel(self.linha1_user, text='', image=self.pass_img)
        self.pass_icon.pack(side=RIGHT, padx=(0, size.container_h(2)))

        self.rpass_icon = CTkLabel(self.linha2_user, text='', image=self.pass_img)
        self.rpass_icon.pack(side=RIGHT, padx=(0, size.container_h(2)))

        # Caixa de seleção
        self.views = CTkCheckBox(self.login_fr, text='Visualizar Senha', checkbox_width=size.container_w(4), checkbox_height=size.container_w(4), border_width=2, border_color='grey')
        self.views.pack(padx=size.container_w(15), anchor=W)

        # Botões
        self.acessar_btn = CTkButton(self.login_fr, command=self.login_1, text='LOGIN', width=size.container_w(80), height=size.container_h(7), fg_color='#55BFCC', hover_color='#55DFE6', text_color='#ffffff', corner_radius=100, font=("", size.container_w(4)))
        self.acessar_btn.pack(padx=size.container_w(10), pady=(size.container_h(2), 0))

        self.voltar_btn = CTkButton(self.login_fr, command=self.voltar, text='Voltar', width=size.container_w(10), height=size.container_h(4), fg_color='transparent', hover_color='#ffffff', text_color='grey', corner_radius=0, font=("", size.container_w(2.5)))
        self.voltar_btn.pack(padx=size.container_w(15), pady=(0, size.container_h(2)), anchor=E)


        size = Responsive_container(self.linha_user)

        # Entry
        self.user2_entry = CTkEntry(self.linha_user, font=("", size.container_w(4)), width=size.container_w(70), height=size.container_h(80), corner_radius=100, fg_color='transparent', border_width=0, placeholder_text='Usuario:')
        self.user2_entry.pack(side=LEFT, padx=(size.container_w(3), 0), pady=size.container_h(10))

        self.user2_entry.insert(0, self.user)

        self.pass2_entry = CTkEntry(self.linha1_user, font=("", size.container_w(4)), width=size.container_w(70), height=size.container_h(80), corner_radius=100, fg_color='transparent', border_width=0, placeholder_text='Senha:')
        self.pass2_entry.pack(side=LEFT, padx=(size.container_w(3), 0), pady=size.container_h(10))

        self.rpass2_entry = CTkEntry(self.linha2_user, font=("", size.container_w(4)), width=size.container_w(70), height=size.container_h(80), corner_radius=100, fg_color='transparent', border_width=0, placeholder_text='Repetir Senha:')
        self.rpass2_entry.pack(side=LEFT, padx=(size.container_w(3), 0), pady=size.container_h(10))

    # Imagem Lateral
    def imagen(self):

        size = Responsive_container(self.logo_fr)

        self.lateral_img = CTkImage(light_image=Image.open('Imagens/fundo.jpg'), dark_image=Image.open('Imagens/fundo.jpg'), size=(size.container_w(80), size.container_h(90)))

        # Label
        self.logo_lb = CTkLabel(self.logo_fr, text='', image=self.lateral_img)
        self.logo_lb.pack(padx=size.container_w(0.1), pady=size.container_w(0.1))

    # primeiro login
    def login_1(self):
        try:
            if self.pass2_entry.get() == self.rpass2_entry.get():
                messagebox.showinfo('Atenção!', 'Aguarde enquanto salvamos sua senha...')
                comando = salvar_google_sheets
                comando.Salvar('13qk5FtGr5QhN0iVBMcO_a0IcMHQS_n-Kh936k3byTAE', f'Acesso!b{self.lin+2}', [[self.pass2_entry.get()]]).gravar()
                messagebox.showinfo('Atenção!', 'Sua senha foi salva com sucesso estamos acessando sua página...')
                Cadastro_Consulta(self.windows, self.user)
            else:
                messagebox.showinfo('Atenção!', 'As senhas não se correspodem, tente novamente...')
                self.pass2_entry.delete(0, 'end')
                self.rpass2_entry.delete(0, 'end')
                self.pass2_entry.focus()
        except:
            messagebox.showinfo('Atenção!', 'Ocorreu 1 Erro no salvamento da sua senha...')

    # primeiro login
    def login_0(self):
        try:
            if self.user1_entry.get() == self.user and self.pass1_entry.get() == self.password:
                Cadastro_Consulta(self.windows, self.user)
            else:
                messagebox.showinfo('Atenção!', 'Senha ou usuario incorretos...')
                self.user1_entry.delete(0, 'end')
                self.pass1_entry.delete(0, 'end')
                self.user1_entry.focus()
        except:
            messagebox.showinfo('Atenção!', 'Ocorreu 1 Erro de login...')

    # Chamar Janela Inicio
    def voltar(self):

        from tela_boas_vindas import Tela_Inicial
        Tela_Inicial(self.windows)
