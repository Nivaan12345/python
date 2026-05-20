from tkinter import *
w=Tk()
w.title('Login app')
w.geometry("400x400")

frame=Frame(master=w,height=200,width=360,bg="#781CF0",bd=2,relief=RAISED)

lbl1=Label(frame,text="Full Name",bg="#3895D3",fg="white",width=12)
lbl2=Label(frame,text="Email Address",bg="#3895D3",fg="white",width=12)
lbl3=Label(frame,text="Password",bg="#3895D3",fg="white",width=12)

name=Entry(frame)
email=Entry(frame)
password=Entry(frame,show="*")

def display():
    nam=name.get()
    greet=(f"hey {nam}")
    mess="\n Congratulations for your new account!"
    txtbx.insert(END,greet)
    txtbx.insert(END,mess)

txtbx=Text(bg="#118C5B",fg="black")
btn=Button(text="Create account",command=display,bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name.place(x=150,y=20)
lbl2.place(x=20,y=80)
email.place(x=150,y=80)
lbl3.place(x=20,y=140)
password.place(x=150,y=140)
btn.place(x=130,y=210)
txtbx.place(x=0,y=250)
 
w.mainloop()