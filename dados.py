from sqlite3 import Row
from tkinter import *

root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)

lb1_fr1 = Label(fr1, text='Dados pessoais')
lb2_fr1 = Label(fr1, text='Nome:')
in1_fr1 = Entry(fr1)
lb3_fr1 = Label(fr1, text='Data Nacs:')
in2_fr1 = Entry(fr1)
lb4_fr1 = Label(fr1, text='CPF:')
in3_fr1 = Entry(fr1)
lb5_fr1 = Label(fr1, text='Telefone:')
in4_fr1 = Entry(fr1)

lb6_fr2 = Label(fr2, text='Endereço')
lb7_fr2 = Label(fr2, text='Rua:')
in5_fr2 = Entry(fr2)
lb8_fr2 = Label(fr2, text='bairro:')
in6_fr2 = Entry(fr2)
lb9_fr2 = Label(fr2, text='Cidade:')
in7_fr2 = Entry(fr2)
lb10_fr2 = Label(fr2, text='N:')
in8_fr2 = Entry(fr2)
lb11_fr2 = Label(fr2, text='UF:')
in9_fr2 = Entry(fr2)

bt1_fr3 = Button(fr3, text='Gravar Dados', font = 28)
bt2_fr3 = Button(fr3, text='Listar Dados', font = 28)

fr1.pack()
fr2.pack()
fr3.pack()

lb1_fr1.grid(row=0, column=0, sticky=NSEW)
lb2_fr1.grid(row=1, column=0, sticky=NSEW)
in1_fr1.grid(row=1, column=1, sticky=NSEW)
lb3_fr1.grid(row=2, column=0, sticky=NSEW)
in2_fr1.grid(row=2, column=1, sticky=NSEW)
lb4_fr1.grid(row=3, column=0, sticky=NSEW)
in3_fr1.grid(row=3, column=1, sticky=NSEW)
lb5_fr1.grid(row=4, column=0, sticky=NSEW)
in4_fr1.grid(row=4, column=1, sticky=NSEW)

lb6_fr2.grid(row=0, column=0, sticky=NSEW)
in5_fr2.grid(row=1, column=1, sticky=NSEW)
lb7_fr2.grid(row=1, column=0, sticky=NSEW)
in6_fr2.grid(row=2, column=1, sticky=NSEW)
lb8_fr2.grid(row=2, column=0, sticky=NSEW)
in7_fr2.grid(row=2, column=1, sticky=NSEW)
lb9_fr2.grid(row=2, column=2, sticky=NSEW)
in8_fr2.grid(row=1, column=5, sticky=NSEW)
lb10_fr2.grid(row=1, column=4, sticky=NSEW)
in9_fr2.grid(row=2, column=5, sticky=NSEW)
lb11_fr2.grid(row=3, column=3, sticky=NSEW)

bt1_fr3.grid(row=0, column=0, sticky=NSEW)
bt1_fr3.grid(row=1, column=1, sticky=NSEW)

root.mainloop()