from tkinter import *
import datetime
w=Tk()
w.title("Age Calculator")
w.geometry("400x400")

lbl1=Label(text="Enter the year you were born in ",bg="#07B3FD",fg="white",width=30)
ent1=Entry()

def display():
    year=int(ent1.get())
    x=datetime.date.today().year
    y=x-year
    mess=(f"Hello! \n I have found out you are {y} years old")
    txtbx.insert(END,mess)
txtbx=Text(bg="#118C5B",fg="black")
btn=Button(text="Calculate the year",command=display,bg="red")

lbl1.place(x=20,y=20)
ent1.place(x=265,y=20)
btn.place(x=130,y=210)
txtbx.place(x=0,y=250)

w.mainloop()