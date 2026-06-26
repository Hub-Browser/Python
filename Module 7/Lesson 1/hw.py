from tkinter import *

window=Tk()
window.title("Product calculator")
window.geometry("400x300")

label=Label(window,text="Enter the numbers below")
label.pack()

entry1=Entry()
entry2=Entry()
entry1.place(relx=0.3,y=100,width=50)
entry2.place(relx=0.6,y=100,width=50)
text=Text()
text.place(y=200)

def sum():
    try:
        text.delete(1.0,END)
        text.insert(END,int(entry1.get())*int(entry2.get()))
    except:
        text.delete(1.0,END)
        text.insert(END,"Invalid input")

button=Button(window,text="Calculate",command=sum)
button.place(relx=0.4,y=150)

window.mainloop()