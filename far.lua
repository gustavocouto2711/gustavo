from tkinter import *

root = Tk()
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)

lb1 = Label(root, text'Label 1',bg='red',fg='white',font='arial 30 bold')
lb2 = Label(root, text'Label 1',bg='red',fg='white',font='arial 30 bold')
lb3 = Label(root, text'Label 1',bg='red',fg='white',font='arial 30 bold')
lb4 = Label(root, text'Label 1',bg='red',fg='white',font='arial 30 bold')