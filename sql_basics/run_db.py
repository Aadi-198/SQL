import sqlite3
import os
import pathlib

# Absolute genius move: Force Python to use the script's current directory
os.chdir(pathlib.Path(__file__).resolve().parent)

def run_sql_file():
    # Connect to SQLite (creates the database file right next to this script)
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    
    print("Reading your SQL file safely from the correct directory...")
    
    # Now this 'open' will NEVER fail with a FileNotFoundError
    with open('schema.sql', 'r') as file:
        sql_script = file.read()
        
    cursor.executescript(sql_script)

    print("Injecting bulk data...")
    with open('insert_data.sql', 'r') as file:
        data_script = file.read()
    cursor.executescript(data_script)
    
    connection.commit()
    connection.close()
    
    print("Success! Your database and table are officially live.")

if __name__ == "__main__":
    run_sql_file()