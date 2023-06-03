# GUI - Interfaces gráficas (imagens e textos)

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()

photo = PhotoImage(file="C:/Users/jobe_/Documents/TI/UNIVESP/Programas/Algoritmos e Programação de Computadores/Algoritmos e Programação de Computadores II/Semana 07/ferumbras.gif").subsample(1)

image = Label(master=root, image=photo)
image.pack(side=TOP)

text = Label(master=root, font=("Roboto", 22), text="Ferumbras")
text.pack(side=BOTTOM)

root.mainloop()