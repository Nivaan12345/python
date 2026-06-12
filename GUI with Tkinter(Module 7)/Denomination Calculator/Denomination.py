from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

w=Tk()
w.title("Denomination Calculator")
w.configure(BG="light blue")
w.geometry("650x400")

upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
image=ImageTk.Photoimage(upload)
label=Label(w,image=image,bg="light blue")
label.place(x=180,y=20)
#INCOMPLETE