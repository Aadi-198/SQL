#import required tools
import sqlite3

#Connect to database
conn = sqlite3.connect("customer.db")

#Create a cursor
curs = conn.cursor()

#Create a table
curs.execute("""CREATE TABLE customers (
             first_name DATATYPE,
             last_name DATATYPE,
             email  DATATYPE
             )""")

#5 Datatypes in SQLite
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

