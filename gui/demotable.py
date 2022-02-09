from tkinter import *

class table(Tk):
    def __init__(self):
        Tk. __init__(self)

        self.title("new table")
        self.geometry("500x300")

        self.t1=Entry(self)
        self.t1.insert(END,"org name")
        self.t1.grid(row=0,column=0)

        self.t2=Entry(self)
        self.t2.insert(END,"org type")
        self.t2.grid(row=0,column=1)

        self.t3=Entry(self)
        self.t3.insert(END,"org location")
        self.t3.grid(row=0,column=2)

        self.t4=Entry(self)
        self.t4.insert(END,"org apps")
        self.t4.grid(row=0,column=3)

        self.t5=Entry(self)
        self.t5.insert(END,"wipro")
        self.t5.grid(row=1,column=0)

        self.t6=Entry(self)
        self.t6.insert(END,"service")
        self.t6.grid(row=1,column=1)

        self.t7=Entry(self)
        self.t7.insert(END,"chennai")
        self.t7.grid(row=1,column=2)

        self.t8=Entry(self)
        self.t8.insert(END,"passport verify")
        self.t8.grid(row=1,column=3)

        self.dict={
            "name":["tcs","cts","wipro","infosys"],
            "type":["service","product","BPO","product"],
            "location":["chennai","bangalore","chennai","hyderabad"],
            "apps":["icic","irctc","axisbank","train ticket"]
        }

        col=0
        for x in self.dict.keys():
            row1=2
            for y in self.dict[x]:
                self.t9=Entry(self)
                self.t9.insert(END,y)
                self.t9.grid(row=row1,column=col)
                row1+=1
            col+=1

td=table()
td.mainloop()