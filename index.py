import tkinter as tk
from tkinter import ttk
from tkinter import *

# functions
def convert():
    try:
        textOutput.set(str(toConvert.get())+'miles = '+str(toConvert.get() * 1.60934)+'km')
    except:
        textOutput.set('Your must enter a number')

# window
window = tk.Tk()
window.title("Demo")
window.geometry('300x300')

# title
title_label = ttk.Label(window, text="Miles to kilometers", font= 'Calibri 15 bold')
title_label.pack(pady=10)

# input field
toConvert = IntVar()
input_frame = ttk.Frame(window)

entry = ttk.Entry(
    input_frame,
    textvariable=toConvert,
    )      
    
button = ttk.Button(
    input_frame, 
    text='Convert',
    command=convert,
    )

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=15)

# output
textOutput = StringVar()
output = ttk.Frame(window)
label = Label(output, 
              text="response", 
              font="Arial 15 bold",
              textvariable=textOutput
              )
label.pack()
output.pack()

# run
window.mainloop()

# functions
def convert():
    toConvert.get()
    
    