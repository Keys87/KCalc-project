import widget_store as ws
import math as m
import tkinter as tk


root = ws.Root(300, 400)
textbox_x = ws.Entry()
textbox_y = ws.Entry()
tkinter_result = tk.DoubleVar()
tkinter_sign = tk.StringVar()
label_sign = ws.DynamicLabel(textvariable=tkinter_sign)
label_result = ws.DynamicLabel(textvariable=tkinter_result)
label_equal_sign = ws.Label(text="=")

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

        sign = "√"
        tkinter_sign.set(sign)
        result = m.sqrt(x)
        tkinter_result.set(result)

    main_event()

button_add = ws.Button(text="+", command=add_onclick, width=12)
button_sub = ws.Button(text="-", command=sub_onclick, width=12)
button_mtpl = ws.Button(text="x", command=mtpl_onclick, width=12)
button_div = ws.Button(text=":", command=div_onclick, width=12)
button_pwr = ws.Button(text="^", command=pwr_onclick, width=12)
button_sqrt = ws.Button(text="√", command=sqrt_onclick, width=12)

#not done yet...