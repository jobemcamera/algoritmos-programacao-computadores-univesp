# GUI - Interfaces gráficas - Eventos (key_press)

from tkinter import Tk, Text, BOTH
from tkinter.messagebox import showinfo
from time import strftime, strptime

def key_pressed(event):
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    print('mouse left clicked')

def mouse_clicked_right(event):
    print('mouse right clicked')

root = Tk()
root.geometry('280x100+500+100')
root.resizable(False, False)  
text = Text(root, width=20, height=5)
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-3>', mouse_clicked_right)
text.pack(expand=True, fill=BOTH)
root.mainloop()