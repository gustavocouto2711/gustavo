from tkinter import *


def soma():
    if lb1['text'] <10: 
        lb1['text']+= 1
    else:
        pass
def subitrair():
    if lb1['text'] >-10:
        lb1['text'] -=1
    else:
        pass




#window
janela=Tk()
janela.grid_rowconfigure(0,weight=1)
janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=1)
janela.grid_columnconfigure(2,weight=1)
janela.bind('-', lambda event: subitrair())
janela.bind('+', lambda event: soma()) 

#widgtes
lb1 = Label(janela, text=0,font='Arial')
bt1 = Button(janela,text='+', command=soma)
bt2 = Button(janela,text='-', command=subitrair)
#organizar os widgets
lb1.grid(row=0, column=1, sticky=NSEW)
bt1.grid(row=0, column=2, sticky=NSEW)
bt2.grid(row=0, column=0, sticky=NSEW)


janela.mainloop()