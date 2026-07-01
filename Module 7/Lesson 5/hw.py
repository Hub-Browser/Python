from tkinter import *

window=Tk()
window.title("Password strength checker app")
window.geometry("800x600")

label=Label(window,text="Enter password below")
label.place(relx=0.5,y=50,anchor=CENTER)

entry=Entry()
entry.place(relx=0.5,y=75,anchor=CENTER)

text=Text()
text.insert(END,"Password strength: ")
text.config(state="disabled")
text.place(relx=0.5,y=125,anchor=CENTER,height=25)

text.tag_configure("a",foreground="red")
text.tag_configure("b",foreground="yellow")
text.tag_configure("c",foreground="lightgreen")
text.tag_configure("d",foreground="Darkgreen")

def calc():  
    p=str(entry.get())
    l=len(p)
    if " " in p or p=="":
        text.config(state="normal")
        text.delete("1.19", END)
        text.insert(END,"Invalid input")
        text.config(state="disabled")
        return
    else:    
        if l<=5:
            text.config(state="normal")
            text.delete("1.19", END)
            text.insert(END,"Weak","a")
            text.config(state="disabled")

        if l>=6 and l<=8:
            text.config(state="normal")
            text.delete("1.19", END)
            text.insert(END,"Medium","b")
            text.config(state="disabled")
        
        if l>8 and l<=12:
            text.config(state="normal")
            text.delete("1.19", END)
            text.insert(END,"Strong","c")
            text.config(state="disabled")

        if l>12:
            text.config(state="normal")
            text.delete("1.19", END)
            text.insert(END,"Very strong","d")
            text.config(state="disabled")    

button=Button(text="Check password strength",command=calc)
button.place(relx=0.5,y=100,anchor=CENTER)

window.mainloop()

