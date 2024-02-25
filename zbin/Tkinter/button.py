import tkinter
from customtkinter import *

def click():
    print("You clicked the button!")

window = CTk()

button = CTkButton(window,
                   text="CLICK ME",
                   command=click,
                   font=("Comic Sans", 30),
                   state=ACTIVE)
button.pack()

window.mainloop()