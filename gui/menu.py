from importlib.resources import contents
from msilib.schema import File
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.scrolledtext import ScrolledText


class demo(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("menu bar")
        self.geometry("500x300")

        self.bar=Menu(self)

        self.m1=Menu(self.bar,tearoff=0)

        self.m1.add_command(label="open",command=self.opening)

        self.m1.add_command(label="save",command=self.saving)

        self.m1.add_command(label="exit",command=self.finish)

        self.bar.add_cascade(label="File",menu=self.m1)

        self.config(menu=self.bar)

        self.a=ScrolledText(self)
        self.a.pack(expand=True,fill=BOTH)

    def opening(self):
        messagebox.showinfo("open file","file open process initiated")
        which=askopenfile(mode="r",filetypes=[
        
            ('All Files','*.*'),
            ('Java Files','*.java'),
            ('Python Files','*.py')
            ])
        if which is not None:
            contents=which.read()
            self.a.insert(1.0,contents)
            messagebox.showinfo("open status",which.name+" has opened")

        else:
            messagebox.showinfo("open status","file is invalid")

    def saving(self):
        messagebox.showinfo("save file","file save process initiated")
        types=[
            ('All Files','*.*'),
            ('Java Files','*.java'),
            ('Python Files','*.py')
            ]

        h=asksaveasfile(filetypes=types,defaultextension=types)
        h.write(self.a.get(1.0,END))

        messagebox.showinfo("save file",h.name+" has saved")

    def finish(self):
        self.destroy()
        
M1=demo()
M1.mainloop()


'''from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.scrolledtext import ScrolledText


class Editor(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Sample Editor")
        self.geometry("500x300")
        
        #menu bar
        self.bar=Menu(self)
        #menu allocation
        self.m1=Menu(self.bar,tearoff=0)
        
        self.m1.add_command(label="Open",command=self.openning)
        self.m1.add_command(label="Save",command=self.saving)
        self.m1.add_command(label="Exit",command=self.finish)
        
        self.bar.add_cascade(label="File",menu=self.m1)
        
        self.config(menu=self.bar)
        
        self.area=ScrolledText(self)
        self.area.pack(expand=True,fill=BOTH)
    
    def finish(self):
        self.destroy()
    
    def openning(self):
        messagebox.showinfo("Open File","File Open process initiated")
        which=askopenfile(mode="r",filetypes=[
            ('All Files','*.*'),
            ('Java Files','*.java'),
            ('Python Files','*.py')
            ])
        if which is not None:
            contents=which.read()
            self.area.insert(1.0,contents)
            messagebox.showinfo("Open Status",which.name+" has openned")
        else:
            messagebox.showinfo("Open Status","File is invalid")
        
    def saving(self):
        messagebox.showinfo("Save File","File Save process initiated")
        types=[
            ('All Files','*.*'),
            ('Java Files','*.java'),
            ('Python Files','*.py')
            ]
        hai=asksaveasfile(filetypes=types,defaultextension=types)
        
        hai.write(self.area.get(1.0,END))
        
        messagebox.showinfo("Save Status",hai.name+" file has saved")

ed=Editor()
ed.mainloop()'''