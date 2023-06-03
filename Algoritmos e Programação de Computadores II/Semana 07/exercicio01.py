# GUI - Interfaces gráficas (textos)

from tkinter import Tk, Label

root = Tk()

hello = Label(master = root, text = "Hello, World!")

hello.pack()

root.mainloop()