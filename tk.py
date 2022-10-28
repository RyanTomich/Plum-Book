# TODO imports and references
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import *


# TODO creating GUI structure

# Create Root window
root = tk.Tk()
root.title("Plum Book")
root.geometry('900x700')

# Create Tabs
tabControl = ttk.Notebook(root)
new_year = ttk.Frame(tabControl)
all_data = ttk.Frame(tabControl)
plums = ttk.Frame(tabControl)
tabControl.add(new_year, text='New year')
tabControl.add(all_data, text='All Data')
tabControl.add(plums, text='Plums')
tabControl.pack(expand=1, fill="both")

# TODO button functions


# Tab new_year Buttons
def submit():
    year_input = year_entry_input.get()
    grad_year_input = grad_year_entry_input.get()
    season = v.get()
    honor = c.get()

    print(year_input)
    print(grad_year_input)

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

    em_entry.delete(0, END)
    hi_entry.delete(0, END)
    ke_entry.delete(0, END)
    ml_entry.delete(0, END)
    we_entry.delete(0, END)
    wh_entry.delete(0, END)
    ea_entry.delete(0, END)

    # add each person to database with school assignment
    school = "emerson"
    for i in emerson:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)

    school = "hillcrest"
    for i in hillcrest:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)

    school = "kennedy"
    for i in kennedy:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)

    school = "margaret_leary"
    for i in margaret_leary:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)

    school = "west"
    for i in west:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)

    school = "whittier"
    for i in whittier:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)

    school = "east"
    for i in east:
        first, last = (split_name(i))
        rawdata_insert(first, last, grad_year_input, year_input, school, season, honor)


# TODO Tab (New_year)

# Main Title
ttk.Label(new_year, text="Plum Book", font=("Courier", 40, "bold"))\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(new_year, text="New year Data Input", font=("Courier", 25, "underline"))\
    .grid(column=0, row=1, padx=5, pady=5)

# Titles
ttk.Label(new_year, text="Emerson").grid(column=0, row=2, padx=5, pady=5)
ttk.Label(new_year, text="Hillcrest").grid(column=0, row=4, padx=5, pady=5)
ttk.Label(new_year, text="Kennedy").grid(column=0, row=6, padx=5, pady=5)
ttk.Label(new_year, text="Margaret Leary").grid(column=0, row=8, padx=5, pady=5)
ttk.Label(new_year, text="West").grid(column=0, row=10, padx=5, pady=5)
ttk.Label(new_year, text="Whittier").grid(column=0, row=12, padx=5, pady=5)
ttk.Label(new_year, text="East").grid(column=0, row=14, padx=5, pady=5)
ttk.Label(new_year, text="Year(2020-2021 is 2021)").grid(column=1, row=2, padx=5, pady=5)
ttk.Label(new_year, text="Graduation Year").grid(column=1, row=4, padx=4, pady=5)
ttk.Label(new_year, text="Season").grid(column=1, row=6, padx=4, pady=5)
ttk.Label(new_year, text="Honor").grid(column=1, row=9, padx=4, pady=5)

# year
year_entry_input = Entry(new_year, width=10)
year_entry_input.grid(column=1, row=3, padx=5, pady=5)

# grad year
grad_year_entry_input = Entry(new_year, width=10)
grad_year_entry_input.grid(column=1, row=5, padx=5, pady=5)

# season Entry
v = tk.StringVar()
v.set("1")

ttk.Radiobutton(new_year, text="Fall", variable=v, value="1").grid(column=1, row=7, padx=5, pady=5)
ttk.Radiobutton(new_year, text="Spring", variable=v, value="2").grid(column=1, row=8, padx=5, pady=5)

# Honor Entry
c = tk.StringVar()
c.set("1")

ttk.Radiobutton(new_year, text="Gold", variable=c, value="3").grid(column=1, row=10, padx=5, pady=5)
ttk.Radiobutton(new_year, text="Silver", variable=c, value="2").grid(column=1, row=11, padx=5, pady=5)
ttk.Radiobutton(new_year, text="Bronze", variable=c, value="1").grid(column=1, row=12, padx=5, pady=5)

