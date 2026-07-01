from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Interest calculator app")
window.geometry("800x600")

label_principal=Label(window,text="Principal ($)")
label_rate=Label(window,text="Rate (%)")
label_time=Label(window,text="Time (y)")
label_simple=Label(window,text="Simple interest")
label_compound=Label(window,text="Compound interest")

label_principal.place(relx=0.2,y=50)
label_rate.place(relx=0.4,y=50)
label_time.place(relx=0.6,y=50)
label_simple.place(relx=0.4,y=125)
label_compound.place(relx=0.4,y=175)

entry_principal=Entry()
entry_rate=Entry()
entry_time=Entry()

entry_principal.place(relx=0.2,y=75)
entry_rate.place(relx=0.4,y=75)
entry_time.place(relx=0.6,y=75)

text_simple=Text(window)
text_compound=Text(window)

text_simple.place(y=150,width=800,height=25)
text_compound.place(y=200,width=800,height=25)


def calc():
    try:
        p=float(entry_principal.get())
        r=float(entry_rate.get())
        t=float(entry_time.get())
    except:
        text_simple.delete("1.0",END)
        text_compound.delete("1.0",END)
        messagebox.showerror("Error","Invalid input")
        return

    if p<0 or r<0 or t<0:
        text_simple.delete("1.0",END)
        text_compound.delete("1.0",END)
        messagebox.showerror("Error","Invalid input")
    else:
        simple=f"${(p*r*t)/100:.2f}"
        compound=f"${(p*((1+r/100))**t)-p:.2f}"

        text_simple.delete("1.0",END)
        text_compound.delete("1.0",END)

        text_simple.insert(END,simple)
        text_compound.insert(END,compound)

button=Button(window,text="Calculate",command=calc)
button.place(relx=0.4,y=100)

window.mainloop()