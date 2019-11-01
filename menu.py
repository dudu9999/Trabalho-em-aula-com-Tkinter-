from tkinter import *
from functools import partial
import tkinter.messagebox
import sys

import Cadastro
import CadastroCor
import AtualizarPreco
import ExportarTxt
import ImportarTxt
import Relatorio
import Vender

class Menu:
    def __init__(self, janela):  # Inicia como None
        width = 800
        height = 600
        janela.title("Sapataria do Seu IVO - Menu Inicial")

        self.b1 = Button(janela, text='Cadastrar Tenis')
        self.b1["command"] = partial(Cadastro.Cadastro.new_janCT, self)
        self.b1.place(x=335, y=245)

        self.b2 = Button(janela, text='Relatório Geral')
        self.b1["command"] = partial(Relatorio.Relatorio.new_janRG, self)
        self.b2.place(x=335, y=285)

        self.b3 = Button(janela, text='Realizar Venda')
        self.b1["command"] = partial(Vender.Vender.new_janRV, self)
        self.b3.place(x=335, y=325)

        self.b4 = Button(janela, text='Atualizar preços')
        self.b1["command"] = partial(AtualizarPreco.AtualizaPreco.new_janAP, self)
        self.b4.place(x=335, y=365)

        self.b5 = Button(janela, text='Cadastrar Cores')
        self.b1["command"] = partial(CadastroCor.CadastroCor.new_janCC, self)
        self.b5.place(x=335, y=405)

        self.b6 = Button(janela, text='Guarda no TXT')
        self.b1["command"] = partial(ExportarTxt.ExportarTxt.new_janGT, self)
        self.b6.place(x=335, y=445)

        self.b7 = Button(janela, text='Recupera do TXT')
        self.b1["command"] = partial(ImportarTxt.ImportarTxt.new_janRT, self)
        self.b7.place(x=335, y=485)

        self.b8 = Button(janela, text='Sair', command=root.destroy)
        self.b8.place(x=335, y=525)

        self.l1 = Label(janela, text='raiz!')
        self.l1.place(x=750, y=560)

        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.jan = None
        self.caixa = Frame(janela)
        self.caixa.grid()

        def new_janSA(self):
            self.janela.destroy()
            sys.exit()
            l1.text['Para Fechar clique no X vermelho acima! ']

        def fecha_jan(self):
            # Seta de novo em None para recriar quando abrir
            self.jan.destroy()
            self.jan = None

root = Tk()

Menu(root)
root.geometry('800x600')

root.mainloop()
Menu()