import tkinter
from tkinter.filedialog import *
from tkinter import  *
root = Tk()
root.title('Memorizer')
root.geometry('800x800')
root.config(background='red')







fopen = Button(root,text = 'Open')
ldelete = Button(root,text='Delete list')
fsave = Button(root,text = 'Save')
lAdd = Button(root,text = 'Add item')
item = Entry(root)



root.mainloop()
