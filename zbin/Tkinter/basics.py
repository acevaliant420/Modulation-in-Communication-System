from tkinter import *
import customtkinter as tk

window = tk.CTk()


window.title("Hello World")
#window.geometry("720x480")


icon = PhotoImage(file='E:\\College\\First Year\\SEM 2\\2. Labs\\PH170\\Project\\Tkinter\\icon.png')
window.iconphoto(True, icon)
#tk.set_default_color_theme("blue")

label = tk.CTkLabel(window,
                    text="Hello Rajat",
                    font=('Arial', 40, 'bold'),
                    fg_color='black',
                    padx=20,
                    pady=20,
                    image=icon,
                    compound='bottom')
label.pack()
#label.place(x=100, y=100)
#window.config(background='blue')


window.mainloop()