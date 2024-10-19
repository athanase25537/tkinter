import tkinter as tk
from tkinter import ttk

# creating window
window = tk.Tk()
window.title('Data Entry Form')
window.geometry('700x550')

# creating frame
frame = tk.Frame(window)
frame.pack()

# saving the user info
user_info_frame = tk.LabelFrame(frame,
                                text="User Information",
                                )
user_info_frame.grid(row=0,
                     column=0,
                     )
firstname_label = tk.Label(user_info_frame,
                           text='First Name')
firstname_label.grid(row=0, 
                     column=0,)

lastname_label = tk.Label(user_info_frame,
                           text='Last Name')
lastname_label.grid(row=0, 
                     column=1,)

firstname_entry = tk.Entry(user_info_frame,
)
firstname_entry.grid(row=1,
                     column=0,)

lastname_entry = tk.Entry(user_info_frame)
lastname_entry.grid(row=1,
                    column=1,)

title_label = tk.Label(user_info_frame,
                 text='Title')
title_label.grid(row=0,
           column=2)
title_combobox = ttk.Combobox(user_info_frame,
                              values=[
                                  '',
                                  'Mr',
                                  'Ms',
                                  'Dr'
                              ])
title_combobox.grid(row=1,
                    column=2)

age_label = tk.Label(user_info_frame,
                    text='Age')
age_label.grid(row=2,
               column=0)
age_entry = ttk.Spinbox(user_info_frame,
                        from_=0,
                        to=100)
age_entry.grid(row=3,
               column=0)

nationaly_label = tk.Label(user_info_frame,
                           text='Nationality')
nationaly_label.grid(row=2,
                     column=1)
nationaly_entry = ttk.Combobox(user_info_frame,
                               values=['', 'Malagasy', 'French', 'American', 'Britich'])
nationaly_entry.grid(row=3,
                     column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# saving course info
user_course_frame = tk.LabelFrame(frame, text='Course Info')
user_course_frame.grid(row=1, column=0, sticky='news')

register_label = tk.Label(user_course_frame, text='Registration Status')
register_label.grid(row=0,
                    column=0)
reister_entry = tk.Checkbutton(user_course_frame,
                               text='Currently Registered')
reister_entry.grid(row=1,
                   column=0)

numcoures_label = tk.Label(user_course_frame, 
                           text='# Complete Courses')
numcoures_label.grid(row=0,
                     column=1)
numcoures_spinbox = ttk.Spinbox(user_course_frame,
                               from_=0,
                               to='infinity')
numcoures_spinbox.grid(row=1,
                       column=1)

semester_label = tk.Label(user_course_frame, 
                           text='# Complete Senesters')
semester_label.grid(row=0,
                     column=2)
semester_spinbox = ttk.Spinbox(user_course_frame,
                               from_=0,
                               to='infinity')
semester_spinbox.grid(row=1,
                       column=2)
# run the app
window.mainloop()