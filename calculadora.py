from tkinter import *

def entrada (valor):
    lb['text'] += valor
def limpar():
    lb['text'] = ''
def resultado():
    x=eval(lb['text'])
    lb['text']=str(x)



root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)

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

lb = Label(fr1, text='', font='Arial 26')
bt0_fr2 = Button(fr2, text='0', font='Arial 26', command=lambda: entrada('0'))
bt1_fr2 = Button(fr2, text='1', font='Arial 26', command=lambda: entrada('1'))
bt2_fr2 = Button(fr2, text='2', font='Arial 26', command=lambda: entrada('2'))
bt3_fr2 = Button(fr2, text='3', font='Arial 26', command=lambda: entrada('3'))
bt4_fr2 = Button(fr2, text='4', font='Arial 26', command=lambda: entrada('4'))
bt5_fr2 = Button(fr2, text='5', font='Arial 26', command=lambda: entrada('5'))
bt6_fr2 = Button(fr2, text='6', font='Arial 26', command=lambda: entrada('6'))
bt7_fr2 = Button(fr2, text='7', font='Arial 26', command=lambda: entrada('7'))
bt8_fr2 = Button(fr2, text='8', font='Arial 26', command=lambda: entrada('8'))
bt9_fr2 = Button(fr2, text='9', font='Arial 26', command=lambda: entrada('9'))
bt10_fr2 = Button(fr2, text='+', font='Arial 26', command=lambda: entrada('+'))
bt11_fr2 = Button(fr2, text='-', font='Arial 26', command=lambda: entrada('-'))
bt12_fr2 = Button(fr2, text='*', font='Arial 26', command=lambda: entrada('*'))
bt13_fr2 = Button(fr2, text='/', font='Arial 26', command=lambda: entrada('/'))
bt14_fr2 = Button(fr2, text='=', font='Arial 26', command=lambda: resultado())
bt15_fr2 = Button(fr2, text='C', font='Arial 26', command=lambda: limpar(fr2lb.grid(row=0, column=0, columnspan=4, sticky=NSEW)))

fr1.pack()
fr2.pack()
lb.pack()
bt0_fr2.grid(row=4, column=2, sticky=NSEW)
bt1_fr2.grid(row=3, column=1, sticky=NSEW)
bt2_fr2.grid(row=3, column=2, sticky=NSEW)
bt3_fr2.grid(row=3, column=3, sticky=NSEW)
bt4_fr2.grid(row=2, column=1, sticky=NSEW)
bt5_fr2.grid(row=2, column=2, sticky=NSEW)
bt6_fr2.grid(row=2, column=3, sticky=NSEW)
bt7_fr2.grid(row=1, column=1, sticky=NSEW)
bt8_fr2.grid(row=1, column=2, sticky=NSEW)
bt9_fr2.grid(row=1, column=3, sticky=NSEW)
bt10_fr2.grid(row=3, column=4, sticky=NSEW)
bt11_fr2.grid(row=2, column=4, sticky=NSEW)
bt12_fr2.grid(row=3, column=4, sticky=NSEW)
bt13_fr2.grid(row=1, column=4, sticky=NSEW)
bt14_fr2.grid(row=4, column=4, sticky=NSEW)
bt15_fr2.grid(row=4, column=3, sticky=NSEW)

root.mainloop()