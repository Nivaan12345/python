from tkinter import *
from tkinter import askopenfilename,asksaveasfilename

w=Tk()
w.title("Codingal's text editor")
w.geometry("600x500")
w.rowconfigure(0,minsize=800,weight=1)
w.columnconfigure(1,minsize=800,weight=1)

def openfile():
    filepath=askopenfilename(
        filetypes=[("Text files","*txt"),("All files","*.*")]
    )
    if not filepath:
        return
#INCOMPLETE