import tkinter.font as font
import tkinter.messagebox as mbox
import math as m

root = tk.Tk()
textbox_x = tk.Entry(width=15, bd=2)
tkinter_result = tk.DoubleVar()
tkinter_sign = tk.StringVar()
tkinter_textbox_y_state = tk.StringVar()
textbox_y = tk.Entry(width=15, bd=2)
label_sign = tk.Label(textvariable=tkinter_sign)
label_result = tk.Label(textvariable=tkinter_result)
label_equal_sign = tk.Label(text="=")


def comma_support_a(a):
    a_str_list = a.split(sep=",")
    index = 0
    tracker = 1

    a = f"{a_str_list[index]}"
    index += 1

    while len(a_str_list) > tracker:  # repeat by 2 if len(str_list) == 3
        a = f"{a}{a_str_list[index]}"
        index += 1
        tracker += 1

    a = float(a)
    return a


def comma_support_b(b):
    b_str_list = b.split(sep=",")
    index = 0
    tracker = 1

    b = f"{b_str_list[index]}"
    index += 1

    while len(b_str_list) > tracker:  # repeat by 2 if len(str_list) == 3
        b = f"{b}{b_str_list[index]}"
        index += 1
        tracker += 1

    b = float(b)
    return b


"""
add_onclick function is the function used to react to the event of a user pressing the '+' button
"""


def add_onclick():
    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = comma_support_a(x)

    elif x == " ":
        x = 0.0

    if y != " ":
        y = comma_support_b(y)

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
        x = comma_support_a(x)

    elif x == " ":
        x = 0.0

    if y != " ":
        y = comma_support_b(y)

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
        x = comma_support_a(x)

    elif x == " ":
        x = 0.0

    if y != " ":
        y = comma_support_b(y)

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
        x = comma_support_a(x)

    elif x == " ":
        x = 0.0

    if y != " ":
        y = comma_support_b(y)

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
        x = comma_support_a(x)

    elif x == " ":
        x = 0.0

    if y != " ":
        y = comma_support_b(y)

    elif y == " ":
        y = 0.0

    main_event()


def sqrt_onclick():
    def main_event():
        x = textbox_x.get()
        y = textbox_y.get()

        if x != " ":
            x = comma_support_a(x)

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

button_add = tk.Button(text="+", command=add_onclick, width=12)
button_sub = tk.Button(text="-", command=sub_onclick, width=12)
button_mtpl = tk.Button(text="x", command=mtpl_onclick, width=12)
button_div = tk.Button(text=":", command=div_onclick, width=12)
button_pwr = tk.Button(text="^", command=pwr_onclick, width=12)
button_sqrt = tk.Button(text="√", command=sqrt_onclick, width=12)

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
