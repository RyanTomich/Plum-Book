import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import *

# Create Root window
root = tk.Tk()
root.title("Plum Book")
root.geometry('1000x800')

# Create Tabs
tabControl = ttk.Notebook(root)
new_year = ttk.Frame(tabControl)
all_data = ttk.Frame(tabControl)
names = ttk.Frame(tabControl)
plums = ttk.Frame(tabControl)
tabControl.add(new_year, text='New year')
tabControl.add(all_data, text='All Data')
tabControl.add(names, text='Names')
tabControl.add(plums, text='Plums')
tabControl.pack(expand=1, fill="both")


# Tab new_year Buttons
def submit():
    string = em_entry.get()
    emerson = str_to_lst(string)
    string = hi_entry.get()
    hillcrest = str_to_lst(string)
    string = ke_entry.get()
    kennedy = str_to_lst(string)
    string = ml_entry.get()
    margaret_leary = str_to_lst(string)
    string = we_entry.get()
    west = str_to_lst(string)
    string = wh_entry.get()
    whittier = str_to_lst(string)
    string = ea_entry.get()
    east = str_to_lst(string)

    print(emerson)
    print(hillcrest)
    print(kennedy)
    print(margaret_leary)
    print(west)
    print(whittier)
    print(east)


#
# Tab (New_year)
#

# Main Title
ttk.Label(new_year, text="Plum Book", font=("Courier", 40, "bold"), background="grey")\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(new_year, text="New year Data Input", font=("Courier", 25, "underline"), background="grey")\
    .grid(column=0, row=1, padx=5, pady=5)

# School Titles
ttk.Label(new_year, text="Emerson", background="grey").grid(column=0, row=2, padx=5, pady=5)
ttk.Label(new_year, text="Hillcrest", background="grey").grid(column=0, row=4, padx=5, pady=5)
ttk.Label(new_year, text="kennedy", background="grey").grid(column=0, row=6, padx=5, pady=5)
ttk.Label(new_year, text="Margaret Leary", background="grey").grid(column=0, row=8, padx=5, pady=5)
ttk.Label(new_year, text="West", background="grey").grid(column=0, row=10, padx=5, pady=5)
ttk.Label(new_year, text="Whittier", background="grey").grid(column=0, row=12, padx=5, pady=5)
ttk.Label(new_year, text="East", background="grey").grid(column=0, row=14, padx=5, pady=5)

# School Entry
em_entry = Entry(new_year, width=100)
em_entry.grid(column=0, row=3, padx=5, pady=5)
hi_entry = Entry(new_year, width=100)
hi_entry.grid(column=0, row=5, padx=5, pady=5)
ke_entry = Entry(new_year, width=100)
ke_entry.grid(column=0, row=7, padx=5, pady=5)
ml_entry = Entry(new_year, width=100)
ml_entry.grid(column=0, row=9, padx=5, pady=5)
we_entry = Entry(new_year, width=100)
we_entry.grid(column=0, row=11, padx=5, pady=5)
wh_entry = Entry(new_year, width=100)
wh_entry.grid(column=0, row=13, padx=5, pady=5)
ea_entry = Entry(new_year, width=100)
ea_entry.grid(column=0, row=15, padx=5, pady=5)

# Submit Button
Button(new_year, text="Submit", width=10, command=submit).grid(column=0, row=16, padx=15, pady=10)

#
# Tab (All_Data)
#

# Main Title
ttk.Label(all_data, text="Plum Book", font=("Courier", 40, "bold"), background="grey")\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(all_data, text="All data", font=("Courier", 25, "underline"), background="grey")\
    .grid(column=0, row=1, padx=5, pady=5)

#
# Tab (Names)
#

# Main Title
ttk.Label(names, text="Plum Book", font=("Courier", 40, "bold"), background="grey")\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(names, text="Names", font=("Courier", 25, "underline"), background="grey")\
    .grid(column=0, row=1, padx=5, pady=5)

#
# Tab (Plums)
#

# Main Title
ttk.Label(plums, text="Plum Book", font=("Courier", 40, "bold"), background="grey")\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(plums, text="Plums", font=("Courier", 25, "underline"), background="grey")\
    .grid(column=0, row=1, padx=5, pady=5)


# Run root window
root.mainloop()
