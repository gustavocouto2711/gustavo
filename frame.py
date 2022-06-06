from tkinter import*
root = Tk()
#widgets
fr1 = Frame(root)
fr2 = Frame(root)


lb1 = Label(fr1, text='Label no frame 1')
lb2 = Label(fr2, text='Label no frame 2')

bt1_fr1 = Button (fr1, text= 'Bt mp frame 1', font = 28)
bt1_fr2 = Button (fr2, text= 'Bt mp frame 2', font = 28)
#Layout
fr1.pack()
fr2.pack()

lb1.grid(row=0, column=0)
bt1_fr1.grid(row=1, column=1)
lb2.grid(row=0, column=0)
bt1_fr2.grid(row=1, column=1)
root.mainloop()