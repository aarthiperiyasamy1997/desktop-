from msilib.schema import ComboBox
from sqlite3 import connect
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox
from pymysql import *

con = connect(host='localhost',database='studentapp',user='root',password='')
cur=con.cursor()


class stapp(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("student details")
        self.geometry("1000x500")
        #self.configure(background="black")
        self.resizable(False,False)
        self.style=font=("times",18)

        self.tit=Label(self,text="BIO DATA",font=self.style)#.place(x=180,y=10)
        self.tit.grid(row=0,column=0)

        self.fst_name=Label(self,text="NAME",font=self.style)
        self.fst_name.grid(row=1,column=0)
        self.fst_name_txt=Entry(self,font=self.style)
        self.fst_name_txt.grid(row=1,column=1)

        self.stu_rollno=Label(self,text="ROLLNO",font=self.style)
        self.stu_rollno.grid(row=2,column=0)
        self.stu_rollno_txt=Entry(self,font=self.style)
        self.stu_rollno_txt.grid(row=2,column=1)

        self.n_place=Label(self,text="NATIVE PLACE",font=self.style)
        self.n_place.grid(row=3,column=0)
        self.n_place_txt=Entry(self,font=self.style)
        self.n_place_txt.grid(row=3,column=1)

        self.stu_course=Label(self,text="COURSE",font=self.style)
        self.stu_course.grid(row=4,column=0)
        self.stu_course_cmb=Combobox(self,font=self.style,values=("CSE","EEE","ECE","IT","MECH"))
        self.stu_course_cmb.grid(row=4,column=1)

        self.stu_per=Label(self,text="PERCENTAGE",font=self.style)
        self.stu_per.grid(row=5,column=0)
        self.stu_per_txt=Entry(self,font=self.style)
        self.stu_per_txt.grid(row=5,column=1)

        self.but=Button(self,text="submit",font=self.style,fg="white",bg="blue",command=self.submit).place(x=110,y=230)
        self.but=Button(self,text="cancel",font=self.style,fg="white",bg="blue",command=self.clear).place(x=200,y=230)
        self.but=Button(self,text="update",font=self.style,fg="white",bg="blue",command=self.up).place(x=300,y=230)
        self.but=Button(self,text="")
    def submit(self):
        messagebox.showinfo("submited","details can be submited")
 
        qry="""insert into student(name,rollno,place,course,percentage) values('%s',%d,'%s','%s',%f)"""\
              %(self.fst_name_txt.get(),int(self.stu_rollno_txt.get()),self.n_place_txt.get(),self.stu_course_cmb.get(),float(self.stu_per_txt.get()))
        
        ack=cur.execute(qry)
        con.autocommit(True)

        if ack!=0:
            messagebox.showinfo("info","can be inserted")
            self.clear()
        else:
            messagebox.showinfo("info","can't inserted")

    def clear(self):
        self.fst_name_txt.delete(0,END)
        self.stu_rollno_txt.delete(0,END)
        self.n_place_txt.delete(0,END)
        self.stu_course_cmb.delete(0,END)
        self.stu_per_txt.delete(0,END)

    def up(self):
        con.autocommit(True)
        qry="""update student set name=%s rollno=%d place=%s course=%s percentage=%f"""\
            %(self.fst_name_txt.get(),int(self.stu_rollno_txt.get()),self.n_place_txt.get(),self.stu_course_cmb.get(),float(self.stu_per_txt.get()))
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("info","updated")

        else:
            messagebox.showinfo("info","can't updated")
        
st=stapp()
st.mainloop()