from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText

class area(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("text area")
        self.geometry('500x300')

        self.a=ScrolledText(self)
        self.a.grid(row=0,column=0)

        self.b=Button(self,text="find out",font=('Times New Roman',20),fg='blue',bg='black',command=self.item)
        self.b.grid(row=0,column=1)

        self.c=Spinbox(self,from_=1,to=100)
        self.c.grid(row=0,column=2)

    def item(self):
        messagebox.showinfo(self,str(self.a.get(0.1,END))+str(self.c.get()))


A=area()
A.mainloop()


