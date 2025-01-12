#Modules
import tkinter as tk
from tkinter import messagebox
import math
import re

#For The Windows
root = tk.Tk()
root.geometry('400x600')
root.resizable(False, False)
root.iconbitmap("../media/ico/icon.ico")
root.title("Simple Python Calculator")
root.config(bg="#f5f5f5")

#Defining Functions for the buttons and entry
def clicked_buttons(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def prevent_key(event):
        pattern= "[0-9+\-*/().π^]"
        if not re.match(pattern, event.char):
            return "break" 

def calculate():  
    calc=display.get()
    calc=calc.replace("×", "*")
    calc=calc.replace("÷", "/")
    calc=calc.replace("−", "-")
    calc=calc.replace("π", str(math.pi))
    calc=calc.replace("^", "**")
    if "√" in calc:
        calc=calc.replace("√", "math.sqrt(")
        calc= calc + ")"
    if "0/0" in calc:
        messagebox.showinfo("Undefined", "The Answer is Undifined!")
        display.delete(0, tk.END)
        return
    try:      
        ans=eval(calc)
        display.delete(0, tk.END)
        display.insert(tk.END, ans)
    except:
        messagebox.showwarning("Invalid", "Invalid Mathematical Expression!")
        display.delete(0, tk.END)

#Entry
display = tk.Entry(root, width=400, font=("Open Sans ExtraBold", 50), fg="#333333", bd=0, highlightthickness=0)
display.place(width=400, height=200)
display.bind("<KeyPress>", prevent_key)

#Buttons
op_plus=tk.Button(root, text="+", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("+"))
op_plus.place(x=24, y=223, width=60, height=60)
op_minus=tk.Button(root, text="−", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("-"))
op_minus.place(x=97, y=223, width=60, height=60)
op_multiplication=tk.Button(root, text="×", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("×"))
op_multiplication.place(x=170, y=223, width=60, height=60)
op_divison=tk.Button(root, text="÷", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("÷"))
op_divison.place(x=243, y=223, width=60, height=60)
clear=tk.Button(root, text="C", font=("Open Sans ExtraBold", 30), bg="#3ac2aa", fg="#2c2c2c", activebackground="#36b39e", activeforeground="#383838", bd=0, highlightthickness=0, command=clear)
clear.place(x=316, y=223, width=60, height=60)
power=tk.Button(root, text="^", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("^"))
power.place(x=24, y=297, width=60, height=60)
num9=tk.Button(root, text="9", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("9"))
num9.place(x=97, y=297, width=60, height=60)
num8=tk.Button(root, text="8", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("8"))
num8.place(x=170, y=297, width=60, height=60)
num7=tk.Button(root, text="7", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("7"))
num7.place(x=243, y=297, width=60, height=60)
bracket_fright=tk.Button(root, text="(", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("("))
bracket_fright.place(x=316, y=297, width=60, height=60)
sq_root=tk.Button(root, text="√", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("√"))
sq_root.place(x=24, y=371, width=60, height=60)
num6=tk.Button(root, text="6", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("6"))
num6.place(x=97, y=371, width=60, height=60)
num5=tk.Button(root, text="5", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("5"))
num5.place(x=170, y=371, width=60, height=60)
num4=tk.Button(root, text="4", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("4"))
num4.place(x=243, y=371, width=60, height=60)
bracket_fleft=tk.Button(root, text=")", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons(")"))
bracket_fleft.place(x=316, y=371, width=60, height=60)
pi=tk.Button(root, text="π", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("π"))
pi.place(x=24, y=445, width=60, height=60)
num3=tk.Button(root, text="3", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("3"))
num3.place(x=97, y=445, width=60, height=60)
num2=tk.Button(root, text="2", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("2"))
num2.place(x=170, y=445, width=60, height=60)
num1=tk.Button(root, text="1", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("1"))
num1.place(x=243, y=445, width=60, height=60)
equal=tk.Button(root, text="=", font=("Open Sans ExtraBold", 30), bg="#3ac2aa", fg="#2c2c2c", activebackground="#36b39e", activeforeground="#383838", bd=0, highlightthickness=0, command=calculate)
equal.place(x=316, y=445, width=60, height=134)
point=tk.Button(root, text=".", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("."))
point.place(x=24, y=519, width=60, height=60)
num0=tk.Button(root, text="0", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0, command=lambda: clicked_buttons("0"))
num0.place(x=97, y=519, width=206, height=60)

root.mainloop()