from tkinter import *
import random

def destroy(arg):
    arg.grid_forget()
def activate():
                rock.configure(state="active")
                paper.configure(state="active")
                scissors.configure(state="active")
def disable():
            rock.configure(state="disabled")
            paper.configure(state="disabled")
            scissors.configure(state="disabled")

def decide(meth, com):
    if meth == "rock":
        if com == "rock":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=0)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=0)
            l.after(2500, lambda: l.configure(text=f"It's a TIE"))
            l.grid(row=4, column=0)
            
        if com == "paper":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=0)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=0)
            l.after(2500, lambda: l.configure(text=f"You LOSE"))
            l.grid(row=4, column=0)
            
        if com == "scissors":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=0)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=0)
            l.after(2500, lambda: l.configure(text=f"You WIN"))
            l.grid(row=4, column=0)

    if meth == "paper":
        if com == "paper":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=1)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=1)
            l.after(2500, lambda: l.configure(text=f"It's a TIE"))
            l.grid(row=4, column=1)
            
        if com == "scissors":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=1)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=1)
            l.after(2500, lambda: l.configure(text=f"You LOSE"))
            l.grid(row=4, column=1)
            
        if com == "rock":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=1)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=1)
            l.after(2500, lambda: l.configure(text=f"You WIN"))
            l.grid(row=4, column=1)

    if meth == "scissors":
        if com == "scissors":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=2)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=2)
            l.after(2500, lambda: l.configure(text=f"It's a TIE"))
            l.grid(row=4, column=2)
            
        if com == "rock":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=2)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=2)
            l.after(2500, lambda: l.configure(text=f"You LOSE"))
            l.grid(row=4, column=2)
            
        if com == "paper":
            l.configure(text=f"Compter chose: {com}", font=("", 20))
            l.grid(row=4, column=2)
            l.after(1500, lambda: l.configure(text=f"You chose: {meth}"))
            l.grid(row=4, column=2)
            l.after(2500, lambda: l.configure(text=f"You WIN"))
            l.grid(row=4, column=2)
        
            

def check(meth):
    choices = ["rock", "paper", "scissors"]
    com = random.choice(choices)
    print(com)
    disable()
    decide(com=com,meth=meth)
    l.after(6000, lambda: destroy(l))
    l.after(6000, activate)


def setup():

    global root, rock, paper, scissors, l
    root = Tk()
    root.geometry("1005x320")
    root.title("Rock | Paper | Scissors")
    root.configure(background="#ff9082", borderwidth=5)

    backgroundcolor = "#912111"
    activebgc="#5c1308"
    rock = Button(root, text="Rock", height="4", width="20", font=("System", 20), background=backgroundcolor, foreground="#cfcfcf", activebackground=activebgc, borderwidth=10,activeforeground="white", command=lambda: check(meth="rock"))
    
    paper = Button(root, text="Paper", height="4", width="20", font=("System", 20) , background=backgroundcolor, foreground="#cfcfcf", activebackground=activebgc, borderwidth=10,activeforeground="white", command=lambda: check(meth="paper"))
    
    scissors = Button(root, text="Scissors", height="4", width="20", font=("System", 20), background=backgroundcolor, foreground="#cfcfcf", activebackground=activebgc, borderwidth=10,activeforeground="white", command=lambda: check(meth="scissors"))


    l = Label(root)


    rock.grid(row=1, column=0, padx=15, sticky="we")
    paper.grid(row=1, column=1, padx=15, sticky="we")
    scissors.grid(row=1, column=2, padx=15, sticky="we")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(1, weight=1)

    root.mainloop()

setup()