# School Entry
em_entry = Entry(new_year, width=60)
em_entry.grid(column=0, row=3, padx=5, pady=5)
hi_entry = Entry(new_year, width=60)
hi_entry.grid(column=0, row=5, padx=5, pady=5)
ke_entry = Entry(new_year, width=60)
ke_entry.grid(column=0, row=7, padx=5, pady=5)
ml_entry = Entry(new_year, width=60)
ml_entry.grid(column=0, row=9, padx=5, pady=5)
we_entry = Entry(new_year, width=60)
we_entry.grid(column=0, row=11, padx=5, pady=5)
wh_entry = Entry(new_year, width=60)
wh_entry.grid(column=0, row=13, padx=5, pady=5)
ea_entry = Entry(new_year, width=60)
ea_entry.grid(column=0, row=15, padx=5, pady=5)

# Submit Button
Button(new_year, text="Submit", width=10, command=submit).grid(column=0, row=20, padx=15, pady=10)

# TODO Tab (All_Data)

# Main Title
ttk.Label(all_data, text="Plum Book", font=("Courier", 40, "bold"))\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(all_data, text="All data", font=("Courier", 25, "underline"))\
    .grid(column=0, row=1, padx=5, pady=5)

# treeview
# creating treeview
style = ttk.Style()
style.configure("Treeview", background="grey40", foreground="black", rowheight=20, fieldbackground="grey10")
style.map("Treeview", background=[('selected', 'grey100')])

# treeview frame
tree_frame = Frame(all_data)
tree_frame.grid(column=0, row=2, padx=5, pady=5)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
all_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
all_tree.pack()
tree_scroll.config(command=all_tree.yview)

# columns
all_tree['columns'] = ("First Name", "Last Name", "Grad Year", "Year", "School", "Season", "Honor", "oid")
all_tree.column("#0", width=0, stretch=NO)
all_tree.column("First Name", anchor=W, width=100)
all_tree.column("Last Name", anchor=W, width=100)
all_tree.column("Grad Year", anchor=CENTER, width=100)
all_tree.column("Year", anchor=CENTER, width=100)
all_tree.column("School", anchor=W, width=100)
all_tree.column("Season", anchor=CENTER, width=100)
all_tree.column("Honor", anchor=CENTER, width=100)
all_tree.column("oid", anchor=CENTER, width=100)

all_tree.heading("#0", text="", anchor=W)
all_tree.heading("First Name", text="First Name", anchor=W)
all_tree.heading("Last Name", text="Last Name", anchor=W)
all_tree.heading("Grad Year", text="Grad Year", anchor=CENTER)
all_tree.heading("Year", text="Year", anchor=CENTER)
all_tree.heading("School", text="School", anchor=W)
all_tree.heading("Season", text="Season", anchor=CENTER)
all_tree.heading("Honor", text="Honor", anchor=CENTER)
all_tree.heading("oid", text="OID", anchor=CENTER)

all_tree.tag_configure('oddrow', background="grey50")
all_tree.tag_configure('evenrow', background="grey70")

# Editing Data
# Entry boxes
data_frame = LabelFrame(all_data, text="Record")
data_frame.grid(column=0, row=3, padx="5", pady="5")

first_label = Label(data_frame, text="First Name:")
first_label.grid(row=0, column=0, padx=20, pady=10)
first_entry = Entry(data_frame)
first_entry.grid(row=0, column=1, padx=20, pady=10)

last_label = Label(data_frame, text="last name:")
last_label.grid(row=1, column=0, padx=20, pady=10)
last_entry = Entry(data_frame)
last_entry.grid(row=1, column=1, padx=20, pady=10)

grad_year_label = Label(data_frame, text="Graduation year:")
grad_year_label.grid(row=2, column=0, padx=20, pady=10)
grad_year_entry = Entry(data_frame)
grad_year_entry.grid(row=2, column=1, padx=20, pady=10)

