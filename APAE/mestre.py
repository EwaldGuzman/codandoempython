
# Bilbiotecas Pyrhon
from customtkinter import *


# Bibliotecas Minhas
from tela_boas_vindas import Tela_Inicial


# Classe Principal
class main:

    # Propriedades da classe
    def __init__(self):

        self.font_lb = 'arial'
        self.size_font_lb = 16
        self.size_font_entry = 18
        self.stile_font_lb = 'bold'
        self.cor_entry = '#FFFFFF'

        self.screem()
        self.user = Tela_Inicial(self.windows)

    # Iniciar janela
    def screem(self):

        # janela
        self.windows = CTk()
        self.windows.attributes('-fullscreen', True)
        self.windows.configure(fg_color='#ffffff')


if __name__ == '__main__':
    app = main()
    app.windows.mainloop()
