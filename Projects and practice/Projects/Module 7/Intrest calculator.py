from tkinter import *
w=Tk()
w.title("Intrest calculator")
w.geometry("400x400")

lbl1=Label(text="Enter the Principle",bg="#31E393",fg="#F54702")
lbl2=Label(text="Enter the Time in years",bg="#31E393",fg="#F54702")
lbl3=Label(text="Enter the Rate in percentage(no symbols)",bg="#31E393",fg="#F54702")
p1=Entry()
r1=Entry()
t1=Entry()
def simple_inrest():
    p=int(p1.get())
    r=((int(r1.get()))/100)
    t=int(t1.get())
    i=p*r*t
    a=p*(1+(r*t))
    mess=(f"The simple intrest is {round(i,2)} \nand the total amount is {round(a,2)}\n")
    txtbx.insert(END,mess)
def compound_intrest():
    p=int(p1.get())
    r=((int(r1.get()))/100)
    t=int(t1.get())
    a=p*((1+r)**t)
    i=a-p
    mess=(f"The compound intrest is {round(i,2)} \nand the total amount is {round(a,2)}\n")
    txtbx.insert(END,mess)
txtbx=Text(bg="#05D0F8")
btn1=Button(text="Simple intrest",command=simple_inrest,bg="#371EDE",fg="#B310A2")
btn2=Button(text="Compound intrest",command=compound_intrest,bg="#371EDE",fg="#B310A2")

lbl1.place(x=20,y=20)
p1.place(x=200,y=20)
lbl2.place(x=20,y=80)
t1.place(x=200,y=80)
lbl3.place(x=20,y=140)
r1.place(x=200,y=140)
btn1.place(x=20,y=200)
btn2.place(x=200,y=200)
txtbx.place(x=0,y=250)

w.mainloop()