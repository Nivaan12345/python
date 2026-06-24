from tkinter import *
w=Tk()
w.title("Password Strength Calculator")
w.geometry("300x300")

lbl1=Label(text="Enter your password",bg="light grey")
ent1=Entry()

def Calc():
    top=Toplevel()
    top.title("Calculator")
    top.geometry("300x300")
    txtbx=Text(top)
    pas=ent1.get()
    check=len(pas)
    if check<=5:
        res="Weak"
        color="red"
    elif check>6 and check<8:
        res="Medium"
        color="yellow"
    elif check>9 and check<12:
        res="Strong"
        color="light green"
    else:
        res="Very Strong"
        color="dark green"
    mess=(f"Your password is: {res}")
    txtbx.insert(END,mess)
    lbl2=Label(top,text="  ",bg=(color))
    txtbx.place(y=150)
    lbl2.pack()
    top.mainloop()

btn=Button(text="calculate",command=Calc,bg="light grey")

lbl1.place(x=20,y=20)
ent1.place(x=150,y=20)
btn.place(x=130,y=110)

w.mainloop()