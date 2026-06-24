from tkinter import *
w=Tk()
w.title('Find the product!')
w.geometry("500x500")
plbl=Label(text="Enter both the numbers you want to multiply", bg="#D6180E")
entp1=Entry()
entp2=Entry()

def display():
    p1=int(entp1.get())
    p2=int(entp2.get())
    p3=p1*p2
    mes="Welcome to Find the product\n"
    pro=f"The number {p1} multiplied by {p2} gives you {p3}\n"


    txt.insert(END,mes)
    txt.insert(END,pro)

txt=Text(height=2)
btn=Button(text="Calculate",command=display,height=1,bg="#F7123C",fg="white")

plbl.pack()
entp1.pack()
entp2.pack()
btn.pack()
txt.pack()

w.mainloop()