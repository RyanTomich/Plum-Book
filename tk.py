import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import *

# Create Root window
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


# Tab new_year Buttons
def submit():
    str = em_entry.get()
    emerson = str_to_lst(str)
    str = hi_entry.get()
    hilcrest = str_to_lst(str)
    str = ke_entry.get()
    kenidy = str_to_lst(str)
    str = ml_entry.get()
    margret_leary = str_to_lst(str)
    str = we_entry.get()
    west = str_to_lst(str)
    str = wh_entry.get()
    whiter = str_to_lst(str)
    str = ea_entry.get()
    east = str_to_lst(str)

    print(emerson)
    print(hilcrest)
    print(kenidy)
    print(margret_leary)
    print(west)
    print(whiter)
    print(east)



# Tab (New_year)
# School Titles
ttk.Label(new_year, text="New year Data Input", background="grey").grid(column=0, row=0, padx=5, pady=5)
ttk.Label(new_year, text="Emerson", background="grey").grid(column=0, row=1, padx=5, pady=5)
ttk.Label(new_year, text="Hillcrest", background="grey").grid(column=0, row=3, padx=5, pady=5)
ttk.Label(new_year, text="Kennedy", background="grey").grid(column=0, row=5, padx=5, pady=5)
ttk.Label(new_year, text="Margret Leary", background="grey").grid(column=0, row=7, padx=5, pady=5)
ttk.Label(new_year, text="West", background="grey").grid(column=0, row=9, padx=5, pady=5)
ttk.Label(new_year, text="Whittier", background="grey").grid(column=0, row=11, padx=5, pady=5)
ttk.Label(new_year, text="East", background="grey").grid(column=0, row=13, padx=5, pady=5)

# School Entry
em_entry = Entry(new_year, width=100)
em_entry.grid(column=0, row=2, padx=5, pady=5)
hi_entry = Entry(new_year, width=100)
hi_entry.grid(column=0, row=4, padx=5, pady=5)
ke_entry = Entry(new_year, width=100)
ke_entry.grid(column=0, row=6, padx=5, pady=5)
ml_entry = Entry(new_year, width=100)
ml_entry.grid(column=0, row=8, padx=5, pady=5)
we_entry = Entry(new_year, width=100)
we_entry.grid(column=0, row=10, padx=5, pady=5)
wh_entry = Entry(new_year, width=100)
wh_entry.grid(column=0, row=12, padx=5, pady=5)
ea_entry = Entry(new_year, width=100)
ea_entry.grid(column=0, row=14, padx=5, pady=5)

# Submit Button
Button(new_year, text="Submit", width=10, command=submit).grid(column=0, row=15, padx=15, pady=10)


# Tab (All_Data)
ttk.Label(all_data, text="Lets dive into the world of computers").grid(column=0, row=0, padx=10, pady=10)

# Run root window
root.mainloop()
