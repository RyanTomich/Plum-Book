import tkinter as tk
from tkinter import *
from tkinter import ttk

# Make window
root = tk.Tk()
root.title("Plum Book")
root.geometry('1500x900')

# Create Tabs
tabControl = ttk.Notebook(root)
new_year = ttk.Frame(tabControl)
all_data = ttk.Frame(tabControl)
tabControl.add(new_year, text='New year')
tabControl.add(all_data, text='All Data')
tabControl.pack(expand=1, fill="both")

# Tab New_year
ttk.Label(new_year, text="New year Data Input", background="grey").grid(column=0,row=0,padx=30,pady=30)
school_entry = Entry(new_year).grid(column=3, row=0, padx=30, pady=30)

# Tab All_Data
ttk.Label(all_data, text="Lets dive into the world of computers").grid(column=0,row=0,padx=30,pady=30)


# Run
root.mainloop()