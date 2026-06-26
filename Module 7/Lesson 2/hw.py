from tkinter import *
from datetime import date

window=Tk()
window.title("Age calculator")
window.geometry("400x300")

l1=Label(window,text="Year")
l1.place(relx=0.2,y=25)
l2=Label(window,text="Month")
l2.place(relx=0.4,y=25)
l3=Label(window,text="Day")
l3.place(relx=0.6,y=25)

entry_year_entry=Entry()
entry_year_entry.place(relx=0.2,y=50,width=50)
entry_month_entry=Entry()
entry_month_entry.place(relx=0.4,y=50,width=50)
entry_day_entry=Entry()
entry_day_entry.place(relx=0.6,y=50,width=50)
text=Text()
text.place(y=150)

def calculate():
    try:
        entry_year=int(entry_year_entry.get())
        entry_month=int(entry_month_entry.get())
        entry_day=int(entry_day_entry.get())
    except:
        text.delete(1.0,END)
        text.insert(END,"Invalid input")
    if entry_day<1 or entry_day>31:
        text.delete(1.0,END)
        text.insert(END,"Invalid input")
    if entry_month==2:
        leap=False
        if (entry_year%400==0) or (entry_year%4==0 and entry_year%100!=0):
            leap=True
        if leap==False and entry_day>28:
            text.delete(1.0,END)
            text.insert(END,"Invalid input")
        elif leap==True and entry_day>29:
            text.delete(1.0,END)
            text.insert(END,"Invalid input")
    if entry_month==4 or entry_month==6 or entry_month==9 or entry_month==11:
        if entry_day>30:
            text.delete(1.0,END)
            text.insert(END,"Invalid input")
    else:
        today=date.today()
        age=today.year-entry_year
        if (today.month<entry_month) or (today.month==entry_month and today.day<entry_day):
            age=age-1
        text.delete(1.0,END)
        text.insert(END,f"Your are {age} years old")

button=Button(window,text="Calculate age",command=calculate)
button.place(relx=0.4,y=100)

text.delete(1.0,END)
window.mainloop()