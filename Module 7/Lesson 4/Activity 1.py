from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Codingal's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
    window.title(f"Codingal's text editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Codingal's text editor - {filepath}")

text_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
button_open = Button(fr_buttons, text="Open", command=open_file)
button_save = Button(fr_buttons, text="Save As", command=save_file)

button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
