from tkinter import ttk


class SelectBox(ttk.Combobox):
    def __init__(self, master=None, text_variable=None, values=None):
        super().__init__(master, textvariable=text_variable)

        self["state"] = "readonly"
        self["values"] = values
