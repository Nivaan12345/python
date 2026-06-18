from tkinter import *
w=Tk()
w.title("Password Strength Calculator")
w.geometry("300x300")

lbl1=Label(text="Enter your password",bg="light grey")
ent1=Entry()
def Calc():
    r=0
    upper=False
    lower=False
    number=False
    symbol=False
    pas=ent1.get()
    for i in pas:
        if i==i.upper():
            if upper==False:
               r+=1
               upper=True
        elif i==i.lower():
            if lower==False:
                r+=1
                lower=True
        elif type(i)==int:
            if number==False:
                r+=1
                number=True