import tkinter as tk

root = tk.Tk()
root.geometry('400x600')
root.resizable(False, False)
root.iconbitmap("../media/ico/icon.ico")
root.title("Simple Python Calculator")
root.config(bg="#f5f5f5")

#Entry
display = tk.Entry(root, width=400, font=("Open Sans ExtraBold", 50), fg="#333333", bd=0, highlightthickness=0)
display.place(width=400, height=200)

#Buttons
op_plus=tk.Button(root, text="+", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
op_plus.place(x=24, y=230, width=60, height=60)
op_minus=tk.Button(root, text="-", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
op_minus.place(x=97, y=230, width=60, height=60)
op_multiplication=tk.Button(root, text="×", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
op_multiplication.place(x=170, y=230, width=60, height=60)
op_divison=tk.Button(root, text="÷", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
op_divison.place(x=243, y=230, width=60, height=60)
clear=tk.Button(root, text="C", font=("Open Sans ExtraBold", 30), bg="#3ac2aa", fg="#2c2c2c", activebackground="#36b39e", activeforeground="#383838", bd=0, highlightthickness=0)
clear.place(x=316, y=230, width=60, height=60)
power=tk.Button(root, text="^", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
power.place(x=24, y=304, width=60, height=60)
num9=tk.Button(root, text="9", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num9.place(x=97, y=304, width=60, height=60)
num8=tk.Button(root, text="8", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num8.place(x=170, y=304, width=60, height=60)
num7=tk.Button(root, text="7", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num7.place(x=243, y=304, width=60, height=60)
bracket_fright=tk.Button(root, text="(", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
bracket_fright.place(x=316, y=304, width=60, height=60)
sq_root=tk.Button(root, text="√", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
sq_root.place(x=24, y=378, width=60, height=60)
num6=tk.Button(root, text="6", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num6.place(x=97, y=378, width=60, height=60)
num5=tk.Button(root, text="5", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num5.place(x=170, y=378, width=60, height=60)
num4=tk.Button(root, text="4", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num4.place(x=243, y=378, width=60, height=60)
bracket_fleft=tk.Button(root, text=")", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
bracket_fleft.place(x=316, y=378, width=60, height=60)
pi=tk.Button(root, text="π", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
pi.place(x=24, y=452, width=60, height=60)
num3=tk.Button(root, text="3", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num3.place(x=97, y=452, width=60, height=60)
num2=tk.Button(root, text="2", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num2.place(x=170, y=452, width=60, height=60)
num1=tk.Button(root, text="1", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num1.place(x=243, y=452, width=60, height=60)
equal=tk.Button(root, text="=", font=("Open Sans ExtraBold", 30), bg="#3ac2aa", fg="#2c2c2c", activebackground="#36b39e", activeforeground="#383838", bd=0, highlightthickness=0)
equal.place(x=316, y=452, width=60, height=134)
point=tk.Button(root, text=".", font=("Open Sans ExtraBold", 30), bg="#8fbc8f", fg="#2c2c2c", activebackground="#91b991", activeforeground="#383838", bd=0, highlightthickness=0)
point.place(x=24, y=526, width=60, height=60)
num0=tk.Button(root, text="0", font=("Open Sans ExtraBold", 30), bg="#aee1c9", fg="#2c2c2c", activebackground="#a7dfc0", activeforeground="#383838", bd=0, highlightthickness=0)
num0.place(x=97, y=526, width=206, height=60)



root.mainloop()
