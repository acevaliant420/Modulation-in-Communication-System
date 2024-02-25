from customtkinter import *

def createwin():
    new_win = CTk()
    old_win.destroy()
    new_win.mainloop()

old_win = CTk()

CTkButton(old_win, text="create new window", command=createwin).pack()

old_win.mainloop()