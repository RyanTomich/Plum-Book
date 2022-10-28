from database import *


# changes list to string, removing excess spaces and enters
def str_to_lst(string):
    string = string.replace(" \n" or "\n ", " ")
    string = " ".join(string.split())
    lst = string.split(",")
    lst_final = []
    for i in lst:
        ela = i.strip()
        lst_final.append(ela)
    return lst_final


# splits full name into first and last at the space
def split_name(name):
    full_name = []
    full_name = (name.split())
    first = full_name[0]
    last = full_name[1]
    return first, last


# takes inputs from tk  and inserts them into raw.db
def rawdata_insert(first, last, grad_year, year, school, season, honor):
    con = sqlite3.connect('raw.db')
    csr = con.cursor()

    con.execute("INSERT INTO raw_table VALUES (?, ?, ?, ?, ?, ?, ?)", (first, last, grad_year, year, school, season, honor))
    con.commit()
    con.close()
