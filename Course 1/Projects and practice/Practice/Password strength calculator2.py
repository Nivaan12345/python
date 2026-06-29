from tkinter import *
w=Tk()
w.title("Password Strength Calculator")
w.geometry("500x500")

lbl1=Label(text="Enter your password",bg="light grey")
ent1=Entry(show="*")
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
    sym_upp=False
    for i in pas:
        for j in symbols:
            if i==j:
                if symbol==False:
                    r+=1
                    symbol=True
                    sym_upp=True
                    print("symbol")
        try:
            x=int(i)
            if number==False:
                r+=1
                number=True
                print("Numbers")
        except ValueError:
            if i==i.upper():
                if upper==False:
                    if sym_upp==False:
                        r+=1
                        upper=True
                        print("Upper case")
            elif i==i.lower():
                if lower==False:
                    r+=1
                    lower=True
                    
                    print("Lower case")
    if len(pas)>=8:
        r+=1
        print("length")
    print("\n--------------\n")
    if r<=1:
        res="Weak"
        color="red"
    elif r==2:
        res="Medium"
        color="yellow"
    elif r>2 and r<=4:
        res="Strong"
        color="light green"
    elif r>4:
        res="Super strong"
        color="dark green"
    
    mess=(f"Your password is: {res}")
    txtbx.insert(END,mess)
    lbl2=Label(top,text="        \n       ",bg=(color))
    txtbx.place(y=150)
    lbl2.place(x=150,y=100)
    top.mainloop()

btn=Button(text="calculate",command=Calc,bg="light grey")

lbl1.place(x=20,y=20)
ent1.place(x=150,y=20)
btn.place(x=130,y=110)

w.mainloop()
#end