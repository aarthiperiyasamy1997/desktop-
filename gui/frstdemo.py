'''from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import messagebox
class demo(Tk):
    def __init__(self):
        Tk. __init__(self)
        self.title("Demo box")
        self.geometry('500x300')

        self.a=BooleanVar(False)
        self.b=BooleanVar(False)
        self.c=BooleanVar(False)

        self.a1=Checkbutton(self,variable=self.a,text='salem')
        self.a1.grid(row=0,column=0)

        self.a2=Checkbutton(self,variable=self.b,text='madurai')
        self.a2.grid(row=0,column=1)

        self.a3=Checkbutton(self,variable=self.c,text='Erode')
        self.a3.grid(row=0,column=2)

    def place(self):
        messagebox.showinfo(self,"display")
de=demo()
de.mainloop()'''

from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import messagebox

class Small(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Small items")
        self.geometry('500x300')

        self.b1=BooleanVar()
        self.b1.set(False)
        self.b2=BooleanVar()
        self.b2.set(False)
        self.b3=BooleanVar()
        self.b3.set(False)

        self.cb1=Checkbutton(self,variable=self.b1,text='Falooda')
        self.cb1.grid(row=0,column=0)

        self.cb2=Checkbutton(self,variable=self.b2,text='CashewShake')
        self.cb2.grid(row=1,column=0)

        self.cb3=Checkbutton(self,variable=self.b3,text='Coke')
        self.cb3.grid(row=2,column=0)

        self.bt=Button(self,text="Order",command=self.place)
        self.bt.grid(row=3,column=0)
    def place(self):
        messagebox.showinfo(self,"You placed ")


sm=Small()
sm.mainloop() 