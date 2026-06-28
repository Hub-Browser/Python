import tkinter as tk
from tkinter import ttk,messagebox

class RestaurantOrderManagement:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Restaurant Management App")

        self.menu_items={
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":3,
            "PIZZA MEAL":4,
            "CHEESE BURGER":2.5,
            "DRINKS":1,
        }
        self.exchange_rate=82
        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        ttk.Label(frame,text="Restaurant Order Management",font=("Arial",20,"bold")).grid(row=0,columnspan=2,padx=10,pady=10)
        self.menu_labels={}
        self.menu_quantities={}

        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} (${price}):",font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5,sticky="w")

            self.menu_labels[item]=label

            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)

        self.currency_var=tk.StringVar()
        dropdown_row=len(self.menu_items)+1

        ttk.Label(frame,text="Currency",font=("Arial",12)).grid(row=dropdown_row,column=0,padx=10,pady=5,sticky="w")

        currency_dropdown=ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,values=("USD","INR"))
        currency_dropdown.grid(row=dropdown_row,column=1,padx=10,pady=5)
        currency_dropdown.current(0)

        self.currency_var.trace_add("write",self.update_menu_prices)

        order_button=ttk.Button(frame,text="Place order",command=self.place_order)
        order_button.grid(row=dropdown_row+1,columnspan=2,padx=10,pady=10)
    
    def setup_background(self,root):
        bg_width,bg_height=800,600
        canvas=tk.Canvas(root,width=bg_width,height=bg_height,highlightthickness=0)
        canvas.grid(row=0,column=0,sticky="nsew")

        try:
            original_image=tk.PhotoImage(file=r"/Users/apple/Desktop/Python/Module 7/Lesson 6/images.jpeg")
            sub_x=max(1,original_image.width()//bg_width)
            sub_y=max(1,original_image.height()//bg_height)

            background_image=original_image.subsample(sub_x,sub_y)
            canvas.create_image(0,0,anchor=tk.NW,image=background_image)
            canvas_image=background_image
        except tk.TclError:
            canvas.configure(bg="#ffffff")

        