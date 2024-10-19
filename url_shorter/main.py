import tkinter as tk
import pyshorteners as short

# functions
def shorten():
    print('Url shorted')
    shortener = short.Shortener()
    short_url = shortener.tinyurl.short(longUrl.get())
    shortUrl.set(short_url)
    
# create window
root = tk.Tk()
root.geometry('300x300')
root.title('URL Shortener')
root.resizable(False, False)

# widgets variables
longUrl = tk.StringVar()
shortUrl = tk.StringVar()
# creating widgets
long_url_label = tk.Label(master=root,
                 text='Enter Long URL')
long_url_entry = tk.Entry(master=root,
                          textvariable=longUrl)
short_url_label = tk.Label(master=root,
                           text='Output shortened URL')
short_url_entry = tk.Entry(master=root,
                           text=shortUrl)
shorten_button = tk.Button(master=root,
                           text='Shorten URL',
                           command=shorten)

# placing widgets
long_url_label.pack()
long_url_entry.pack()
short_url_label.pack()
short_url_entry.pack()
shorten_button.pack()

#run
root.mainloop()