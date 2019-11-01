from tkinter import *
from functools import partial
import tkinter.messagebox
import sys

class Cadastro:
    def __init__(self, janela):
        width = 800
        height = 600
        janela.title("Sapataria do Seu IVO - Cadastro")

    def new_janCT(self, *args):
        super(Cadastro, self).new_janCT()

        # Verifica se já foi criada
        if self.jan is None:
            self.jan = Tk()
            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_jan)

            self.l = Label(self.jan, text='Cadastro de tenis')
            self.l.grid()

            self.lblistbox = Label(self.jan, text="ESTOQUE DO TIO IVO", bg='lightSteelBlue3', fg='blue').place(x=50, y=60)

            self.listbox = Listbox(self.jan, width=60)
            self.listbox.insert(0, "Criando listbox = 1")

            self.listbox.place(x=100, y=200)

            self.lblistbox1 = Label(self.jan, text="Inserindo dados", bg='lightSteelBlue3', fg='blue').place(x=20, y=10)
            self.inserir = StringVar()
            self.txtlistbox = Entry(self.jan, textvariable=self.inserir, width=47).place(x=120, y=10)
            self.btninserir = Button(self.jan, text='INSERIR', height=1, width=10, command=self.inserindoDados).place(
                x=325, y=30)

            self.jan.geometry('800x600')
        else:
            # Se já foi, basta colocá-la na frente
            self.jan.lift()

    def inserindoDados(self, *args):
        self.listbox.insert(END, self.inserir.get())

    def new_janSA(self):
        # self.janela.destroy()
        sys.exit()
        l1.text['Para Fechar clique no X vermelho acima! ']

    ###########################################################################################

    def fecha_jan(self):
        # Seta de novo em None para recriar quando abrir
        self.jan.destroy()
        self.jan = None


root = Tk()
Cadastro(root)
root.geometry('800x600')
root.mainloop()
