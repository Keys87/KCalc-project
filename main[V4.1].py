import tkinter as tk
import tkinter.font as font
import tkinter.messagebox as mbox
import math as m

root = tk.Tk()
textbox_x = tk.Entry(width=15)
tkinter_result = tk.DoubleVar()
tkinter_sign = tk.StringVar()
tkinter_textbox_y_state = tk.StringVar()
textbox_y = tk.Entry(width=15)
label_sign = tk.Label(textvariable=tkinter_sign)
label_result = tk.Label(textvariable=tkinter_result)
label_equal_sign = tk.Label(text="=")


def comma_support(x, y):
    x_str_list = x.split(sep=",")
    y_str_list = y.split(sep=",")
    len_x = len(x_str_list) - 1
    len_y = len(y_str_list)
    element = 0
    while element < len_x:
        x = f"{x_str_list[element]}"
        element += 1
        x = f"{x}{x_str_list[element]}"
        if element == len_x - 1:
            return int(x)

    element = 0
    while element < len_y:
        y = f"{y_str_list[element]}"
        element += 1
        y = f"{y}{y[element]}"
        if element == len_y - 1:
            return int(y)


def add_onclick():
    x = textbox_x.get()
    y = textbox_y.get()
    comma_support(x, y)
    if x != " ":
        x = float(textbox_x.get())

    elif x == " ":
        x = 0.0

    if y != " ":
        y = float(textbox_y.get())

    elif y == " ":
        y = 0.0

    def main_event():
        sign = "+"
        result = x + y
        tkinter_sign.set(sign)
        tkinter_result.set(result)

    main_event()


def sub_onclick():
    def main_event():
        sign = "-"
        tkinter_sign.set(sign)
        result = x - y
        tkinter_result.set(result)

    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = float(textbox_x.get())

    elif x == " ":
        x = 0.0

    if y != " ":
        y = float(textbox_y.get())

    elif y == " ":
        y = 0.0

    main_event()


def mtpl_onclick():
    def main_event():
        sign = "x"
        tkinter_sign.set(sign)
        result = x * y
        tkinter_result.set(result)

    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = float(textbox_x.get())

    elif x == " ":
        x = 0.0

    if y != " ":
        y = float(textbox_y.get())

    elif y == " ":
        y = 0.0

    main_event()


def div_onclick():
    def main_event():
        sign = ":"
        tkinter_sign.set(sign)
        result = x / y
        tkinter_result.set(result)

    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = float(textbox_x.get())

    elif x == " ":
        x = 0.0

    if y != " ":
        y = float(textbox_y.get())

    elif y == " ":
        y = 0.0

    main_event()


def pwr_onclick():
    def main_event():
        sign = "^"
        tkinter_sign.set(sign)
        result = m.pow(x, y)
        tkinter_result.set(result)

    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = float(textbox_x.get())

    elif x == " ":
        x = 0.0

    if y != " ":
        y = float(textbox_y.get())

    elif y == " ":
        y = 0.0

    main_event()


def sqrt_onclick():
    def main_event():
        x = textbox_x.get()
        y = textbox_y.get()

        if x != " ":
            x = float(textbox_x.get())

        elif x == " ":
            x = 0.0
        if y != "  ":
            mbox.Message("Text inserted to the second textbox will be ignored")
        sign = "√"
        tkinter_sign.set(sign)
        result = m.sqrt(x)
        tkinter_result.set(result)

    main_event()


font_for_buttons = font.Font(family="calibri", size=11, weight="bold")

button_add = tk.Button(text="+", command=add_onclick, width=10)
button_sub = tk.Button(text="-", command=sub_onclick, width=10)
button_mtpl = tk.Button(text="x", command=mtpl_onclick, width=10)
button_div = tk.Button(text=":", command=div_onclick, width=10)
button_pwr = tk.Button(text="^", command=pwr_onclick, width=10)
button_sqrt = tk.Button(text="√", command=sqrt_onclick, width=10)

textbox_x.grid(column=1, row=1)
label_sign.grid(column=2, row=1)
textbox_y.grid(column=3, row=1)
label_equal_sign.grid(column=4, row=1)
label_result.grid(column=5, row=1)
button_add.grid(column=1, row=2)
button_sub.grid(column=2, row=2)
button_mtpl.grid(column=3, row=2)
button_div.grid(column=4, row=2)
button_pwr.grid(column=1, row=3)
button_sqrt.grid(column=2, row=3)

root.mainloop()
