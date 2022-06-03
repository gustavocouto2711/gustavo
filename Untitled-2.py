from tkinter import *

def entrada(valor):
    lb['text'] += valor

def limpar():
    lb['text'] = ''

root = Tk()

lb = Label(root, text='',font='Arial 26')
bt1 = Button (root, text='A', font='Arial', command=lambda: entrada('A'))
bt2 = Button(root, text='B', font='Arial', command=lambda: entrada('B'))
bt3 = Button(root, text='+', font='Arial', command=lambda: entrada('+'))
bt4 = Button(root, text='Limpar', font='Arial', command=limpar)

lb.grid()
bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()

root.mainloop()