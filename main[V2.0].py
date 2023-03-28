import tkinter as tk
import tkinter.font as font

root = tk.Tk()
textbox_x = tk.Entry(relief="solid")
textbox_y = tk.Entry(relief="solid")
tkinter_result = tk.DoubleVar()
tkinter_sign = tk.StringVar()
label_sign = tk.Label(textvariable=tkinter_sign)
label_result = tk.Label(textvariable=tkinter_result)
label_equal_sign = tk.Label(text="=")


def value_checker():
    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = float(textbox_x.get())
        return x

    elif x == " ":
        x = 0.0
        return x

    if y != " ":
        y = float(textbox_y.get())
        return y

    elif y == " ":
        y = 0.0
        return y


def add_onclick():
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

    def main_event():
        sign = "+"
        tkinter_sign.set(sign)
        result = x + y
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


font_for_buttons = font.Font(family="calibri", size=11)


button_add = tk.Button(text="+", command=add_onclick, relief="solid", bd=1, width=6)
button_sub = tk.Button(text="-", command=sub_onclick, relief="solid", bd=1, width=6)
button_mtpl = tk.Button(text="x", command=mtpl_onclick, relief="solid", bd=1, width=6)
button_div = tk.Button(text=":", command=div_onclick, relief="solid", bd=1, width=6)
button_add["font"] = font_for_buttons
button_sub["font"] = font_for_buttons
button_mtpl["font"] = font_for_buttons
button_div["font"] = font_for_buttons
textbox_x["font"] = font_for_buttons
textbox_y["font"] = font_for_buttons
label_sign["font"] = font_for_buttons
label_result["font"] = font_for_buttons
label_equal_sign["font"] = font_for_buttons


textbox_x.grid(column=1, row=1)
label_sign.grid(column=2, row=1)
textbox_y.grid(column=3, row=1)
label_equal_sign.grid(column=4, row=1)
label_result.grid(column=5, row=1)
button_add.grid(column=1, row=2)
button_sub.grid(column=2, row=2)
button_mtpl.grid(column=3, row=2)
button_div.grid(column=4, row=2)

root.mainloop()
