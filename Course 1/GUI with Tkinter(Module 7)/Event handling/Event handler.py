from tkinter import *
w=Tk()

w.title("Event handler")
w.geometry("500x500")

def event_keypress(event):
    print(event.char)
w.bind("<Key>",event_keypress)

def event_click(event):
    print("This button has been clicked!")
btn=Button(text="Click me!")
btn.pack()

btn.bind("<Button-1>",event_click)
w.mainloop()