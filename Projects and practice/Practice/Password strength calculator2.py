from tkinter import *
w=Tk()
w.title("Password Strength Calculator")
w.geometry("300x300")

lbl1=Label(text="Enter your password",bg="light grey")
ent1=Entry()
def Calc():
    pas=ent1.get()