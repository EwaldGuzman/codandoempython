
# Bibliotecas Python
from customtkinter import *
from PIL import Image

# Bibliotecas Minhas
from geometria_sistema import Responsive_windows, Responsive_container
from cadastro_pag1 import Cadastro_paciente
from consulta_principal import Cadastro_Consulta
from tela_login import Login
from chamar_google_sheets import Chamar

class Tela_Inicial:

    def __init__(self, win):

        self.windows = win

        self.limpar_windows()

        self.acesso_user = Chamar(ID='13qk5FtGr5QhN0iVBMcO_a0IcMHQS_n-Kh936k3byTAE', RANGE='Acesso!A2:F20').main()

        self.contains_principal()
        self.contains()
        self.boas_vindas()
        self.menu()
        self.recepcao(self.atendente)
        self.user(self.user1)
        self.adm(None)

        # self.add_user()
        # Desligar app
        self.windows.bind("<Key>", self.fechar_app)

    def limpar_windows(self):

        for obj in self.windows.winfo_children():
            obj.destroy()

    def contains_principal(self):

        size = Responsive_windows(self.windows)

        self.body = CTkFrame(self.windows, width=size.windows_w(100), height=size.windows_h(100), fg_color=None, corner_radius=0)

        self.body.pack(fill=BOTH)

    def fechar_app(self, event):

        if event.char == "":
            self.windows.quit()

    def contains(self):

        size = Responsive_container(self.body)

        self.imagem_fr = CTkFrame(self.body, width=size.container_w(100), height=size.container_h(57), fg_color='#FFFFFF', corner_radius=0)
        self.menu_fr = CTkFrame(self.body, width=size.container_w(100), height=size.container_h(30), fg_color='#FFFFFF', corner_radius=0)
        self.footer_fr = CTkFrame(self.body, width=size.container_w(100), height=size.container_h(20), fg_color='#00B0F0', corner_radius=0)

        self.imagem_fr.pack()
        self.menu_fr.pack(fill=BOTH)
        self.footer_fr.pack(fill=BOTH)

        size = Responsive_container(self.menu_fr)

        self.contains_fr = CTkFrame(self.menu_fr, width=size.container_w(30), height=size.container_h(100), fg_color='transparent')
        self.contains_fr.pack(side=LEFT)

        self.lista_fr = CTkFrame(self.menu_fr, width=size.container_w(70), height=size.container_h(100), fg_color='transparent', corner_radius=0)
        self.lista_fr.pack()

        size = Responsive_container(self.imagem_fr)

        self.img_fundo = CTkImage(light_image=Image.open('Imagens/tela_inicio2.png'), dark_image=Image.open(
            'Imagens/tela_inicio2.png'), size=(size.container_w(100), size.container_h(100)))

        size = Responsive_container(self.footer_fr)

        # self.img_footer = CTkImage(light_image=Image.open('Imagens/teste-2.jpg'), dark_image=Image.open('Imagens/teste-2.jpg'), size=(size.container_w(100), size.container_h(100)))

        self.imagem_lb = CTkLabel(self.imagem_fr, text='', image=self.img_fundo)
        # self.imagem2_lb = CTkLabel(self.footer_fr, text='', image=self.img_footer)
        self.imagem_lb.pack()
        # self.imagem2_lb.pack()

    def boas_vindas(self):

        texto = '''
Pagina de cadastro da 
Associação de Pais e Amigos dos
Excepcionais - (APAE)
        '''

        size = Responsive_container(self.contains_fr)

        # container
        self.titulo_fr = CTkFrame(self.contains_fr, width=size.container_w(100), height=size.container_h(100), fg_color='transparent')
        self.titulo_fr.pack(side=LEFT, pady=(size.container_h(3), 0), padx=size.container_w(10), fill=BOTH)

        self.bem_vindo = CTkLabel(self.titulo_fr, text='BEM-VINDO', font=('times new roman', size.container_w(15)))
        self.descricao = CTkLabel(self.titulo_fr, text=texto, font=('times new roman', size.container_w(6)), justify=LEFT)


        self.bem_vindo.pack(anchor=W, pady=(size.container_h(3), 0), padx=size.container_w(5))
        self.descricao.pack(anchor=W, pady=(0, size.container_h(3)), padx=size.container_w(5))

    def menu(self):

        size = Responsive_container(self.lista_fr)

        # container
        self.menu_cont_fr = CTkFrame(self.lista_fr, width=size.container_w(100), height=size.container_h(100), fg_color='transparent')
        self.menu_cont_fr.pack(fill=BOTH, anchor='center')

    def user(self, comando):

        user = list(self.acesso_user['USER'])

        size = Responsive_container(self.menu_cont_fr)

        # container
        self.user_fr = CTkFrame(self.menu_cont_fr, width=size.container_w(15), height=size.container_h(80), fg_color='transparent', corner_radius=0)
        self.user_fr.pack(side=LEFT, pady=size.container_h(15), padx=size.container_w(5), fill=Y)

        size = Responsive_container(self.user_fr)

        self.perfil = CTkImage(light_image=Image.open('Imagens/consulta.png'), dark_image=Image.open('Imagens/consulta.png'), size=(size.container_w(74), size.container_h(58)))

        self.perfil_lb = CTkLabel(self.user_fr, text='', image=self.perfil)
        self.perfil_lb.pack()

        self.cargo = CTkOptionMenu(self.user_fr, values=user[1:], fg_color='#00AAA8', text_color='#ffffff', corner_radius=20, button_color='#00AAA8',
                                   width=size.container_w(80), height=size.container_h(15), font=('', size.container_w(10)),
                                   button_hover_color='#00AAA8', command=self.login)
        self.cargo.pack(padx=size.container_w(0.8), pady=(size.container_h(6), size.container_h(10)))

        self.cargo.set('CONSULTAS')

    def adm(self, comando):

        size = Responsive_container(self.menu_cont_fr)

        # container
        self.user_fr = CTkFrame(self.menu_cont_fr, width=size.container_w(15), height=size.container_h(80), fg_color='transparent', corner_radius=0)
        self.user_fr.pack(side=LEFT, pady=size.container_h(15), fill=Y)

        size = Responsive_container(self.user_fr)

        self.perfil = CTkImage(light_image=Image.open('Imagens/suporte.png'), dark_image=Image.open('Imagens/suporte.png'), size=(size.container_w(74), size.container_h(58)))

        self.perfil_lb = CTkLabel(self.user_fr, text='', image=self.perfil)
        self.perfil_lb.pack(pady=(0, size.container_h(6)))

        # self.funcao = CTkLabel(self.user_fr, text='ADM', font=('', 20), width=size.container_w(80), height=size.container_h(10))
        # self.funcao.pack(padx=size.container_w(1), pady=(size.container_h(1), size.container_h(10)))

        self.acessar_btn = CTkButton(self.user_fr, command=comando, text='ADM', text_color='#ffffff', font=('', size.container_w(10)), width=size.container_w(80), height=size.container_h(15), corner_radius=100, fg_color='#00AAA8')
        self.acessar_btn.pack(padx=size.container_w(10))

    def recepcao(self, comando):

        size = Responsive_container(self.menu_cont_fr)

        # container
        self.user_fr = CTkFrame(self.menu_cont_fr, width=size.container_w(15), height=size.container_h(80), fg_color='transparent', corner_radius=0)
        self.user_fr.pack(side=LEFT, pady=size.container_h(15), fill=Y)

        size = Responsive_container(self.user_fr)

        self.perfil = CTkImage(light_image=Image.open('Imagens/relatorio.png'), dark_image=Image.open('Imagens/relatorio.png'), size=(size.container_w(74), size.container_h(58)))

        self.perfil_lb = CTkLabel(self.user_fr, text='', image=self.perfil)
        self.perfil_lb.pack(pady=(0, size.container_h(6)))

        # self.funcao = CTkLabel(self.user_fr, text='RECEPÇÃO', font=('', 20), width=size.container_w(80), height=size.container_h(10))
        # self.funcao.pack(padx=size.container_w(1), pady=(size.container_h(1), size.container_h(10)))

        self.acessar_btn = CTkButton(self.user_fr, command=comando, text='RECEPÇÃO', text_color='#ffffff', font=('', size.container_w(10)), width=size.container_w(80), height=size.container_h(15), corner_radius=100, fg_color='#00AAA8')
        self.acessar_btn.pack(padx=size.container_w(10))

    def user1(self, a):
        Cadastro_Consulta(self.windows, self.cargo.get())

    def atendente(self):
        Cadastro_paciente(self.windows)

    def login(self, a):
        usuario = self.cargo.get()
        infor = self.acesso_user.loc[self.acesso_user['USER'] == usuario, 'PASSWORD']
        senha = list(infor)[0]
        linha = infor.index[0]

        if senha == 'adicionar':
            Login(self.windows, 1, usuario, senha, linha)
        else:
            Login(self.windows, 0, usuario, senha, linha)



