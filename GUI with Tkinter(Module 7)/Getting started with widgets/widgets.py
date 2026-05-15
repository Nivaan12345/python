from tkinter import *
from datetime import date

w=Tk()
w.title('Getting started with widgets')
w.geometry("400x300")

lbl=Label(text="Hey there!",fg="White", bg="#1C5887",height=1, width=300)
name_lbl=Label(text="full Name", bg="#0ED62C")
name_entry=Entry()

def display():
    nm=name_entry.get()
    global mes
    mes="Welcome to the Application!\n todays date is:"
    gre="Hello "+nm+"\n"

    txt_bx.insert(END,gre)
    txt_bx.insert(END,mes)
    txt_bx.insert(END,date.today())

txt_bx=Text(height=3)

btn=Button(text="Begin",command=display,height=1,bg="#F7123C",fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
txt_bx.pack()

w.mainloop()
#end