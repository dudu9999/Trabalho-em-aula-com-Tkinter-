from tkinter import *
from functools import partial
import tkinter.messagebox
import sys

class AtualizaPreco:
    def __init__(self, janela):
        width = 800
        height = 600
        janela.title("Sapataria do Seu IVO - Atualizar preços")

    def new_janAP(self):
        # Verifica se já foi criada
        if self.jan is None:
            self.jan = Tk()
            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_jan)

            self.l = Label(self.jan, text='Atualizar preços')
            self.l.grid()

            self.jan.geometry('800x600')
        else:
            # Se já foi, basta colocá-la na frente
            self.jan.lift()

        def new_janSA(self):
            # self.janela.destroy()
            sys.exit()
            l1.text['Para Fechar clique no X vermelho acima! ']

        def fecha_jan(self):
            # Seta de novo em None para recriar quando abrir
            self.jan.destroy()
            self.jan = None

root = Tk()
AtualizaPreco(root)
root.geometry('800x600')
root.mainloop()