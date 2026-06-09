from tkinter import *
w=Tk()
w.title('Use the Calculator!')
w.geometry("500x500")
plbl=Label(text="Enter both the numbers you want to calculate", bg="#900ED6")
entp1=Entry()
entp2=Entry()

def multiply():
    p1=int(entp1.get())
    p2=int(entp2.get())
    p3=p1*p2
    mes="Welcome to Find the product\n"
    pro=f"The number {p1} multiplied by {p2} gives you {p3}\n"
    txt.insert(END,mes)
    txt.insert(END,pro)

def divide():
    p1=int(entp1.get())
    p2=int(entp2.get())
    p3=p1/p2
    mes="Welcome to Find the Quotient\n"
    pro=f"The number {p1} divided by {p2} gives you {p3}\n"
    txt.insert(END,mes)
    txt.insert(END,pro)

def add():
    p1=int(entp1.get())
    p2=int(entp2.get())
    p3=p1+p2
    mes="Welcome to Find the Sum\n"
    pro=f"The number {p1} added to {p2} gives you {p3}\n"
    txt.insert(END,mes)
    txt.insert(END,pro)

def subtract():
    p1=int(entp1.get())
    p2=int(entp2.get())
    p3=p1-p2
    mes="Welcome to Find the DifferencOe\n"
    pro=f"The number {p1} subtracted {p2} gives you {p3}\n"
    txt.insert(END,mes)
    txt.insert(END,pro)

def power():
    p1=int(entp1.get())
    p2=int(entp2.get())
    p3=p1**p2
    mes="Welcome to Find the Exponent\n"
    pro=f"The number {p1} raised to {p2} gives you {p3}\n"
    txt.insert(END,mes)
    txt.insert(END,pro)

txt=Text(height=2)
btn1=Button(text="Multiply",command=multiply,height=1,bg="#F7123C",fg="white")
btn2=Button(text="Divide",command=divide,height=1,bg="#1A12F7",fg="white")
btn3=Button(text="Add",command=add,height=1,bg="#12F738",fg="white")
btn4=Button(text="Subtract",command=subtract,height=1,bg="#A7D330",fg="white")
btn5=Button(text="Power",command=power,height=1,bg="#F78812",fg="white")

plbl.pack()
entp1.pack()
entp2.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
txt.pack()
 
w.mainloop()