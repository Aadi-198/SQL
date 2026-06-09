#import required tools
import sqlite3
import os
import pathlib

#Change to current diresctory
os.chdir(pathlib.Path(__file__).resolve().parent)

#Connect to database
conn = sqlite3.connect("customer.db")

#Create a cursor
curs = conn.cursor()

#Create a table
curs.execute("""CREATE TABLE IF NOT EXISTS customers (
             first_name text,
             last_name text,
             email text
             )""")

#5 Datatypes in SQLite
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#Save the singular data
curs.execute("INSERT INTO customers VALUES ('Tom', 'Oliver', 'op@email.com')")

#Save data as a list
many_customers = [('Willam', 'Shakespear', 'will@email.com'),
                  ('Nicola', 'Tesla', 'nickdigiovani@email.com'),
                  ('su', 's', 'suspicious@email.com')]

curs.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
print("\nData Saved\n")

#commit the changes
conn.commit()

#close
conn.close()