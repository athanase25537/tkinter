from tkinter import *
from tkinter.font import Font
# frame config
frame = Tk()
frame.geometry('400x400')
frame.title('First Python Frame - Athanos')
frame['bg'] = 'green'
frame.resizable(height=False, width=False)

font = Font(family="Verdana", size=16, weight="normal")
label = Label(
    frame, 
    text="Write Here",
    font=font,
    fg="white",
    bg="green"
    )
# label.pack(side=RIGHT, padx=50)
textWidth = font.measure("Write Here")
textHeight = font.metrics("linespace")
label.place(x=200-(textWidth/2), y=200-(textHeight/2))

# create input
b = StringVar()
a = Entry(frame, textvariable=b)
a.pack()
# create button
def greeting():
    label['text'] = b.get()
    
btn = Button(
    frame, 
    text="Click Me", 
    bg="blue", 
    fg="white",
    command=greeting)
btn.pack()

# show frame
frame.mainloop()