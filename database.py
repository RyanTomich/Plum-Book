import sqlite3


# establish connection to database(also creates database)
con = sqlite3.connect('raw.db')
csr = con.cursor()

'''
create table (remove if table already created)
csr.execute(""" CREATE TABLE raw_table (
                first text,
                last text,
                grad_year integer,
                year integer,
                school text,
                season integer,
                honor integer)""")
'''

csr.execute("SELECT * FROM raw_table")
#print(csr.fetchall())

# save changes to database
con.commit()
con.close()
