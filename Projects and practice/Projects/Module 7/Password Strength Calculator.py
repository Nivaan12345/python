from tkinter import *
w=Tk()
w.title("Password Strength Calculator")
w.geometry("300x300")

lbl1=Label(text="Enter your password",bg="light grey")
ent1=Entry()
def Calc():
    pas=ent1.get()
    check=len(pas)
    if check<=5:
        res="Weak"
        color="red"
    if check>6 and check<8:
        res=""