import tkinter as tk
import math as m
import customtkinter as ctk


root = ctk.CTk()
root.title("KCalc")
root.geometry("245x98")
equation = ""
main_entry_text = tk.StringVar()
# to make a usual calculator we need to appen the string, such as "1" to the text in textbox, then get oython to eval() that
# next version is to add numpad not just opsignpad
main_frame = tk.Frame(root)
main_entry = tk.Entry(width=40, textvariable=main_entry_text)


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


def result_onclick(local_equation=equation):
   local_equation =  main_entry.get()
   local_equation = local_equation.replace("X", "*")
   local_equation = local_equation.replace("x", "*")
   # below is the algorithm to find X or x in text that is from entry widget, this here because X is used to indicate 'multiply by' operation in the app
   

   main_entry_text.set("")
   main_entry_text.set(eval(local_equation))


def add_onclick():
    main_entry_text.set(f"{main_entry.get()}+")


def sub_onclick():
    main_entry_text.set(f"{main_entry.get()}-")
                      

def mtpl_onclick():
    main_entry_text.set(f"{main_entry.get()}x")


def div_onclick():
    main_entry_text.set(f"{main_entry.get()}/")

add_button = tk.Button(main_frame, text="+", width=16, command=add_onclick)
sub_button = tk.Button(main_frame, text="-", width=16, command=sub_onclick)
mtpl_button = tk.Button(main_frame, text="x", width=16, command=mtpl_onclick)
div_button = tk.Button(main_frame, text="/", width=16, command=div_onclick)
result_button = tk.Button(root, text="=", width=34, command=result_onclick)

main_entry.grid(column=1, row=1)
main_frame.grid(column=1, row=2)
result_button.grid(column=1, row=3)
add_button.grid(column=1, row=1)
sub_button.grid(column=2, row=1)
mtpl_button.grid(column=1, row=2)
div_button.grid(column=2, row=2)

root.mainloop()
