from tkinter import *
from tkinter import messagebox

class item(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("demo item")
        self.geometry("500x300")

        self.a1=BooleanVar()
        self.a1.set(False)
        self.a2=BooleanVar()
        self.a2.set(False)
        self.a3=BooleanVar()
        self.a3.set(False)

        self.b1=Checkbutton(self,variable=self.a1,text="cooker")
        self.b1.grid(row=0,column=0)

        self.b2=Checkbutton(self,variable=self.a2,text="washing machine")
        self.b2.grid(row=1,column=0)

        self.b3=Checkbutton(self,variable=self.a3,text="fridge")
        self.b3.grid(row=2,column=0)

        self.c=Button(self,text="order",command=self.display)
        self.c.grid(row=3,column=0)

        self.radiovar=StringVar()
        self.radiovar.set("")

        self.r1=Radiobutton(self,variable=self.radiovar,value="card",text="card payment",command=self.display1)
        self.r1.grid(row=4,column=1)

        self.r2=Radiobutton(self,variable=self.radiovar,value="cash",text="cash payment",command=self.display1)
        self.r2.grid(row=5,column=1)

        self.r3=Radiobutton(self,variable=self.radiovar,value="upi",text="upi payment",command=self.display1)
        self.r3.grid(row=6,column=1)

    def display(self):
        messagebox.showinfo(self,"you placed "+format(self.a1.get())+" "+format(self.a2.get())+" "+format(self.a3.get()))

    def display1(self):
        messagebox.showinfo("my order mode",str(self.radiovar.get()))


de=item()
de.mainloop()


