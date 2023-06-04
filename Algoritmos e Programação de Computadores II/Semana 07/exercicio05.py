# GUI - Interfaces gráficas - Eventos

from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime("Day: %d %b %Y\nTime: %H:%M:%S%p\n", localtime())
    showinfo(message=time)

root = Tk()
button = Button(root, text="Click", command=clicked)


button.pack()
root.mainloop()
