from tkinter import *

def entrada (valor):
    lb['text'] += valor
def limpar():
    lb['text'] = ''
def resultado():
    x=eval(lb['text'])
    lb['text']=str(x)



root = Tk()


#geometria
root.geometry('600x400+500+500')
root.minsize(width=300,height=100)
root.maxsize(width=900, height=400)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=2)
root.grid_rowconfigure(3, weight=3)
root.grid_rowconfigure(4, weight=4)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=2)
root.grid_columnconfigure(3, weight=3)
root.grid_columnconfigure(4, weight=4)

lb = Label(root, text='', font='Arial 26')
bt0 = Button(root, text='0', font='Arial 26', command=lambda: entrada('0'))
bt1 = Button(root, text='1', font='Arial 26', command=lambda: entrada('1'))
bt2 = Button(root, text='2', font='Arial 26', command=lambda: entrada('2'))
bt3 = Button(root, text='3', font='Arial 26', command=lambda: entrada('3'))
bt4 = Button(root, text='4', font='Arial 26', command=lambda: entrada('4'))
bt5 = Button(root, text='5', font='Arial 26', command=lambda: entrada('5'))
bt6 = Button(root, text='6', font='Arial 26', command=lambda: entrada('6'))
bt7 = Button(root, text='7', font='Arial 26', command=lambda: entrada('7'))
bt8 = Button(root, text='8', font='Arial 26', command=lambda: entrada('8'))
bt9 = Button(root, text='9', font='Arial 26', command=lambda: entrada('9'))
bt10 = Button(root, text='+', font='Arial 26', command=lambda: entrada('+'))
bt11 = Button(root, text='-', font='Arial 26', command=lambda: entrada('-'))
bt12 = Button(root, text='*', font='Arial 26', command=lambda: entrada('*'))
bt13 = Button(root, text='/', font='Arial 26', command=lambda: entrada('/'))
bt14 = Button(root, text='=', font='Arial 26', command=lambda: resultado())
bt15 = Button(root, text='C', font='Arial 26', command=lambda: limpar())

lb.grid(row=0, column=0, columnspan=4, sticky=NSEW)
bt0.grid(row=4, column=2, sticky=NSEW)
bt1.grid(row=3, column=1, sticky=NSEW)
bt2.grid(row=3, column=2, sticky=NSEW)
bt3.grid(row=3, column=3, sticky=NSEW)
bt4.grid(row=2, column=1, sticky=NSEW)
bt5.grid(row=2, column=2, sticky=NSEW)
bt6.grid(row=2, column=3, sticky=NSEW)
bt7.grid(row=1, column=1, sticky=NSEW)
bt8.grid(row=1, column=2, sticky=NSEW)
bt9.grid(row=1, column=3, sticky=NSEW)
bt10.grid(row=3, column=4, sticky=NSEW)
bt11.grid(row=2, column=4, sticky=NSEW)
bt12.grid(row=3, column=4, sticky=NSEW)
bt13.grid(row=1, column=4, sticky=NSEW)
bt14.grid(row=4, column=4, sticky=NSEW)
bt15.grid(row=4, column=3, sticky=NSEW)

root.mainloop()