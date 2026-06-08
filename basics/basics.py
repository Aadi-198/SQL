#import required tools
import sqlite3

#Connect to database
conn = sqlite3.connect("customer.db")

#Create a cursor
curs = conn.cursor()

#Create a table
curs.execute("""CREATE TABLE customers (
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

#commit the changes
conn.commit()

#close
conn.close()