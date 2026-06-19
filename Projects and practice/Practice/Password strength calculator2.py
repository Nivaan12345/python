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
    r=0
    symbols="!@#$%^&*()<>?:}[';/.,-|_+"
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
        elif i in symbols:
            if symbol==False:
                r+=1
                symbol=True
    if len(i)>=8:
        r+=1
    
    if r<=1:
        res="Weak"
        color="red"
    elif r==2:
        res="Medium"
        color="yellow"
    elif r>2 and r<=4:
        res="Strong"
        color="light green"
    else:
        res="Super strong"
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