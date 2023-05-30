import customtkinter as tk


# This file supposed to be imported not executed. DO NOT EXECUTE THIS FILE #


class Button(tk.CTkButton):
    def __init__(self, text, command, bg, width):
        text = text # text to be displayed on the button
        command = command # function to execute on click
        fg = bg
        width = width
        

class Label(tk.CTkLabel):
    def __init__(self, text):
        text = text # text to be displayed on the label
        

class DynamicLabel(tk.CTkLabel):
    def __init__(self, textvariable):
        textvariable = textvariable # text to be displayed on the label
        
        
class Root(tk.CTk):
    def __init__(self, X, Y):
        tk.CTk.geometry(f"{X}x{Y}")
        tk.set_default_color_theme("dark-blue")
        tk.set_appearance_mode("system")
        

class Entry(tk.CTkEntry):
    def __init__(self):
        pass
        