#from pymysql import*
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

class student(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("student ")
        self.geometry("700x450")
        self.configure(background="black")
        self.resizable(False,False)

        self.Style = font=('Times New Roman',14)

        self.h=Label(self,text="Student details",font=self.Style,fg="blue",bg="white")
        #self.h.configure(justify=CENTER)
        self.h.grid(row=0,column=1)

        self.l1=Label(self,text="Student name",font=self.Style,fg="blue",bg="white")
        self.l1.grid(row=1,column=0)
        
        self.l2=Label(self,text="Student rollno",font=self.Style,fg="blue",bg="white")
        self.l2.grid(row=2,column=0)

        self.l3=Label(self,text="Native place",font=self.Style,fg="blue",bg="white")
        self.l3.grid(row=3,column=0)

        self.l4=Label(self,text="Course",font=self.Style,fg="blue",bg="white")
        self.l4.grid(row=4,column=0)

        self.l5=Label(self,text="Percentage",font=self.Style,fg="blue",bg="white")
        self.l5.grid(row=5,column=0)

        self.e=Entry(self,font=self.Style,fg="blue",bg="white")
        self.e.grid(row=1,column=1)

        self.cm1=Combobox(self,font=self.Style,values=("101","102","103","104","105","106","107","108","109","110"))
        self.cm1.grid(row=2,column=1)

        self.e1=Entry(self,font=self.Style,fg="blue",bg="white")
        self.e1.grid(row=3,column=1)

        self.cm2=Combobox(self,font=self.Style,values=("CSE","EEE","IT","ECE","MECH"))
        self.cm2.grid(row=4,column=1)

        self.e2=Entry(self,font=self.Style,fg="blue",bg="white")
        self.e2.grid(row=5,column=1)

        self.b1=Button(self,text="submit",fg="blue",bg="black",font=self.Style).place(x=150,y=300)

        self.b2=Button(self,text="cancel",fg="blue",bg="black",font=self.Style).place(x=150,y=400)

        '''def submit(self):
            messagebox.showinfo("submit","student yet to be added")

            c=connect(host="localhost",user="root",password="",database="aa")

            per=float(str(self.e2.get()))'''


st=student()
st.mainloop()


            



        
        




