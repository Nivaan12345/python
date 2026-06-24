from tkinter import *

w=Tk()
w.title("Length Calculator app")
w.geometry("500x500")

lbl1=Label(text="Enter your length in inches",bg="#1A17D9",fg="white")
ent1=Entry()
def display():
    inch=int(ent1.get())
    cm=inch*2.54
    msg=(f"{inch} inches are {round(cm,2)} centimeters \n")
    txtbx.insert(END,msg)
txtbx=Text(bg="#118C5B",fg="black")
btn=Button(text="Calculate the length in centimeters",command=display,bg="red",fg="yellow")

lbl1.place(x=20,y=20)
ent1.place(x=265,y=20)
btn.place(x=130,y=210)
txtbx.place(x=0,y=250)
w.mainloop()
#end