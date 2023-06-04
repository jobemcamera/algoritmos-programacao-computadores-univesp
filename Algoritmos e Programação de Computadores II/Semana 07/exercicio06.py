# GUI - Interfaces gráficas - Eventos - Entry 

from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime


def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))
    entry.delete(0, 'end')


root = Tk()
root.geometry('280x100+500+100')
root.resizable(False, False)  
              
label = Label(root, text='Write a date:\n(MMM DD, YYYY) ')
label.grid(row=0, column=0, padx=10)

entry = Entry(root)
entry.grid(row=0, column=1)

button = Button(root, text='Click', command=clicked)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()
