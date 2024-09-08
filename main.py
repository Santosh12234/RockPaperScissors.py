#Rock Paper Scissors
from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x500")
root.config(bg = "pink")
root.resizable(False,False)

def answer(n):
    choices = ["Rock","Paper","Scissors"]
    m = random.choice(choices)
    if n == "Rock":
        label_1.config(text="Your choice: Rock")
    elif n == "Paper":
        label_1.config(text="Your choice: Paper")
    elif n == "Scissors":
        label_1.config(text="Your choice: Scissors")
    label_2.config(text="and")
    label_3.config(text="Computer choice: "+m)
    check(n,m)
def check(n,m):
    if m == n:
        label_5.config(text="Draw")
    elif m=="Rock" and n=="Scissors":
        label_5.config(text="Computer win's")
    elif m=="Rock" and n=="Paper":
        label_5.config(text="Congratulations you win's")
    elif m=="Paper" and n=="Scissors":
        label_5.config(text="Congratulations you win's")
    elif m=="Paper" and n=="Rock":
        label_5.config(text="Computer win's")
    elif m == "Scissors" and n == "Rock":
        label_5.config(text="Congratulations you win's")
    elif m == "Scissors" and n == "Paper":
        label_5.config(text="Computer win's")


button_1 = Button(root,bg="red",fg="black",text="Rock",font=13,width=14,borderwidth=1,command=lambda:answer("Rock"))
button_1.place(x=19,y=350)

button_2 = Button(root,bg="red",fg="black",text="Paper",font=13,width=14,borderwidth=1,command=lambda:answer("Paper"))
button_2.place(x=184,y=350)

button_3 = Button(root,bg="red",fg="black",text="Scissors",font=13,width=14,borderwidth=1,command=lambda:answer("Scissors"))
button_3.place(x=349,y=350)

button_4 = Button(root,bg="red",fg="black",text="Exit",font=13,width=14,borderwidth=1,command=lambda:exit(0))
button_4.place(x=514,y=350)

label_1 = Label(root,width=26,height=4,bg="pink",font=("bold",15))
label_1.place(x=20,y=100)

label_2 = Label(root,width=5,height=4,bg="pink",font=("bold",15))
label_2.place(x=305,y=100)

label_3 = Label(root,width=25,height=4,bg="pink",font=("bold",15))
label_3.place(x=380,y=100)

label_4 = Label(root,width=61,height=2,bg="blue",text="Rock-Paper-Scissors",font=("bold",15))
label_4.place(x=10,y=10)

label_5 = Label(root,width=40,height=4,bg="pink",font=("bold",15))
label_5.place(x=125,y=200)

label_6 = Label(root,width=40,height=4,bg="pink",font=("bold",10),text="NOTE:The rules are straightforward:\t\t   "
"\n1. Rock crushes Scissors.\t\t\t"
"\n2. Scissors cuts Paper.\t\t              "
"\n3. Paper covers Rock.                                      ",fg="red")
label_6.place(x=5,y=425)

root.mainloop()