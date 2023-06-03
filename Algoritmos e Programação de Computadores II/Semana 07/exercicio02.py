# GUI - Interfaces gráficas (imagens)

from tkinter import Tk, Label, PhotoImage

root = Tk()

photo = PhotoImage(file="C:/Users/jobe_/Documents/TI/UNIVESP/Programas/Algoritmos e Programação de Computadores/Algoritmos e Programação de Computadores II/Semana 07/ferumbras.gif").subsample(1)
hello = Label(master=root, image=photo, width=498, height=498)
hello.pack()
root.mainloop()