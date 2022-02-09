from cProfile import label
from cgitb import text
from tkinter import *
from tkinter.ttk import Combobox

class combo(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("combo box")
        self.geometry("500x300")

        self.cm=Combobox(self)
        self.cm.grid(row=0,column=0)
        self.cm['values']=['web developer','web designer','automation tester','manual tester']

        self.b=Button(self,text="select role",command=self.display)
        self.b.grid(row=1,column=0)

        self.l=Label(self,text="user has choosen")
        self.l.grid(row=2,column=0)

    def display(self):
        a=self.cm.get()
        self.l.config(text=a+" has choosen")

c=combo()
c.mainloop()