year_label = Label(data_frame, text="Year:")
year_label.grid(row=3, column=0, padx=20, pady=10)
year_entry = Entry(data_frame)
year_entry.grid(row=3, column=1, padx=20, pady=10)

school_label = Label(data_frame, text="School:")
school_label.grid(row=0, column=3, padx=20, pady=10)
school_entry = Entry(data_frame)
school_entry.grid(row=0, column=4, padx=20, pady=10)

season_label = Label(data_frame, text="Season:")
season_label.grid(row=1, column=3, padx=20, pady=10)
season_entry = Entry(data_frame)
season_entry.grid(row=1, column=4, padx=20, pady=10)

honor_label = Label(data_frame, text="Honor:")
honor_label.grid(row=2, column=3, padx=20, pady=10)
honor_entry = Entry(data_frame)
honor_entry.grid(row=2, column=4, padx=20, pady=10)

oid_label = Label(data_frame, text="oid:")
oid_label.grid(row=3, column=3, padx=20, pady=10)
oid_entry = Entry(data_frame)
oid_entry.grid(row=3, column=4, padx=20, pady=10)


# misc functions
# Adding to database
def query_database():
    for record in all_tree.get_children():
        all_tree.delete(record)

    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    csr.execute("SELECT *, rowid FROM raw_table")
    records = csr.fetchall()

    # adding data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            all_tree.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
        else:
            all_tree.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('oddrow'))
        count += 1

    con.commit()
    con.close()


# Clearing entry widgets
def clear_entry():
    first_entry.delete(0, END)
    last_entry.delete(0, END)
    grad_year_entry.delete(0, END)
    year_entry.delete(0, END)
    school_entry.delete(0, END)
    season_entry.delete(0, END)
    honor_entry.delete(0, END)
    oid_entry.delete(0, END)


def conduct_search():
    lookup_record = search_entry.get()
    # close window
    search.destroy()
    # clear treeview
    for record in all_tree.get_children():
        all_tree.delete(record)

    selection = j.get()

    # database
    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    if selection == "1":
        csr.execute("SELECT *, rowid FROM raw_table WHERE first like ?", (lookup_record,))
        records = csr.fetchall()
    elif selection == "2":
        csr.execute("SELECT *, rowid FROM raw_table WHERE last like ?", (lookup_record,))
        records = csr.fetchall()
    elif selection == "3":
        csr.execute("SELECT *, rowid FROM raw_table WHERE grad_year like ?", (lookup_record,))
        records = csr.fetchall()
    elif selection == "4":
        csr.execute("SELECT *, rowid FROM raw_table WHERE year like ?", (lookup_record,))
        records = csr.fetchall()
    elif selection == "5":
        csr.execute("SELECT *, rowid FROM raw_table WHERE school like ?", (lookup_record,))
        records = csr.fetchall()
    elif selection == "6":
        csr.execute("SELECT *, rowid FROM raw_table WHERE season like ?", (lookup_record,))
        records = csr.fetchall()
    elif selection == "7":
        csr.execute("SELECT *, rowid FROM raw_table WHERE honor like ?", (lookup_record,))
        records = csr.fetchall()

    # adding data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            all_tree.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags='evenrow')
        else:
            all_tree.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags='oddrow')
        count += 1

    con.commit()
    con.close()


# Button Functions
# select
def select_record(e):
    first_entry.delete(0, END)
    last_entry.delete(0, END)
    grad_year_entry.delete(0, END)
    year_entry.delete(0, END)
    school_entry.delete(0, END)
    season_entry.delete(0, END)
    honor_entry.delete(0, END)
    oid_entry.delete(0, END)

    selected = all_tree.focus()
    values = all_tree.item(selected, 'values')

    first_entry.insert(0, values[0])
    last_entry.insert(0, values[1])
    grad_year_entry.insert(0, values[2])
    year_entry.insert(0, values[3])
    school_entry.insert(0, values[4])
    season_entry.insert(0, values[5])
    honor_entry.insert(0, values[6])
    oid_entry.insert(0, values[7])


