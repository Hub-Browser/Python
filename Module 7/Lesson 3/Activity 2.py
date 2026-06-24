from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Virus Scanner")
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","Stop! Virus found")

button=Button(text="Scan for virus",command=msg)
button.place(x=40,y=40)

window.mainloop()