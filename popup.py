import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
times_ran = 0
def popup_window():
    r = tk.Tk()
    r.title('Are you sure you want to quit?')
    button1 = tk.Button(r, text='Yes', width=25, command=r.destroy)
    button2 = tk.Button(r, text='No', width = 25, command = r.destroy)
    button1.pack()
    button2.pack()
    r.mainloop()

popup_window()

