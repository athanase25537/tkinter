import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

entries = []
comboboxes = []
spinboxes = []

# functions  
def editUser():
    newWindow = tk.Toplevel(window)
    newWindow.title('Ajouter les utilisateurs')
    newWindow.geometry('700x700')
    frame = ttk.Frame(newWindow)
    frame.pack()
    
    k = 0
    for i in range(0,int(number_user_entry.get())):
        ttk.Label(frame, text='Somme a payer').grid(row=k, column=3)
        topay =ttk.Label(frame, text='non defini')
        topay.grid(row=k+1, column=3)
        ttk.Label(frame,text="Prenom user (*) "+str(k+1)).grid(row=k, column=0)
        entry = ttk.Entry(frame)
        entry.grid(row=k+1, column=0)
        entries.append(entry)
        ttk.Label(frame, text='Type d\'utilisateur (*)').grid(row=k, column=1)
        combobox = ttk.Combobox(frame, values=['Normale', 'Autre'])
        combobox.grid(row=k+1, column=1)
        comboboxes.append(combobox)
        ttk.Label(frame, text='Nombre de jour d\'absence').grid(row=k, column=2)
        spinbox = ttk.Spinbox(frame,from_=0,to='infinity')
        spinbox.grid(row=k+1, column=2)
        spinboxes.append(spinbox)
        k = k + 2
            
    btn_validate = ttk.Button(frame, text='Sauvegarder', command=validateData)
    btn_validate.grid(row=k, column=1)

def validateData():
    print('Data validation')
    for i in range(len(entries)):
        if entries[i].get() == '': 
            messagebox.showerror(title='Donnees invalid',
                                 message='Le champ prenom est obligatoire')
            break
    for i in range(len(comboboxes)):
        if comboboxes[i].get() == '':
            messagebox.showerror(title='Donnees invalid',
                                 message='Choisir entre utilisateur normal ou autre')
            break
    for i in range(len(spinboxes)):
        if spinboxes[i].get() == '':
            spinboxes[i].set(0)
            break
    
# window
window = tk.Tk()
window.title('Zaraoma')
window.geometry('400x400')

# add user
number_user_label = ttk.Label(window,
                              text='Entrer le nombre d\'utilisateur')
number_user_label.pack(pady=50)
number_user_entry = ttk.Spinbox(window,
                          from_=1,
                          to='infinity',)
number_user_entry.pack(pady=5)
btn = ttk.Button(window,
                 text='Valider',
                 command=editUser)
btn.pack()


# run app
window.mainloop()