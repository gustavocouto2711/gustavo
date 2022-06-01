from tkinter import *

def soma():
    lb1['text']=int (in1.get())+int(in2.get())
    
    
#window
janela = Tk()

#widgets
lb1 = Label(janela, text='resultado')
in1 = Entry(janela)
in2 = Entry(janela)
bt1 = Button(janela,text='Soma', command=soma)

#Layout
lb1.pack()
in1.pack()
in2.pack()
bt1.pack()

#run
janela.mainloop()