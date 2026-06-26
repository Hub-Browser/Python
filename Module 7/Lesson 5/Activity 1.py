from tkinter import *

window=Tk()
window.title("Main window")
window.geometry("400x300")

label=Label(window,text="This is the main window")

def topwin():
    top=Toplevel()
    top.title("Top window")
    top.geometry("200x200")
    
    label2=Label(top,text="This is toplevel window")
    label2.pack()
    top.mainloop()

button=Button(window,text="Click here to open another window",command=topwin)

label.pack()
button.pack()

window.mainloop()