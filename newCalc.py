import tkinter as tk


root = tk.Tk()
textbox_x = tk.Entry()
textbox_y = tk.Entry()
tkinter_result = tk.IntVar()
tkinter_sign = tk.StringVar()
label_sign = tk.Label(textvariable=tkinter_sign)
label_result = tk.Label(textvariable=tkinter_result)

x = textbox_x.get()
y = textbox_y.get()
if x == " ":
    x = int(textbox_x.get())

if y == " ":
    y = int(textbox_y.get())


def add_onclick():
    sign = "+"
    tkinter_sign.set(sign)
    result = x + y
    tkinter_result.set(result)

def sub_onclick():
    sign = "-"
    tkinter_sign.set(sign)
    result = x - y
    tkinter_result.set(result)


def mtpl_onclick():
    sign = "x"
    tkinter_sign.set(sign)
    result = x * y
    tkinter_result.set(result) 
 

def div_onclick():
    sign = ":"
    tkinter_sign.set(sign)
    result = x / y
    tkinter_result.set(result)
        

button_add = tk.Button(text="+", command=add_onclick)
button_sub = tk.Button(text="-", command=sub_onclick)
button_mtlp = tk.Button(text="x", command=mtpl_onclick)
button_div = tk.Button(text=":", command=div_onclick)
textbox_x.grid(column=1, row=1)
label_sign.grid(column=2, row=1)
textbox_y.grid(column=3, row=1)
label_result.grid(column=4, row=1)
button_sub.grid(column=1, row=3)
button_add.grid(column=1, row=3)


root.mainloop()