# Remove one record
def remove_one():
    x = all_tree.selection()[0]
    all_tree.delete(x)

    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    csr.execute("DELETE from raw_table WHERE oid=" + oid_entry.get())

    con.commit()
    con.close()

    clear_entry()


# remove many
def remove_many():
    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    x = all_tree.selection()
    # delete from database
    for record in x:
        oid = (all_tree.item(record, 'values')[7])
        csr.execute("DELETE from raw_table WHERE oid=" + oid)

    # delete from treeview
    for record in x:
        all_tree.delete(record)

    con.commit()
    con.close()

    clear_entry()


# update record
def update_record():
    # update treeview
    selected = all_tree.focus()
    all_tree.item(selected, text="", values=(first_entry.get(), last_entry.get(), grad_year_entry.get(), year_entry.get(), school_entry.get(), season_entry.get(), honor_entry.get(), oid_entry.get()))

    # update database
    con = sqlite3.connect('raw.db')
    csr = con.cursor()
    csr.execute("""UPDATE raw_table SET
                first = :first,
                last = :last,
                grad_year = :grad,
                year = :year,
                school = :school,
                season = :season,
                honor = :honor
                        
            WHERE oid = :oid""", {
                'first': first_entry.get(),
                'last': last_entry.get(),
                'grad': grad_year_entry.get(),
                'year': year_entry.get(),
                'school': school_entry.get(),
                'season': season_entry.get(),
                'honor': honor_entry.get(),
                'oid': oid_entry.get()})

    con.commit()
    con.close()

    clear_entry()


# add new record to database
def add_record():
    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    con.execute("INSERT INTO raw_table VALUES (?, ?, ?, ?, ?, ?, ?)", (first_entry.get(), last_entry.get(), grad_year_entry.get(), year_entry.get(), school_entry.get(), season_entry.get(), honor_entry.get()))

    con.commit()
    con.close()

    clear_entry()


def search_database():
    global search_entry, search, j
    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")

    # select what search
    j = tk.StringVar()
    j.set("2")

    ttk.Radiobutton(search, text="First", variable=j, value="1").grid(column=1, row=1, padx=5, pady=5)
    ttk.Radiobutton(search, text="Last", variable=j, value="2").grid(column=1, row=2, padx=5, pady=5)
    ttk.Radiobutton(search, text="Grad", variable=j, value="3").grid(column=1, row=3, padx=5, pady=5)
    ttk.Radiobutton(search, text=" Year", variable=j, value="4").grid(column=1, row=4, padx=5, pady=5)
    ttk.Radiobutton(search, text="School", variable=j, value="5").grid(column=2, row=1, padx=5, pady=5)
    ttk.Radiobutton(search, text="Season", variable=j, value="6").grid(column=2, row=2, padx=5, pady=5)
    ttk.Radiobutton(search, text="Honor", variable=j, value="7").grid(column=2, row=3, padx=5, pady=5)

    search_entry = Entry(search, )
    search_entry.grid(column=1, row=5, padx=10, pady=10)
    conduct_search_button = Button(search, text="Search", command=conduct_search)
    conduct_search_button.grid(column=2, row=5, padx=10, pady=10)


# append database buttons
button_frame = LabelFrame(all_data, text="append")
button_frame.grid(column=0, row=4, padx="5", pady="5")

add_button = Button(button_frame, text="Add", command=add_record)
add_button.grid(row=0, column=0, padx=15, pady=10)

update_button = Button(button_frame, text="Update", command=update_record)
update_button.grid(row=0, column=1, padx=15, pady=10)

remove_sel_button = Button(button_frame, text="Remove One", command=remove_one)
remove_sel_button.grid(row=0, column=2, padx=15, pady=10)

