from stringprep import in_table_a1
from tkinter import *
from turtle import width

#hack end
def imprimir():
    lb1['text'] = in1.get()
    print(in1.get())

#window
janela = Tk()


#geometria
janela.geometry('600x400+500+500')
janela.minsize(width=300,height=100)
janela.maxsize(width=900, height=400)

#widgets
lb1 = Label(janela, text='ola mundo!',font='arial 26')
in1 = Entry(janela, font='arial 26')
bt1 = Button(janela,text='Sair', font='arial 26', command=quit)
bt2 = Button(janela, text='imprimir', font='Arial 26', command=imprimir)

#layout
lb1.pack()
in1.pack()
bt1.pack()
bt2.pack()

#run
janela.mainloop()