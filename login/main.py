import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# functions
def login():
    username = "athanase"
    password = "12345678"
    if(text_password.get() == password and text_username.get() == username):
        messagebox.showinfo(title='Login Success',
                            message='Successfully logged in !')
        print('Successfully logged in !')
    else:
        print('Invalid username or password')

# window
window = tk.Tk()
window.title('Login form')
window.configure(bg='#333333')
window.geometry('540x640')


# creating frame
frame = tk.Frame(master=window,
                 bg='#333333',
                 )

# creating widgets
text_password = tk.StringVar()
text_username = tk.StringVar()

login_label = tk.Label(master=frame, 
                        text='Login', 
                        background='#333333', 
                        foreground='#ff3399',
                        font='Arial 30',
                        
                        )
username_label = ttk.Label(master=frame, 
                           text='Username', 
                           background='#333333', 
                           foreground='#ffffff',
                           font='Arial 16',
                           
                           )
password_label = ttk.Label(master=frame, 
                           text='Password', 
                           background='#333333', 
                           foreground='#ffffff',
                           font='Arial 16',
                           )
password_entry = ttk.Entry(master=frame, 
                           show=".",
                           font='Arial 16',
                           textvariable=text_password
                           
                           )
username_entry = ttk.Entry(master=frame,
                           font='Arial 16',
                           textvariable=text_username,
                           
                           )
login_button = tk.Button(master=frame, 
                         text='Login', 
                         bg='#ff3399', 
                         fg='#ffffff',
                         font='Arial 16',
                         command=login,
                         
                         )

# placing widgets on the screen
login_label.grid(row=0, 
                 column=0, 
                 columnspan=3, 
                 pady=40,
                 sticky='news')
username_label.grid(row=1, 
                    column=0)
username_entry.grid(row=1, 
                    column=1,
                    pady=20,
                    )
password_label.grid(row=2, 
                    column=0)
password_entry.grid(row=2, 
                    column=1,
                    pady=20,
                    )
login_button.grid(row=3, 
                  column=0, 
                  columnspan=2,
                  pady=10,
                  )

# placing frame
frame.pack()
# run
window.mainloop()