remove_many_button = Button(button_frame, text="Remove Many", command=remove_many)
remove_many_button.grid(row=0, column=3, padx=15, pady=10)

select_button = Button(button_frame, text="Select", command=select_record)
select_button.grid(row=0, column=4, padx=15, pady=10)

pop_button = Button(button_frame, text="Populate", command=query_database)
pop_button.grid(row=0, column=5, padx=15, pady=10)

search_button = Button(button_frame, text="Search", command=search_database)
search_button.grid(row=0, column=6, padx=15, pady=10)

# bind Tree view
all_tree.bind("<ButtonRelease-1>", select_record)

# TODO Tab (Plums)

# Main Title
ttk.Label(plums, text="Plum Book", font=("Courier", 40, "bold"))\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(plums, text="Plums", font=("Courier", 25, "underline"))\
    .grid(column=0, row=1, padx=5, pady=5)


# calculate function
def rank_place(person, honor_list):
    total = 0

    total += honor_list[0] - 0.6
    total += honor_list[1] - 0.5
    total += honor_list[2] - 0.4
    total += honor_list[3] - 0.3
    total += honor_list[4] - 0.2
    total += honor_list[5] - 0.1
    total += honor_list[6] + 0.1
    total += honor_list[7] + 0.2
    total += honor_list[8] + 0.3
    total += honor_list[9] + 0.4
    total += honor_list[10] + 0.5
    total += honor_list[11] + 0.6
    print(total)

    plum_tree.insert(parent='', index='end', text='',
                    values=(person[0], person[1], person[2], total,))


def calculate():
    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    get_year = year_entry_calc.get()
    csr.execute("SELECT * FROM raw_table WHERE grad_year = ?", (get_year, ))
    records = csr.fetchall()

    con.commit()
    con.close()

    people_done = []
    person_honors = []
    done = FALSE

    for record in records:
        last = record[1]
        for i in people_done:
            if last == i:
                done = TRUE
                break

        if done == TRUE:
            done = FALSE
            pass
        else:
            people_done.append(last)
            for people in records:
                if people[1] == last:
                    name_lst = people
                    person_honors.append(people[6])
            print(person_honors)
            rank_place(name_lst, person_honors)
            person_honors = []


# creating year entry
year_frame = Frame(plums)
year_frame.grid(column=0, row=2, padx=5, pady=5)

year = Label(year_frame, text="Graduation Year")
year.pack(padx=5, pady=5)
year_entry_calc = Entry(year_frame)
year_entry_calc.pack(padx=5, pady=5)
calculate_button = Button(year_frame, text="Calculate", command=calculate)
calculate_button.pack(padx=5, pady=5)

# treeview
# creating treeview
style = ttk.Style()
style.configure("Treeview", background="grey40", foreground="black", rowheight=20, fieldbackground="grey10")
style.map("Treeview", background=[('selected', 'grey100')])

# treeview frame
tree_frame = Frame(plums)
tree_frame.grid(column=0, row=3, padx=5, pady=5)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
plum_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
plum_tree.pack()
tree_scroll.config(command=plum_tree.yview)

# columns
plum_tree['columns'] = ("First Name", "Last Name", "Grad Year", "Rank")
plum_tree.column("#0", width=0, stretch=NO)
plum_tree.column("First Name", anchor=W, width=100)
plum_tree.column("Last Name", anchor=W, width=100)
plum_tree.column("Grad Year", anchor=CENTER, width=100)
plum_tree.column("Rank", anchor=CENTER, width=100)

plum_tree.heading("#0", text="", anchor=W)
plum_tree.heading("First Name", text="First Name", anchor=W)
plum_tree.heading("Last Name", text="Last Name", anchor=W)
plum_tree.heading("Grad Year", text="Grad Year", anchor=CENTER)
plum_tree.heading("Rank", text="Rank", anchor=CENTER)

plum_tree.tag_configure('oddrow', background="grey50")
plum_tree.tag_configure('evenrow', background="grey70")


# Run root window
root.mainloop()
