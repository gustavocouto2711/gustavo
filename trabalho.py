from tkinter import *

def soma():
    lb1['text']=int (in1.get())+int(in2.get())
    
    
#window
janela = Tk()

fr1 = Frame(janela)
fr2 = Frame(janela)

#widgets
lb1 = Label(fr1, text='resultado')
in1 = Entry(fr1)
in2 = Entry(fr1)
bt1 = Button(fr2,text='Soma', command=soma)

#Layout
lb1.pack()
in1.pack()
in2.pack()
bt1.pack()

#run
janela.mainloop()