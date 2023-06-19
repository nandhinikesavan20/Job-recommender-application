import sqlite3

conn = sqlite3.connect('job_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE jobs (keywords TEXT, jobrole TEXT, company TEXT, location TEXT,experience TEXT, ctc TEXT)')
print("Table created successfully")
conn.close()