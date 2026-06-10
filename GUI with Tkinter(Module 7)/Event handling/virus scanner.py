from tkinter import *
from tkinter import messagebox

w=Tk()
w.title("Virus scanner")
w.geometry("500x500")

def msg():
    messagebox.showwarning("Virus!","Virus is found")

btn=Button(text="Scan for viruses",command=msg)
btn.pack()
w.mainloop()