import tkinter as tk


root = tk.Tk()
textbox_x = tk.Entry()
textbox_y = tk.Entry()
tkinter_result = tk.IntVar()
tkinter_sign = tk.StringVar()
label_sign = tk.Label(textvariable=tkinter_sign)
label_result = tk.Label(textvariable=tkinter_result)


def value_checker():
    x = textbox_x.get()
    y = textbox_y.get()
    if x != " ":
        x = int(textbox_x.get())
        return x
    if y != " ":
        y = int(textbox_y.get())
        return y


def add_onclick():
    def main_event(local_x, local_y):
        sign = "+"
        tkinter_sign.set(sign)
        result = local_x + local_y
        tkinter_result.set(result)
    
    value_checker()
    main_event()

def sub_onclick(local_x, local_y):
    def main_event():
        sign = "-"
        tkinter_sign.set(sign)
        result = local_x - local_y
        tkinter_result.set(result)
        
    value_checker()
    main_event()


def mtpl_onclick(local_x, local_y):
    def main_event():
        sign = "x"
        tkinter_sign.set(sign)
        result = local_x * local_y
        tkinter_result.set(result) 
     
    value_checker()
    main_event()   
 

def div_onclick(local_x, local_y):
	def main_event():
        sign = ":"
        tkinter_sign.set(sign)
        result = local_x / local_y
        tkinter_result.set(result)
        
    value_checker()
    main_event()

button_add = tk.Button(text="+", command=add_onclick)
button_sub = tk.Button(text="-", command=sub_onclick)
button_mtlp = tk.Button(text="x", command=mtpl_onclick)
button_div = tk.Button(text=":", command=div_onclick)
textbox_x.grid(column=1, row=1)
label_sign.grid(column=2, row=1)
textbox_y.grid(column=3, row=1)
label_result.grid(column=4, row=1)
button_sub.grid(column=2, row=3)
button_add.grid(column=1, row=3)
button_div.grid(column=4, row=3)
button_mtlp.grid(column=3, row=3)


root.mainloop()