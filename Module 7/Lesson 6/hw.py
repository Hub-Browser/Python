from tkinter import *
import random as r

window=Tk()
window.title("Rock paper scissor app")
window.geometry("1280x720")

l1=Label(text="")
l1.place(relx=0.5,y=150,anchor=CENTER)
l2=Label(text="")
l2.place(relx=0.5,y=200,anchor=CENTER)

def rps(u):
    c=r.choice(("r","p","s"))
    if c=="r":
        if u=="r":
            res = "It's a draw!"
        if u=="p":
            res = "You win!"
        if u=="s":
            res = "You lose!"

    if c=="p":
        if u=="r":
            res = "You lose!"
        if u=="p":
            res = "It's a draw!"
        if u=="s":
            res = "You win!"

    if c=="s":
        if u=="r":
            res = "You win!"
        if u=="p":
            res = "You lose!"
        if u=="s":
            res = "It's a draw!"
    
    names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    l1.config(text=f"Computer chooses: {names[c]}",font=("Arial",36))
    l2.config(text=res,font=("Arial",36))
    
button_r=Button(text="Rock",command=lambda: rps("r"),font=("Arial",36))
button_p=Button(text="Paper",command=lambda: rps("p"),font=("Arial",36))
button_s=Button(text="Scissors",command=lambda: rps("s"),font=("Arial",36))

button_r.place(relx=0.25,y=50,anchor=CENTER)
button_p.place(relx=0.5,y=50,anchor=CENTER)
button_s.place(relx=0.75,y=50,anchor=CENTER)

window.mainloop()