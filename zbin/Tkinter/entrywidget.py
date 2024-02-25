from customtkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = CTk()

entry = CTkEntry(window,
                 font=("Arial", 50),
                 fg_color="#00FF00",
                 bg_color="black",
                 show="*")
entry.pack(side=LEFT)

submit_button = CTkButton(window, text="submit",
                          command=submit)
submit_button.pack(side=RIGHT)

delete_button = CTkButton(window, text="delete",
                          command=delete)
delete_button.pack(side=RIGHT)

back_button = CTkButton(window, text="backspace",
                          command=backspace)
back_button.pack(side=RIGHT)

window.mainloop()