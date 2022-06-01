from tkinter import *

# back-end
def IMC():
    
    # if peso numerico e altura numerico faça:
        ## resultado = peso / (altura * altura)
    #else
        # erro!
    
    if en1.get().replace('.','',1).isdigit() and en2.get().replace('.','',1).isdigit():  
        peso = float(en1.get())
        altura = float(en2.get())
        resultado = peso / (altura*altura)
        lb3['text']=resultado
    else:
        lb3['text']='Entrada Invalida'

#window
janela = Tk()

#geometria
janela.geometry('600x400+500+500')
janela.minsize(width=300,height=100)
janela.maxsize(width=900, height=400)

#widgets
lb1 = Label (janela, text='Peso', font= 'Arial 26')
en1 = Entry (janela, font='Arial 26')
lb2 = Label (janela, text='Altura', font= 'Arial 26')
en2 = Entry (janela, font='Arial 26')
bt1 = Button(janela, text='IMC', font='Arial 26', command=IMC)
lb3 = Label(janela, text='Resultado', font='Arial 26')
#layout
lb1.grid(row=0, column=0)
en1.grid(row=0, column=1)
lb2.grid(row=1, column=0)
en2.grid(row=1, column=1)
bt1.grid(row=2, column=1)
lb3.grid(row=3, column=1)
janela.mainloop()