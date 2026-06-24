from tkinter import *

window=Tk()
window.title("Length converter app")
window.geometry("400x400")

label=Label(text="Enter length in inchies to convert")
entry=Entry()
textbox=Text(fg="black")

def convert():
    length=entry.get()
    try:
        length=float(length)
        cm=length*2.54
        textbox.insert(END,f"{cm} cm")
    except:
        textbox.insert(END,"Invalid input")

button=Button(text="Convert",command=convert)

label.place(x=100,y=20)
entry.place(x=100,y=50)
button.place(x=100,y=80)
textbox.place(y=120)

window.mainloop()