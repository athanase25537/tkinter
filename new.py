import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('My window App')
window.geometry('500x500')

# ttk widgets
label = ttk.Label(master=window, text='This is a label')
label.pack()

# tk widgets
text = tk.Text(master=window)
text.pack()

# run
window.mainloop()