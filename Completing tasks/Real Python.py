# #Temperature Converter

import tkinter as tk
window=tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False,height=False)

frm_entry=tk.Frame(master=window)
ent_temperature=tk.Entry(master=frm_entry,width=10)
lbl_temp=tk.Label(master=frm_entry,text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0,column=0,sticky="e")
lbl_temp.grid(row=0,column=1,sticky="W")

btn_convert=tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}"
)
lbl_result=tk.Label(master=window,text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0,column=0,padx=10)
btn_convert.grid(row=0,column=1,padx=10)
lbl_result.grid(row=0,column=2,padx=10)

window.mainloop()

import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit=ent_temperature.get()
    celsius=(5 / 9)*(float(fahrenheit)-32)
    lbl_result["text"]=f"{round(celsius, 2)}\N{DEGREE CELSIUS}"

btn_convert=tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    #command=fahrenheit_to_celsius
)


#Text Editor

import tkinter as tk

window=tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

txt_edit=tk.Text(window)
frm_buttons=tk.Frame(window,relief=tk.RAISED,bd=2)
btn_open=tk.Button(frm_buttons,text="Open")
btn_save=tk.Button(frm_buttons,text="Save As...")
 
window.rowconfigure(0,minsize=800,weight=1)
window.rowconfigure(1,minsize=800,weight=1)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

import tkinter as tk

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
    
import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_file():
    """Open a file for editing."""
    filepath=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0",tk.END)
    with open(filepath,mode="r",encoding="utf-8") as input_file:
        text=input_file.readr()
        txt_edit.inserrt(tk.END,text)
    window.title(f"Simple Text Editor-{filepath}")
    
window=tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

txt_edit=tk.Text(window)
frm_buttons=tk.Frame(window,relief=tk.RAISED,bd=2)
btn_open=tk.Button(frm_buttons,text="Open",command=open_file)
btn_save=tk.Button(frm_buttons,text="Save As...")

def save_file():
    """Save the current file as a new file."""
    filepath=asksavesfilename(
        defaultextenion=".txt",
        filetypes=[("Text Files","*.txt"),("All Files","*.*")],
    )
    if not filepath:
        return
    with open(filepath,mode="w",encoding="utf-8") as ouput_file:
        text=txt_edit.get("1.0",tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor-{filepath}")

import tkinter as tk
from tkinter.filedialog import askopenfilename,asksavesfilename

window=tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

txt_edit=tk.Text(window)
frm_buttons=tk.Frame(window,relief=tk.RAISED,bd=2)
btn_open=tk.Button(frm_buttons,text="Open",command=open_file)
btn_save=tk.Button(frm_buttons,text="Save As...",command=save_file)

btn_open.grid(row=0,column=0,sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

