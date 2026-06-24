import random
from tkinter import *

w=Tk()
w.title("Rock paper scissors")
w.geometry("400x400")

lbl1=Label(text="Let us start playing the game\nClick your action when you are ready",bg="#0AB0FC",fg="#000000")
x=["rock","paper","scissor"]
bot_point=0
player_point=0
bot_point_display=Label(text=str(bot_point),bg="grey")
player_point_display=Label(text=str(player_point),bg="grey")
def rock():
    bot=random.choice(x)
    if bot=="rock":
        mess="It's a tie, we both picked rock\n"
    elif bot=="paper":
        mess="Yay I got a point because I picked paper!\n"
        bot_point+=1
    else:
        mess="You won a point because I picked scissor\n"
        player_point+=1
    txtbx.insert(END,mess)

def paper():
    bot=random.choice(x)
    if bot=="paper":
        mess="It's a tie, we both picked paper\n"
    elif bot=="scissor":
        mess="Yay I got a point because I picked scissor\n!"
        bot_point+=1
    else:
        mess="You won a point because I picked rock\n"
        player_point+=1
    txtbx.insert(END,mess)

def scissor():
    bot=random.choice(x)
    if bot=="scissor":
        mess="It's a tie, we both picked scissor\n"
    elif bot=="rock":
        mess="Yay I got a point because I picked rock!\n"
        bot_point+=1
    else:
        mess="You won a point because I picked paper\n"
        player_point+=1
    txtbx.insert(END,mess)
txtbx=Text()
btnr=Button(text="Rock",bg="light grey",command=rock)
btns=Button(text="Scissor",bg="light grey",command=scissor)
btnp=Button(text="Paper",bg="light grey",command=paper)

lbl1.place(y=20)
bot_point_display.place(x=20,y=70)
player_point_display.place(x=265,y=70)
btnp.place(x=50,y=100)
btnr.place(x=300,y=100)
btns.place(x=125,y=100)
txtbx.place(y=250)

w.mainloop()