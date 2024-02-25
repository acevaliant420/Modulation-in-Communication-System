from customtkinter import *
from tkinter import ttk

window = CTk()

notebook = ttk.Notebook(window)

tab1 = CTkFrame(notebook)

tab2 = CTkFrame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack()

CTkLabel(tab1, text="HELLO TAB 1", width=50, height=25).pack()
CTkLabel(tab2, text="TAB 2 HELLLO", width=50, height=25).pack()



window.mainloop()

