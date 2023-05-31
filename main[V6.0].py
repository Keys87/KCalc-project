import tkinter as tk
import customtkinter as ctk
import tkinter.font as font
import math as m

root = ctk.CTk()
root.geometry("800x120")
root.title("KCalc")
textbox_x = ctk.CTkEntry(master=root, width=150, border_width=2, fg_color="white", corner_radius=5)
tkinter_result = tk.DoubleVar()
tkinter_sign = tk.StringVar()
tkinter_textbox_y_state = tk.StringVar()
textbox_y = ctk.CTkEntry(master=root, width=150, border_width=2, fg_color="white", corner_radius=5)
label_sign = ctk.CTkLabel(master=root, textvariable=tkinter_sign)
label_result = ctk.CTkLabel(master=root, textvariable=tkinter_result)
label_equal_sign = ctk.CTkLabel(master=root, text="=")


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
add_onclick function is the function used to react to the event of a user pressing the '+' button.
All of onclick functions essentially are the same thing but just for diffrent operation
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

        sign = "√"
        tkinter_sign.set(sign)
        result = m.sqrt(x)
        tkinter_result.set(result)

    main_event()


font_for_buttons = font.Font(family="calibri", size=11, weight="bold")

button_add = ctk.CTkButton(master=root, text="+", command=add_onclick, width=140, corner_radius=5)
button_sub = ctk.CTkButton(master=root, text="-", command=sub_onclick, width=140, corner_radius=5)
button_mtpl = ctk.CTkButton(master=root, text="x", command=mtpl_onclick, width=140, corner_radius=5)
button_div = ctk.CTkButton(master=root, text=":", command=div_onclick, width=140, corner_radius=5)
button_pwr = ctk.CTkButton(master=root, text="^", command=pwr_onclick, width=140, corner_radius=5)
button_sqrt = ctk.CTkButton(master=root, text="√", command=sqrt_onclick, width=140, corner_radius=5)

textbox_x.grid(column=1, row=1, padx=10, pady=5)
label_sign.grid(column=2, row=1)
textbox_y.grid(column=3, row=1, padx=10, pady=5)
label_equal_sign.grid(column=4, row=1)
label_result.grid(column=5, row=1)
button_add.grid(column=1, row=2, padx=5, pady=5)
button_sub.grid(column=2, row=2, padx=5, pady=5)
button_mtpl.grid(column=3, row=2, padx=5, pady=5)
button_div.grid(column=4, row=2, padx=5, pady=5)
button_pwr.grid(column=1, row=3, padx=5, pady=5)
button_sqrt.grid(column=2, row=3, padx=5, pady=5)

root.mainloop()
